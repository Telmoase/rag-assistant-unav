# Sistemas de numeración

**Resumen**: Descripción de los sistemas de numeración decimal, binario, octal y hexadecimal, y métodos de conversión entre ellos.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/TI_01_00a.md

**Última actualización**: 2026-05-19

---

## El sistema posicional

Los sistemas de numeración posicionales asignan a cada dígito un valor que depende de su posición. El valor de una posición es la base elevada a su índice (0, 1, 2…), multiplicado por el dígito en esa posición (fuente: TI_01_00a.md).

Ejemplo en base 10: 364 = 4×10⁰ + 6×10¹ + 3×10² = 4 + 60 + 300.

## Sistemas de numeración

| Base | Nombre | Símbolos |
|------|--------|----------|
| 10 | Decimal | 0–9 |
| 2 | Binario | 0, 1 |
| 8 | Octal | 0–7 |
| 16 | Hexadecimal | 0–9, A–F |

En hexadecimal, los valores 10–15 se representan con letras: A=10, B=11, C=12, D=13, E=14, F=15 (fuente: TI_01_00a.md).

## Conversión de decimal a otra base

Método de **divisiones sucesivas**: se divide el número entre la base repetidamente y se anotan los restos. Los restos leídos de abajo a arriba dan el número en la nueva base (fuente: TI_01_00a.md).

Ejemplo: 364 en base 8 (octal):
- 364 ÷ 8 = 45, resto **4**
- 45 ÷ 8 = 5, resto **5**
- 5 ÷ 8 = 0, resto **5**
- Resultado: **554₈**

El mismo método aplicado a base 16 da **16C₁₆**, y a base 2 da **101101100₂**.

## Conversión rápida entre binario, octal y hexadecimal

Existe una correspondencia directa que evita pasar por decimal (fuente: TI_01_00a.md):

- **Hexadecimal → Binario**: cada dígito hex equivale exactamente a 4 bits.
  - 16C → 0001 0110 1100 → 000101101100₂
- **Octal → Binario**: cada dígito octal equivale exactamente a 3 bits (8 = 2³).
  - 554₈ → 101 101 100 → 101101100₂

Ambas rutas producen el mismo número binario.

## Relevancia en informática

El binario es el sistema nativo de los ordenadores. El hexadecimal se usa en la práctica para visualizar datos binarios de forma compacta: cada byte se representa con exactamente **dos dígitos hexadecimales** (véase [[codigo-ascii]]).

## Páginas relacionadas

- [[codigo-ascii]]
- [[ti1-datos-y-tablas]]
