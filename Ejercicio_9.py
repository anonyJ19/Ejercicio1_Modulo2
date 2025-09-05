"""
Ejercicio 9 — Precios con IVA
Descripción:
- Se recibe una lista de productos con su precio.
- Se calcula el precio con IVA (19%).
- Se devuelve un diccionario {nombre: precio_con_iva}.
"""

def precios_con_iva(productos: list[dict[str, float]], iva: float = 0.19) -> dict[str, float]:
    """Devuelve {nombre: precio_con_iva} redondeado a 2 decimales."""
    return {p["nombre"]: round(p["precio"] * (1 + iva), 2) for p in productos}


def ej9() -> None:
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Zapatos", "precio": 120000},
    ]
    resultado = precios_con_iva(productos)
    for nombre, precio in resultado.items():
        print(f"{nombre}: ${precio}")


if __name__ == "__main__":
    ej9()
