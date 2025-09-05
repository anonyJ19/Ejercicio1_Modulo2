"""
Ejercicio 4 — Piedra, Papel o Tijeras
Descripción:
- Juego contra la computadora.
- El primero en llegar a 3 puntos gana.
"""
import random

OPCIONES = ("piedra", "papel", "tijeras")

def ganador_ronda(jugador: str, pc: str) -> str:
    """Devuelve 'jugador', 'pc' o 'empate'."""
    jugador = jugador.lower().strip()
    pc = pc.lower().strip()

    if jugador == pc:
        return "empate"
    if (
        (jugador == "piedra" and pc == "tijeras")
        or (jugador == "tijeras" and pc == "papel")
        or (jugador == "papel" and pc == "piedra")
    ):
        return "jugador"
    return "pc"

def jugar() -> None:
    jugador_puntos = 0
    pc_puntos = 0
    print("Juguemos Piedra, Papel o Tijeras. Gana quien llegue a 3.")

    while jugador_puntos < 3 and pc_puntos < 3:
        eleccion = input("Elige (piedra/papel/tijeras): ").strip().lower()
        if eleccion not in OPCIONES:
            print("Opción inválida.")
            continue

        pc = random.choice(OPCIONES)
        print(f"La PC eligió: {pc}")

        g = ganador_ronda(eleccion, pc)
        if g == "jugador":
            jugador_puntos += 1
            print("¡Ganaste la ronda!")
        elif g == "pc":
            pc_puntos += 1
            print("Perdiste la ronda.")
        else:
            print("Empate.")

        print(f"Marcador -> Tú: {jugador_puntos} | PC: {pc_puntos}\n")

    print("Juego terminado.")
    if jugador_puntos == 3:
        print("¡Ganaste la partida!")
    else:
        print("La PC ganó la partida.")

if __name__ == "__main__":
    jugar()
