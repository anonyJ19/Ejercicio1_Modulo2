"""
Ejercicio 1 — Sistema de precios de entrada
Descripción:
- Calcula el precio de una entrada según la edad y si es estudiante.
Reglas:
- Menor de 12 años: 10000
- Entre 12 y 17 años: 15000
- 18 o más: 20000
- Estudiantes tienen 10% de descuento sobre el precio según edad
"""

def calcular_precio_entrada(edad: int, es_estudiante: bool) -> int:
    """Devuelve el precio final según edad y si es estudiante."""
    if edad < 12:
        base = 10000
    elif edad <= 17:
        base = 15000
    else:
        base = 20000

    if es_estudiante:
        return int(base * 0.9)  # descuento 10%
    return base


def ej1() -> None:
    """Demo sencilla: pide edad y si es estudiante, muestra el precio."""
    try:
        edad = int(input("Ingresa tu edad: "))
    except ValueError:
        print("Edad inválida. Debes ingresar un número.")
        return

    resp = input("¿Eres estudiante? (si/no): ").strip().lower()
    es_est = resp == "si"

    precio = calcular_precio_entrada(edad, es_est)
    print(f"El precio de la entrada es: ${precio}")


if __name__ == "__main__":
    ej1()
