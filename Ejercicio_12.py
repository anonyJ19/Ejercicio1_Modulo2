"""
Ejercicio 12 — Lanzar un dado varias veces
Descripción:
- Se lanza un dado de 6 caras varias veces.
- El usuario elige cuántas veces.
- Se muestran los resultados en una lista.
"""
import random

def lanzar_dado(veces: int = 5) -> list[int]:
    """Lanza un dado de 6 caras `veces` veces y devuelve los resultados."""
    return [random.randint(1, 6) for _ in range(veces)]


def ej12() -> None:
    n = input("¿Cuántas veces quieres lanzar el dado?: ")
    if not n.isdigit():
        print("Entrada inválida. Debes ingresar un número.")
        return

    resultados = lanzar_dado(int(n))
    print("Resultados:", resultados)


if __name__ == "__main__":
    ej12()
