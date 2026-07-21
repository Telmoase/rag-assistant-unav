import os
import re
import json
import chromadb
import requests
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, Settings
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

load_dotenv()

# --- Configuracion compartida ---

Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-m3")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ASIGNATURAS_CONFIG = {
    "ti": {"carpeta_chroma": "chroma_db_wiki_ti_m3", "coleccion": "wiki_ti_m3"},
    "td": {"carpeta_chroma": "chroma_db_wiki_td_m3", "coleccion": "wiki_td_m3"},
}

ASIGNATURA_ACTIVA = os.getenv("ASIGNATURA_ACTIVA", "td").strip().lower()
if ASIGNATURA_ACTIVA not in ASIGNATURAS_CONFIG:
    print(f"Aviso: ASIGNATURA_ACTIVA '{ASIGNATURA_ACTIVA}' no reconocida, usando 'td' por defecto.")
    ASIGNATURA_ACTIVA = "td"

config_activa = ASIGNATURAS_CONFIG[ASIGNATURA_ACTIVA]
CHROMA_PATH = os.path.join(BASE_DIR, config_activa["carpeta_chroma"])

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
chroma_collection = chroma_client.get_or_create_collection(config_activa["coleccion"])
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
index = VectorStoreIndex.from_vector_store(vector_store)
retriever = index.as_retriever(similarity_top_k=3)

print(f"[core.py] Asignatura activa configurada: {ASIGNATURA_ACTIVA} (coleccion: {config_activa['coleccion']})")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "deepseek/deepseek-chat-v3-0324"

PREFIJO_A_NOMBRE = {
    "ti": "Tecnologia de la Informacion",
    "td": "Tecnologia Digital",
    "is": "Ingenieria del Software",
}


# --- Deteccion automatica de asignatura ---

def detectar_asignatura(collection):
    """
    Lee los metadatos de ChromaDB y deduce el nombre de la asignatura
    y la lista de temas a partir de los nombres de archivo indexados.
    Busca archivos con patron [prefijo][numero]-[nombre-tema].md
    y los ordena numericamente para construir la lista de temas.
    Un mismo numero de tema puede tener varios archivos asociados
    (por ejemplo, varias paginas wiki sobre el mismo tema), asi que
    se agrupan todos los archivos por numero de tema, se usa el primero
    en orden alfabetico para derivar el nombre legible del tema, y se
    devuelve la lista completa de archivos por tema, necesaria para
    recuperar el contenido completo de un tema (no solo un fragmento)
    en el Generador de Requerimientos.
    """
    try:
        resultados = collection.get(include=["metadatas"])
        metadatas = resultados.get("metadatas", [])

        archivos_unicos = set()
        for meta in metadatas:
            nombre = meta.get("file_name", "")
            if nombre:
                archivos_unicos.add(nombre)

        patron = re.compile(r'^([a-z]+)(\d+)-(.+)\.md$')
        candidatos_por_tema = {}
        prefijo_detectado = None

        for archivo in archivos_unicos:
            match = patron.match(archivo)
            if match:
                prefijo = match.group(1)
                numero = int(match.group(2))
                candidatos_por_tema.setdefault(numero, []).append(archivo)
                if prefijo_detectado is None:
                    prefijo_detectado = prefijo

        if not candidatos_por_tema:
            return "Asignatura", ["Tema general"], {}

        temas_encontrados = {}
        archivos_por_tema = {}

        for numero, archivos in candidatos_por_tema.items():
            archivos_ordenados = sorted(archivos)
            archivo_representante = archivos_ordenados[0]
            match = patron.match(archivo_representante)
            nombre_crudo = match.group(3).replace("-", " ")
            nombre_tema = nombre_crudo[0].upper() + nombre_crudo[1:] if nombre_crudo else nombre_crudo
            temas_encontrados[numero] = nombre_tema
            archivos_por_tema[numero] = archivos_ordenados

        nombre_asignatura = PREFIJO_A_NOMBRE.get(
            prefijo_detectado,
            prefijo_detectado.upper() if prefijo_detectado else "Asignatura"
        )

        temas = [
            f"Tema {num}: {nombre}"
            for num, nombre in sorted(temas_encontrados.items())
        ]

        return nombre_asignatura, temas, archivos_por_tema

    except Exception as e:
        print(f"Advertencia: no se pudo detectar la asignatura automaticamente: {e}")
        return "Asignatura", ["Tema general"], {}


