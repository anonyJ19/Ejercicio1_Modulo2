"""
Ejercicio 7 — Combinar listas de estudiantes y notas
Descripción:
- Se tienen dos listas: una de nombres y otra de notas.
- Se combinan en un diccionario {nombre: nota}.
- Luego se muestra un reporte de cada estudiante.
"""

def combinar_estudiantes(nombres: list[str], notas: list[float]) -> dict[str, float]:
    """Combina nombres y notas en un diccionario."""
    return {n: nota for n, nota in zip(nombres, notas)}


def reporte_estudiantes(datos: dict[str, float]) -> str:
    """Genera un reporte con frases por estudiante."""
    lineas = [f"El estudiante {nombre} tiene una nota de {nota}" for nombre, nota in datos.items()]
    return "\n".join(lineas)


def ej7() -> None:
    nombres = ["Ana", "Luis", "María"]
    notas = [4.5, 3.8, 5.0]
    datos = combinar_estudiantes(nombres, notas)
    print(reporte_estudiantes(datos))


if __name__ == "__main__":
    ej7()
