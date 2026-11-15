lineas = []

for i in range(3):
    lineas.append(input(f"{i + 1}: "))

with open("diario.txt", "a", encoding="utf-8") as archivo:
    for linea in lineas:
        archivo.write(linea + "\n")

with open("diario.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

for numero, linea in enumerate(lineas, start=1):
    print(f"{numero}: {linea.strip()}")