ASIGNATURA_NOMBRE, TEMAS_ASIGNATURA, ARCHIVOS_POR_TEMA = detectar_asignatura(chroma_collection)
print(f"[core.py] Asignatura detectada: {ASIGNATURA_NOMBRE}")
print(f"[core.py] Temas detectados: {TEMAS_ASIGNATURA}")

# --- Llamada al LLM (con calculo de tokens y coste) ---

def llamar_llm_mensajes(mensajes):
    """
    Funcion base que llama a DeepSeek-V3 via OpenRouter con una lista de
    mensajes ya construida (formato {"role": "system"/"user"/"assistant",
    "content": "..."}). Es la version generalizada de llamar_llm, que solo
    aceptaba un system_prompt y un user_message sueltos, sin posibilidad
    de historial de conversacion.

    Se usa tanto desde llamar_llm (caso simple de una sola pregunta) como
    desde conversar (caso con historial completo de turnos).

    Devuelve (texto, tokens_info), igual que llamar_llm.
    """
    mensajes_con_cache = []
    for msg in mensajes:
        if msg["role"] == "system":
            mensajes_con_cache.append({
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": msg["content"],
                        "cache_control": {"type": "ephemeral"}
                    }
                ]
            })
        else:
            mensajes_con_cache.append(msg)

    payload = {
        "model": MODEL,
        "messages": mensajes_con_cache,
        "temperature": 0.5,
        "max_tokens": 1500,
        "frequency_penalty": 0.3
    }
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    or_response = requests.post(OPENROUTER_URL, headers=headers, json=payload)
    or_data = or_response.json()
    texto = or_data["choices"][0]["message"]["content"].strip()

    usage = or_data.get("usage", {})
    print(f"[DEBUG usage] {usage}")
    prompt_tokens = usage.get("prompt_tokens", 0)
    completion_tokens = usage.get("completion_tokens", 0)
    total_tokens = usage.get("total_tokens", 0)
    coste = (prompt_tokens * 0.27 / 1_000_000) + (completion_tokens * 1.10 / 1_000_000)

    tokens_info = {
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": total_tokens,
        "coste_usd": round(coste, 6)
    }
    return texto, tokens_info


def llamar_llm(system_prompt, user_message):
    """
    Llama a DeepSeek-V3 via OpenRouter con una sola pregunta suelta, sin
    historial. Mantiene la firma original para no romper nada que ya use
    esta funcion (mcp_server.py incluido, aunque este en pausa; el
    Generador de Requerimientos y el Detector de Lagunas tambien la usan
    asi, sin historial).

    Por debajo, construye la lista de 2 mensajes y delega en la funcion
    general llamar_llm_mensajes.
    """
    mensajes = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
    return llamar_llm_mensajes(mensajes)


# --- Parseo robusto de JSON devuelto por el LLM ---

def parsear_json_llm(texto):
    """
    Limpia fences de markdown (```json ... ```) que el LLM a veces anade
    pese a las instrucciones del prompt, y parsea el resultado como JSON.
    Lanza json.JSONDecodeError si el texto limpio no es JSON valido;
    quien llame a esta funcion debe capturar esa excepcion.
    """
    texto_limpio = texto.strip()
    if texto_limpio.startswith("```"):
        texto_limpio = texto_limpio.split("\n", 1)[1]
    if texto_limpio.endswith("```"):
        texto_limpio = texto_limpio.rsplit("```", 1)[0]
    texto_limpio = texto_limpio.strip()
    return json.loads(texto_limpio)


def extraer_json(texto):
    """
    Aisla un objeto JSON dentro de un texto que pueda contener texto
    adicional antes o despues, buscando desde la primera '{' hasta la
    ultima '}'. Util cuando el LLM anade comentarios pese a las
    instrucciones del prompt.
    """
    inicio = texto.find('{')
    fin = texto.rfind('}')
    if inicio != -1 and fin != -1 and fin > inicio:
        return texto[inicio:fin + 1]
    return texto


# --- Recuperacion de contexto completo de un tema (por metadato exacto) ---

