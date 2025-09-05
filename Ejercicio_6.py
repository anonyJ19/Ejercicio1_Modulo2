"""
Ejercicio 6 — Índices de una letra en una frase
Descripción:
- El usuario escribe una frase y una letra.
- El programa devuelve en qué posiciones aparece esa letra.
"""

def encontrar_indices(frase: str, letra: str) -> list[int]:
    """Devuelve una lista con los índices donde aparece `letra` en `frase`."""
    if not letra:
        return []
    ch = letra[0]  # solo tomamos el primer carácter
    posiciones: list[int] = []

    for idx, c in enumerate(frase):
        if c == ch:
            posiciones.append(idx)
    return posiciones


def ej6() -> None:
    frase = input("Escribe una frase: ")
    letra = input("¿Qué letra quieres buscar?: ")

    indices = encontrar_indices(frase, letra)
    if indices:
        print(f"La letra '{letra[0]}' aparece en las posiciones: {indices}")
    else:
        print(f"La letra '{letra[0]}' no aparece en la frase.")


if __name__ == "__main__":
    ej6()
