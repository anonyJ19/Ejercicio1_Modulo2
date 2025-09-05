"""
Ejercicio 8 — Procesar números con list comprehension
Descripción:
- A partir de una lista de números, crear:
  1. Lista de positivos
  2. Lista de cuadrados
  3. Lista con etiquetas "positivo" o "negativo"
"""

def procesar_numeros(nums: list[int]) -> tuple[list[int], list[int], list[str]]:
    """Devuelve (positivos, cuadrados, etiquetas)."""
    positivos = [n for n in nums if n > 0]
    cuadrados = [n * n for n in nums]
    etiquetas = ["positivo" if n >= 0 else "negativo" for n in nums]
    return positivos, cuadrados, etiquetas


def ej8() -> None:
    numeros = [-5, 10, -15, 20, -25, 30]
    pos, cuad, et = procesar_numeros(numeros)
    print("Números positivos:", pos)
    print("Cuadrados:", cuad)
    print("Etiquetas:", et)


if __name__ == "__main__":
    ej8()