def obtener_contexto_completo_tema(archivos_tema):
    """
    Recupera todos los chunks de los archivos correspondientes a un tema,
    filtrando por metadato file_name en ChromaDB. Acepta una lista de
    archivos porque un mismo tema puede estar repartido en varios ficheros
    de la wiki. Esto garantiza cobertura completa del tema en vez de
    depender de similitud semantica.
    """
    if isinstance(archivos_tema, str):
        archivos_tema = [archivos_tema]

    resultados = chroma_collection.get(
        where={"file_name": {"$in": archivos_tema}},
        include=["documents"]
    )
    documentos = resultados.get("documents", [])
    return "\n\n".join(documentos)


# --- Sistema conversacional nuevo: prompt general unico + iteracion ---

SYSTEM_PROMPT_GENERAL = """Eres un asistente academico de la asignatura {asignatura} de la Universidad de Navarra.

REGLA DE FIDELIDAD AL CONTENIDO:
Responde siempre en español.
Basa tu respuesta principalmente en el contexto proporcionado del material de la asignatura.
Si la respuesta está en el contexto, úsalo como fuente principal y no añadas información externa.
Si la pregunta no tiene relación con el material de la asignatura o el contexto no contiene información suficiente,
puedes responder con conocimiento general, pero indica explícitamente al usuario que esa información
no proviene del material de la asignatura.
No inventes información que no esté en el contexto ni atribuyas al material algo que no aparece en él.

QUE PUEDE PEDIR EL USUARIO:
El usuario puede ser un estudiante o un profesor. Puede pedir cualquier formato útil para
estudiar, preparar clase o trabajar con el tema: resúmenes, esquemas, explicaciones,
comparaciones, ejercicios, exámenes, flashcards, slides, o cualquier otra cosa que se le
ocurra. No estás limitado a una lista cerrada de funciones.

ITERACION SOBRE RESPUESTAS ANTERIORES:
Si el usuario pide un cambio sobre algo que generaste antes en esta misma conversacion
("cambia esto", "anade aquello", "hazlo mas corto", "no me gusta esta part"), debes modificar
especificamente lo que se te pide, conservando el resto de la respuesta anterior tal cual estaba.
No regeneres todo desde cero ignorando lo que ya existia, salvo que el usuario pida explicitamente
empezar de nuevo.

PLAYGROUNDS INTERACTIVOS (codigo ejecutable en el navegador):
Cuando expliques un concepto que se apoye en codigo HTML, CSS o JavaScript ejecutable
directamente en un navegador (por ejemplo, graficos con Chart.js, manipulacion del DOM,
formularios interactivos, animaciones CSS), puedes incluir un bloque especial de codigo
editable usando un fence con la etiqueta playground, asi:

```playground
<canvas id="c" width="400" height="200"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
new Chart(document.getElementById('c'), {{
  type: 'bar',
  data: {{ labels: ['Ene','Feb','Mar'], datasets: [{{ label: 'Ventas', data: [10,20,15] }}] }}
}});
</script>
```

Reglas para el playground:
- Solo usalo para codigo que se ejecuta en el navegador (HTML/CSS/JS). NUNCA para Python, SQL,
  Java u otro codigo que no pueda correr dentro de un iframe del navegador.
- El bloque debe ser autocontenido: si usas una libreria externa (como Chart.js), incluye su
  script de carga dentro del propio bloque playground, no fuera de el.
- No abuses de esto: usalo solo cuando el codigo interactivo aporte valor real a la explicacion,
  no en cada respuesta.
- El resto de tu respuesta (la explicacion en prosa) va fuera del bloque playground, en markdown
  normal, como el resto de TIPO:TEXTO.

FORMATO DE RESPUESTA, OBLIGATORIO:
Toda tu respuesta debe empezar, en la primera linea, por una de estas dos etiquetas exactas:

TIPO:JSON
TIPO:TEXTO

Usa TIPO:JSON unicamente cuando el usuario pida un EXAMEN (preguntas de evaluacion) o
FLASHCARDS (tarjetas de estudio frente/dorso). Para cualquier otra peticion, usa TIPO:TEXTO.

Si usas TIPO:JSON para un examen, la segunda linea en adelante debe ser un array JSON valido
con esta forma exacta, sin texto adicional ni fences de markdown:
[{{"pregunta": "texto de la pregunta", "respuesta_correcta": "respuesta de referencia"}}]

Si usas TIPO:JSON para flashcards, la segunda linea en adelante debe ser un array JSON valido
con esta forma exacta:
[{{"frente": "pregunta o concepto", "dorso": "respuesta o explicacion"}}]

Si usas TIPO:TEXTO, la segunda linea en adelante es markdown libre con tu respuesta completa.
Los bloques playground descritos arriba tambien van dentro de TIPO:TEXTO.

Ejemplo de respuesta para una peticion de examen de 2 preguntas:
TIPO:JSON
[{{"pregunta": "Que es la normalizacion de bases de datos?", "respuesta_correcta": "Es el proceso de organizar..."}}, {{"pregunta": "Que es la primera forma normal?", "respuesta_correcta": "..."}}]

Ejemplo de respuesta para un resumen:
TIPO:TEXTO
## Resumen de Normalizacion de bases de datos

La normalizacion es un proceso que organiza los datos para evitar redundancia...

Ejemplo de respuesta para una peticion sobre Chart.js con ejemplo interactivo:
TIPO:TEXTO
## Chart.js: graficos interactivos en el navegador

Chart.js es una libreria JavaScript para crear graficos usando un elemento canvas. Puedes
probar y modificar este ejemplo directamente:

```playground
<canvas id="c" width="400" height="200"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
new Chart(document.getElementById('c'), {{
  type: 'bar',
  data: {{ labels: ['Ene','Feb','Mar'], datasets: [{{ label: 'Ventas', data: [10,20,15] }}] }}
}});
</script>
```

Cambia el tipo bar por line o pie para ver otros tipos de grafico.
"""


