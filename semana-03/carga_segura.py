import json

gastos = []

try:
    with open("gastos.json", "r", encoding="utf-8") as archivo:
        gastos = json.load(archivo)
    print(f"Cargados {len(gastos)} gastos del archivo.")

except FileNotFoundError:
    print("gastos.json no existe; empezamos con la lista vacía.")