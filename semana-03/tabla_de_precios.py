productos = [
    ("Café molido 250 g", 3.5),
    ("Pan de centeno", 2.10),
    ("Aceite de oliva virgen extra 1 L", 8.90),
    ("Leche entera", 0.95)
]

print(f"{'Producto':<34}{'Precio':>10}")
print("_" * 44)

for producto, precio in productos:
    print(f"{producto:<34}{precio:>10.2f} €")