def construir_system_prompt(asignatura):
    """
    Construye el system prompt general insertando el nombre de la asignatura.
    No llama a ningun servicio externo, solo rellena la plantilla con texto.
    """
    return SYSTEM_PROMPT_GENERAL.format(asignatura=asignatura)


def conversar(historial_mensajes, contexto, asignatura):
    """
    Funcion central del bucle conversacional. Sustituye a las llamadas sueltas
    que antes usaban core.PROMPTS["resumen"], core.PROMPTS["examen"], etc.

    Parametros:
        historial_mensajes: lista de dicts [{"role": "user"/"assistant", "content": "..."}]
                             con toda la conversacion hasta ahora (sin incluir el system prompt).
        contexto: string con los chunks recuperados de ChromaDB relevantes para el turno actual.
                  Puede ser un string vacio si no hizo falta recuperar contexto nuevo
                  (por ejemplo, si el turno es una edicion sobre algo ya generado).
        asignatura: nombre de la asignatura, normalmente ASIGNATURA_NOMBRE.

    Devuelve una tupla (tipo, contenido, tokens_info):
        tipo: "json" o "texto"
        contenido: si tipo es "json", una lista de dicts ya parseada (examen o flashcards).
                   si tipo es "texto", el string de markdown tal cual (puede incluir bloques
                   playground embebidos, sin procesar aqui; eso lo hace el frontend).
        tokens_info: lo que devuelve llamar_llm_mensajes, para seguir registrando coste.

    Lanza ValueError si el modelo indica TIPO:JSON pero el contenido no es JSON
    valido. Quien llame a esta funcion debe capturar esa excepcion y decidir
    como mostrarsela al usuario.
    """
    system_prompt = construir_system_prompt(asignatura)

    if contexto:
        mensaje_contexto = f"Contexto del material de la asignatura:\n{contexto}\n\n"
    else:
        mensaje_contexto = ""

    mensajes_completos = [{"role": "system", "content": system_prompt}]
    mensajes_completos.extend(historial_mensajes)

    # Si hay contexto nuevo de ChromaDB para este turno, se anade al ultimo
    # mensaje del usuario (no como mensaje aparte), para que quede claro que
    # es informacion de apoyo para responder justo a lo que acaba de pedir.
    if mensaje_contexto and mensajes_completos[-1]["role"] == "user":
        mensajes_completos[-1]["content"] = mensaje_contexto + mensajes_completos[-1]["content"]

    texto_respuesta, tokens_info = llamar_llm_mensajes(mensajes_completos)

    primera_linea, _, resto = texto_respuesta.partition("\n")
    primera_linea = primera_linea.strip()

    if primera_linea == "TIPO:JSON":
        try:
            contenido = parsear_json_llm(resto.strip())
        except Exception as e:
            raise ValueError(
                f"El modelo indico TIPO:JSON pero el contenido no es JSON valido: {e}\n"
                f"Respuesta cruda: {texto_respuesta}"
            )
        return "json", contenido, tokens_info

    elif primera_linea == "TIPO:TEXTO":
        return "texto", resto.strip(), tokens_info

    else:
        return "texto", texto_respuesta.strip(), tokens_info


