"""
Ejercicio 5 — Par o Impar y múltiplo de 5
Descripción:
- El usuario ingresa un número.
- El programa dice si es par o impar.
- Además, si es múltiplo de 5.
"""

def par_o_impar(n: int) -> str:
    """Devuelve 'Par' o 'Impar' según el número."""
    return "Par" if n % 2 == 0 else "Impar"


def ej5() -> None:
    dato = input("Ingresa un número: ").strip()
    if not dato.isdigit():
        print("Número inválido.")
        return

    n = int(dato)
    tipo = par_o_impar(n)
    print(f"El número {n} es {tipo}.")

    if n % 5 == 0:
        print("Además, es múltiplo de 5.")


if __name__ == "__main__":
    ej5()
