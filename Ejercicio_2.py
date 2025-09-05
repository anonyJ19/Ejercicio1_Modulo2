"""
Ejercicio 2 — Intérprete de comandos
Descripción:
- Programa que funciona como un pequeño intérprete.
- Repite hasta que el usuario escriba "salir".
- Comandos aceptados: guardar, cargar, salir.
"""

def interprete_comandos() -> None:
    print(" guardar | cargar | salir")
    while True:
        cmd = input(">>> ").strip().lower()

        if cmd == "guardar":
            print("Guardando archivo...")
        elif cmd == "cargar":
            print("Cargando archivo...")
        elif cmd == "salir":
            print("Saliendo del intérprete. ¡Adiós!")
            break
        else:
            print("Comando no válido. Intenta de nuevo.")


if __name__ == "__main__":
    interprete_comandos()