# --- Decision de si hace falta retrieval nuevo en cada turno ---
#
# Antes de generar la respuesta con conversar(), el sistema decide si el
# turno actual necesita buscar contenido nuevo en ChromaDB  o si
# puede responder con lo que ya esta en el historial. Esta decision tambien la toma el
# LLM, con el mismo patron de etiqueta usado en TIPO:JSON/TIPO:TEXTO.

PROMPT_DECISION_BUSQUEDA = """Tu unica tarea es decidir si, para responder al ultimo mensaje del
usuario en esta conversacion, hace falta buscar contenido nuevo en el material indexado de la
asignatura, o si ya hay suficiente informacion en la propia conversacion para responder.

Hace falta buscar contenido nuevo cuando el usuario pregunta sobre un tema, concepto o parte de
la asignatura que no se ha tratado todavia en la conversacion.

NO hace falta buscar contenido nuevo cuando el usuario pide modificar, acortar, ampliar, corregir
o cambiar el formato de algo que el asistente ya genero antes en esta misma conversacion. En ese
caso, la informacion ya esta disponible en el historial.

Responde EXACTAMENTE en uno de estos dos formatos, sin nada mas:

BUSCAR:NO

o bien:

BUSCAR:SI
una consulta breve y clara para buscar en el material indexado, reformulada si hace falta para
que tenga sentido por si misma sin depender del resto de la conversacion

Ejemplo 1, el usuario pregunta por un tema nuevo:
BUSCAR:SI
Normalizacion de bases de datos, primera y segunda forma normal

Ejemplo 2, el usuario pide editar algo que ya se genero antes:
BUSCAR:NO
"""


def decidir_busqueda(historial_mensajes):
    """
    Decide si el turno actual necesita retrieval nuevo de ChromaDB, y con que
    consulta, basandose en el historial completo de la conversacion.

    Parametros:
        historial_mensajes: la misma lista de turnos que se le pasa a conversar(),
                             incluyendo ya el ultimo mensaje del usuario.

    Devuelve una tupla (hace_falta_buscar, consulta):
        hace_falta_buscar: booleano.
        consulta: string con la consulta a usar en el retriever si hace_falta_buscar
                  es True, o None si es False.

    Si el modelo no responde en el formato esperado, por seguridad se asume que
    SI hace falta buscar, usando el ultimo mensaje del usuario tal cual como
    consulta. Es mas barato hacer una busqueda de mas que perder contexto real
    por una respuesta mal formateada.
    """
    mensajes = [{"role": "system", "content": PROMPT_DECISION_BUSQUEDA}]
    mensajes.extend(historial_mensajes)

    texto_respuesta, tokens_info = llamar_llm_mensajes(mensajes)

    primera_linea, _, resto = texto_respuesta.partition("\n")
    primera_linea = primera_linea.strip()

    if primera_linea == "BUSCAR:NO":
        return False, None

    if primera_linea == "BUSCAR:SI":
        consulta = resto.strip()
        if not consulta:
            consulta = historial_mensajes[-1]["content"]
        return True, consulta

    return True, historial_mensajes[-1]["content"]


# --- Prompt del Generador de Requerimientos Evaluables ---

def construir_prompt_requerimientos(asignatura):
    return (
        f"Eres un asistente experto en diseno curricular para la asignatura "
        f"{asignatura} de la Universidad de Navarra.\n\n"
        "Vas a generar UN requerimiento evaluable para el bloque tematico que se te "
        "indique, basandote UNICAMENTE en el contenido proporcionado.\n\n"
        "El requerimiento debe seguir EXACTAMENTE esta estructura:\n"
        "- Descripcion: que debe implementar el estudiante para cubrir este bloque.\n"
        "- Test asociado: ejercicio practico para evaluar el requerimiento en clase.\n"
        "- Entregable: criterios objetivos y observables de lo que debe contener la entrega.\n"
        "- Tecnologias / Conceptos: que herramientas o conceptos se aplican.\n\n"
        "Reglas obligatorias para disenar el test asociado:\n"
        "1. El test NO repite el trabajo que ya hizo el estudiante. Usa una version "
        "generica, modificada o parcialmente rota de la funcionalidad.\n"
        "2. Debe requerir comprension real: crear algo nuevo, identificar que falta, "
        "corregir un error concreto o completar algo incompleto.\n"
        "3. Scope acotado: resoluble en 20-30 minutos.\n"
        "4. Debe apuntar al error o confusion conceptual mas comun de este bloque.\n\n"
        "DEBES responder UNICAMENTE con un JSON valido, sin texto adicional, sin "
        "explicaciones, sin bloques de codigo markdown.\n"
        "No incluyas comillas dobles dentro de los valores de texto; si necesitas citar "
        "un ejemplo literal, usa comillas simples en su lugar.\n"
        "Formato exacto (usa esta estructura literal, solo cambia el contenido):\n"
        "{\n"
        '  "tema": "...",\n'
        '  "descripcion": "...",\n'
        '  "test_asociado": "...",\n'
        '  "entregable": "...",\n'
        '  "tecnologias_conceptos": ["...", "..."]\n'
        "}\n\n"
        "No escribas nada fuera del JSON. Responde siempre en espanol."
    )

