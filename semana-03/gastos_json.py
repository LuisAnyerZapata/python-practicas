import json

gastos = [
    {"nombre": "Café", "precio": 2.1, "categoria": "Bebidas"},
    {"nombre": "Menú del día", "precio": 12.80, "categoria": "Comida"},
    {"nombre": "Cine", "precio": 9.00, "categoria": "Ocio"}
]

with open("gastos.json", "w", encoding="utf-8") as archivo:
    json.dump(gastos, archivo, indent=2, ensure_ascii=False)

print(f"Guardados {len(gastos)} gastos en gastos.json")

with open("gastos.json", "r", encoding="utf-8") as archivo:
    gastos_recuperados = json.load(archivo)

print(f"Leídos {len(gastos_recuperados)} gastos del archivo:")
total = 0

for gasto in gastos_recuperados:
    total += gasto["precio"]

    print(
        f"  {gasto['nombre']}: {gasto['precio']:.2f} €"
        f"  ({gasto['categoria']})"
    )

print(f"Total: {total:.2f} €")