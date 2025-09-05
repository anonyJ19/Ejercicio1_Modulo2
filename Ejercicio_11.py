"""
Ejercicio 11 — Verificar si cédula es válida

Descripción:
- Una cédula es válida si solo contiene dígitos.
- Debe tener entre 6 y 10 caracteres.
"""

def cedula_valida(cedula: str) -> bool:
    """Devuelve True si la cédula es válida."""
    return cedula.isdigit() and 6 <= len(cedula) <= 10


def ej11() -> None:
    ced = input("Ingresa tu número de cédula: ")
    if cedula_valida(ced):
        print("Cédula válida.")
    else:
        print("Cédula inválida.")


if __name__ == "__main__":
    ej11()
