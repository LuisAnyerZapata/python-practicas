nombre = input("Introduce un nombre completo: ")
print(f"Original: '{nombre}'")

nombre_limpio = nombre.strip()
print(f"Sin espacios extra: '{nombre_limpio}'")

print(f"En mayúsculas: {nombre_limpio.upper()}")
print(f"En minúsculas: {nombre_limpio.lower()}")

print(f"Longitud original: {len(nombre)}")
print(f"Longitud limpia: {len(nombre_limpio)}") 