# --- Prompt del modo Examen cronometrado ---

def construir_prompt_examen_generar(asignatura, num_preguntas):
    return (
        f"Eres un profesor de {asignatura} de la Universidad de Navarra.\n"
        "Basandote UNICAMENTE en el siguiente contexto, genera exactamente "
        f"{num_preguntas} preguntas de examen.\n"
        "Las preguntas pueden requerir respuestas de texto o codigo segun el tema.\n"
        "DEBES responder UNICAMENTE con un array JSON valido, sin texto adicional, "
        "sin explicaciones, sin bloques de codigo markdown.\n"
        "Formato exacto:\n"
        '[\n'
        '  {"pregunta": "...", "respuesta_correcta": "..."},\n'
        '  {"pregunta": "...", "respuesta_correcta": "..."}\n'
        ']\n'
        "No escribas nada fuera del array JSON."
    )

# --- Prompt del modo Evaluacion de examen ---

def construir_prompt_examen_evaluar(asignatura):
    return (
        f"Eres un profesor evaluando un examen de {asignatura}.\n"
        "Para cada pregunta, compara la respuesta del usuario con la respuesta correcta.\n"
        "Si la respuesta es codigo, evalua si la logica es correcta aunque la sintaxis sea ligeramente distinta.\n"
        "DEBES responder UNICAMENTE con un array JSON valido, sin texto adicional, "
        "sin explicaciones, sin bloques de codigo markdown.\n"
        "Formato exacto:\n"
        '[\n'
        '  {\n'
        '    "pregunta": "...",\n'
        '    "respuesta_usuario": "...",\n'
        '    "respuesta_correcta": "...",\n'
        '    "resultado": "correcto" | "parcial" | "incorrecto",\n'
        '    "comentario": "explicacion breve"\n'
        '  }\n'
        ']\n'
        "No escribas nada fuera del array JSON."
    )

# --- Prompt del Detector de Lagunas en el Temario ---

def construir_prompt_lagunas(asignatura):
    return (
        "Eres un revisor academico especializado en material docente universitario.\n"
        f"Vas a analizar el siguiente material de la asignatura {asignatura}.\n"
        "Tu tarea es identificar LAGUNAS REALES en el material, no sugerencias de mejora general.\n\n"
        "Una laguna es una de estas situaciones concretas:\n"
        "1. Un termino tecnico que se usa pero nunca se define en el material\n"
        "2. Un concepto que se menciona como conocimiento previo sin haber sido introducido\n"
        "3. Un apartado que el indice promete pero cuyo contenido es escaso o superficial\n"
        "4. Una relacion entre conceptos que se da por obvia pero no se explica\n\n"
        "Para cada laguna encontrada responde UNICAMENTE con un array JSON valido.\n"
        "Sin texto adicional, sin explicaciones, sin bloques de codigo markdown.\n"
        "Formato exacto:\n"
        '[\n'
        '  {\n'
        '    "tipo": "Termino sin definir" | "Conocimiento previo no introducido" | "Contenido escaso" | "Relacion no explicada",\n'
        '    "concepto": "nombre del termino o concepto afectado",\n'
        '    "cita": "fragmento literal breve del material donde aparece el problema",\n'
        '    "sugerencia": "que deberia anadirse o explicarse"\n'
        '  }\n'
        ']\n'
        "Si no encuentras lagunas reales, devuelve un array vacio: []\n"
        "No inventes lagunas. Solo reporta lo que realmente falta.\n"
        "Responde siempre en espanol."
    )