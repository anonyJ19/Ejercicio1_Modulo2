"""
Ejercicio 10 — Transponer una matriz
Descripción:
- Dada una matriz (lista de listas), se debe transponer.
- Es decir, convertir las filas en columnas.
- Se hace con bucles for y con list comprehension.
"""

def transponer_for(matriz: list[list[int]]) -> list[list[int]]:
    """Transpone usando bucles for anidados."""
    if not matriz:
        return []

    filas = len(matriz)
    columnas = len(matriz[0])
    resultado: list[list[int]] = []

    for c in range(columnas):
        nueva_fila: list[int] = []
        for f in range(filas):
            nueva_fila.append(matriz[f][c])
        resultado.append(nueva_fila)

    return resultado


def transponer_comp(matriz: list[list[int]]) -> list[list[int]]:
    """Transpone usando list comprehension."""
    return [[fila[c] for fila in matriz] for c in range(len(matriz[0]))] if matriz else []


def ej10() -> None:
    matriz = [[1, 2, 3], [4, 5, 6]]
    print("Matriz original:", matriz)
    print("Transpuesta (for):", transponer_for(matriz))
    print("Transpuesta (comprehension):", transponer_comp(matriz))


if __name__ == "__main__":
    ej10()
