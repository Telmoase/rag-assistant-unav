import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import core

app = Flask(__name__, static_folder="static", static_url_path="")
CORS(app)

PROFESOR_PASSWORD = "unav2026"

ASIGNATURA_NOMBRE = core.ASIGNATURA_NOMBRE
TEMAS_ASIGNATURA = core.TEMAS_ASIGNATURA
ARCHIVOS_POR_TEMA = core.ARCHIVOS_POR_TEMA

print(f"Asignatura detectada: {ASIGNATURA_NOMBRE}")
print(f"Temas detectados: {TEMAS_ASIGNATURA}")
print("Pipeline RAG cargado correctamente.")

# --- Rutas Flask ---

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/profesor")
def profesor_login():
    return app.send_static_file("profesor.html")

@app.route("/panel-profesor")
def panel_profesor():
    return app.send_static_file("panel-profesor.html")


# --- Chat conversacional nuevo ---

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    historial = data.get("historial", [])

    if not historial:
        return jsonify({"error": "Historial vacio"}), 400

    if historial[-1].get("role") != "user":
        return jsonify({"error": "El ultimo mensaje del historial debe ser del usuario"}), 400

    # Paso 1: decidir si hace falta retrieval nuevo en ChromaDB.
    hace_falta_buscar, consulta_busqueda = core.decidir_busqueda(historial)

    print(f"\n--- DECISION DE BUSQUEDA ---")
    print(f"Ultimo mensaje del usuario: {historial[-1]['content'][:100]}")
    print(f"Hace falta buscar: {hace_falta_buscar}")
    print(f"Consulta usada: {consulta_busqueda}")

    contexto = ""
    fuentes = []
    if hace_falta_buscar:
        nodos = core.retriever.retrieve(consulta_busqueda)
        contexto = "\n\n".join([n.text for n in nodos])
        print(f"Archivos recuperados: {[n.metadata.get('file_name', 'desconocido') for n in nodos]}")
        print(f"Scores: {[round(n.score, 3) if n.score else None for n in nodos]}")
        for nodo in nodos:
            fuentes.append({
                "archivo": nodo.metadata.get("file_name", "desconocido"),
                "texto": nodo.text[:200],
                "score": round(nodo.score, 3) if nodo.score else None,
            })
    print(f"-----------------------------\n")

    # Paso 2: generar la respuesta conversacional, con o sin contexto nuevo.
    #
    # Si el modelo dijo TIPO:JSON pero el contenido no parseo bien, conversar()
    # lanza ValueError. En vez de devolver un error al usuario, se trata como
    # si la respuesta hubiera sido texto libre, mostrando el texto crudo del
    # modelo. Esto es coherente con el criterio de tolerancia ya aplicado
    # dentro de conversar(): es mas seguro mostrar algo legible que romper
    # la conversacion por un fallo de formato.
    try:
        tipo, contenido, tokens_conversar = core.conversar(
            historial_mensajes=historial,
            contexto=contexto,
            asignatura=ASIGNATURA_NOMBRE
        )
    except ValueError as e:
        tipo = "texto"
        contenido = (
            "No he podido generar el formato estructurado esperado, "
            "asi que te dejo la respuesta tal como la genere:\n\n"
            f"{e}"
        )
        tokens_conversar = {
            "prompt_tokens": 0, "completion_tokens": 0,
            "total_tokens": 0, "coste_usd": 0.0
        }

    if tipo == "texto" and contenido.strip() == "SIN_CONTENIDO":
        return jsonify({
            "tipo": "texto",
            "contenido": "SIN_CONTENIDO",
            "fuentes": [],
            "busqueda_realizada": hace_falta_buscar,
            "tokens": tokens_conversar
        })

    return jsonify({
        "tipo": tipo,
        "contenido": contenido,
        "fuentes": fuentes,
        "busqueda_realizada": hace_falta_buscar,
        "consulta_busqueda": consulta_busqueda if hace_falta_buscar else None,
        "tokens": tokens_conversar
    })


# --- Examen cronometrado  ---

@app.route("/api/examen/generar", methods=["POST"])
def examen_generar():
    data = request.get_json()
    tema = data.get("tema", "").strip()
    num_preguntas = data.get("num_preguntas", 4)

    if not tema:
        return jsonify({"error": "Tema vacio"}), 400

    try:
        num_preguntas = int(num_preguntas)
        if num_preguntas not in [4, 6, 8]:
            num_preguntas = 4
    except:
        num_preguntas = 4

    nodos = core.retriever.retrieve(tema)
    contexto = "\n\n".join([n.text for n in nodos])

    system_prompt = core.construir_prompt_examen_generar(ASIGNATURA_NOMBRE, num_preguntas)

    user_message = f"Contexto:\n{contexto}\n\nTema del examen: {tema}"
    texto, tokens_info = core.llamar_llm(system_prompt, user_message)

    try:
        preguntas = core.parsear_json_llm(texto)
    except json.JSONDecodeError:
        return jsonify({"error": "El LLM no devolvio JSON valido", "raw": texto}), 500

    return jsonify({"preguntas": preguntas, "tokens": tokens_info})


