"""
Ejercicio 13 — Aventura de texto
Descripción:
- El programa cuenta una pequeña historia.
- El usuario elige entre dos opciones en cada paso.
- Dependiendo de lo que escoja, la historia cambia y termina.
"""

def aventura() -> None:
    print("Estás en un bosque. Hay dos caminos: izquierda o derecha.")
    eleccion1 = input("¿Qué camino tomas? (izquierda/derecha): ").strip().lower()

    if eleccion1 == "izquierda":
        print("Encuentras un río.")
        eleccion2 = input("¿Cruzas o sigues la orilla? (cruzar/orilla): ").strip().lower()
        if eleccion2 == "cruzar":
            print("El río estaba profundo... ¡te mojaste! Fin del juego.")
        else:
            print("Sigues la orilla y encuentras una cabaña. ¡Ganaste!")
    elif eleccion1 == "derecha":
        print("Te encuentras con un oso y corres de vuelta. Fin del juego.")
    else:
        print("No entendí tu elección. El juego terminó.")


if __name__ == "__main__":
    aventura()
