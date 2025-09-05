"""
Ejercicio 14 — Juego del Ahorcado
Descripción:
- La computadora elige una palabra (por defecto "python").
- El jugador debe adivinar letra por letra.
- Tiene 6 intentos para fallar.
"""

def ahorcado(palabra: str = "python") -> None:
    letras_adivinadas: list[str] = []
    intentos = 6

    while intentos > 0:
        estado = "".join([letra if letra in letras_adivinadas else "_" for letra in palabra])
        print("Palabra:", estado)

        if "_" not in estado:
            print("¡Ganaste! La palabra era:", palabra)
            return

        letra = input("Adivina una letra: ").lower()
        if letra in palabra and letra not in letras_adivinadas:
            letras_adivinadas.append(letra)
            print("¡Bien!")
        else:
            intentos -= 1
            print("Fallaste. Intentos restantes:", intentos)

    print("Perdiste. La palabra era:", palabra)


if __name__ == "__main__":
    ahorcado("perro")