@app.route("/api/examen/evaluar", methods=["POST"])
def examen_evaluar():
    data = request.get_json()
    preguntas = data.get("preguntas", [])
    respuestas_usuario = data.get("respuestas_usuario", [])

    if not preguntas or not respuestas_usuario:
        return jsonify({"error": "Faltan preguntas o respuestas"}), 400

    if len(preguntas) != len(respuestas_usuario):
        return jsonify({"error": "El numero de preguntas y respuestas no coincide"}), 400

    evaluacion_input = ""
    for i, (p, r) in enumerate(zip(preguntas, respuestas_usuario)):
        evaluacion_input += (
            f"Pregunta {i+1}: {p['pregunta']}\n"
            f"Respuesta correcta: {p['respuesta_correcta']}\n"
            f"Respuesta del usuario: {r}\n\n"
        )

    system_prompt = core.construir_prompt_examen_evaluar(ASIGNATURA_NOMBRE)

    user_message = f"Evaluacion:\n{evaluacion_input}"
    texto, tokens_info = core.llamar_llm(system_prompt, user_message)

    try:
        resultados = core.parsear_json_llm(texto)
    except json.JSONDecodeError:
        return jsonify({"error": "El LLM no devolvio JSON valido", "raw": texto}), 500

    puntuacion = sum(1 for r in resultados if r.get("resultado") == "correcto")
    puntuacion_parcial = sum(0.5 for r in resultados if r.get("resultado") == "parcial")
    total = len(resultados)

    return jsonify({
        "resultados": resultados,
        "puntuacion": puntuacion + puntuacion_parcial,
        "total": total,
        "tokens": tokens_info
    })


# --- Panel del Profesor ---

@app.route("/api/profesor/login", methods=["POST"])
def profesor_login_api():
    data = request.get_json()
    password = data.get("password", "").strip()
    if password == PROFESOR_PASSWORD:
        return jsonify({"ok": True})
    return jsonify({"ok": False, "error": "Contrasena incorrecta"}), 401


@app.route("/api/profesor/temas", methods=["GET"])
def profesor_temas():
    return jsonify({"temas": TEMAS_ASIGNATURA})


@app.route("/api/profesor/analizar", methods=["POST"])
def profesor_analizar():
    data = request.get_json()
    tema = data.get("tema", "").strip()

    if not tema:
        return jsonify({"error": "Tema vacio"}), 400

    retriever_amplio = core.index.as_retriever(similarity_top_k=15)
    nodos = retriever_amplio.retrieve(tema)
    nodos_ordenados = sorted(nodos, key=lambda n: n.metadata.get("file_name", ""))
    contexto = "\n\n".join([n.text for n in nodos_ordenados])

    system_prompt = core.construir_prompt_lagunas(ASIGNATURA_NOMBRE)

    user_message = f"Tema a analizar: {tema}\n\nMaterial:\n{contexto}"
    texto, tokens_info = core.llamar_llm(system_prompt, user_message)

    try:
        lagunas = core.parsear_json_llm(texto)
    except json.JSONDecodeError:
        return jsonify({"error": "El LLM no devolvio JSON valido", "raw": texto}), 500

    return jsonify({
        "tema": tema,
        "lagunas": lagunas,
        "chunks_analizados": len(nodos),
        "tokens": tokens_info
    })


@app.route("/api/profesor/requerimientos", methods=["POST"])
def profesor_requerimientos():
    if not ARCHIVOS_POR_TEMA:
        return jsonify({"error": "No se detectaron temas con archivos asociados"}), 500

    system_prompt = core.construir_prompt_requerimientos(ASIGNATURA_NOMBRE)
    requerimientos = []
    tokens_acumulados = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0, "coste_usd": 0.0}

    for numero in sorted(ARCHIVOS_POR_TEMA.keys()):
        archivo_tema = ARCHIVOS_POR_TEMA[numero]
        tema_nombre = next((t for t in TEMAS_ASIGNATURA if t.startswith(f"Tema {numero}:")), f"Tema {numero}")

        contexto = core.obtener_contexto_completo_tema(archivo_tema)
        if not contexto.strip():
            requerimientos.append({"tema": tema_nombre, "error": "No se encontro contenido indexado para este tema"})
            continue

        user_message = f"Bloque tematico: {tema_nombre}\n\nContenido del bloque:\n{contexto}"
        texto, tokens_info = core.llamar_llm(system_prompt, user_message)

        try:
            texto_limpio = texto.strip()
            if texto_limpio.startswith("```"):
                texto_limpio = texto_limpio.split("\n", 1)[1]
            if texto_limpio.endswith("```"):
                texto_limpio = texto_limpio.rsplit("```", 1)[0]
            texto_limpio = core.extraer_json(texto_limpio.strip())
            requerimiento = json.loads(texto_limpio)
            requerimiento["tema"] = tema_nombre
        except json.JSONDecodeError:
            requerimiento = {"tema": tema_nombre, "error": "El LLM no devolvio JSON valido", "raw": texto}

        requerimientos.append(requerimiento)

        for clave in ["prompt_tokens", "completion_tokens", "total_tokens"]:
            tokens_acumulados[clave] += tokens_info.get(clave, 0)
        tokens_acumulados["coste_usd"] += tokens_info.get("coste_usd", 0)

    tokens_acumulados["coste_usd"] = round(tokens_acumulados["coste_usd"], 6)

    return jsonify({
        "asignatura": ASIGNATURA_NOMBRE,
        "requerimientos": requerimientos,
        "tokens": tokens_acumulados
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)