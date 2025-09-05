"""
Ejercicio 3 — Validador de contraseña
Descripción:
- El programa valida si una contraseña cumple con los requisitos.
Reglas mínimas:
1. Tener al menos 8 caracteres.
2. Incluir al menos una letra mayúscula.
3. Incluir al menos un número.
"""

def validar_contrasena(pwd: str) -> tuple[bool, list[str]]:
    """Valida una contraseña y devuelve (es_valida, lista_de_errores)."""
    errores: list[str] = []

    if len(pwd) < 8:
        errores.append("Debe tener al menos 8 caracteres.")
    if not any(ch.isupper() for ch in pwd):
        errores.append("Debe incluir al menos una letra mayúscula.")
    if not any(ch.isdigit() for ch in pwd):
        errores.append("Debe incluir al menos un número.")

    return (len(errores) == 0, errores)


def ej3() -> None:
    while True:
        pwd = input("Crea una contraseña: ")
        ok, errs = validar_contrasena(pwd)
        if ok:
            print("¡Contraseña válida!")
            break
        else:
            print("No válida:")
            for e in errs:
                print(" -", e)


if __name__ == "__main__":
    ej3()
