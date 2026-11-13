nombre_input = input("Introduce tu nombre completo: ")
nombre = nombre_input.strip().upper()

# Recortar si supera los 17 caracteres para que no rompa la caja
nombre_recortado = nombre[:17]
caracteres = len(nombre)

# Extraer iniciales recorriendo las palabras
iniciales = ""
for palabra in nombre.split():
    iniciales += palabra[0]

ANCHO_CAJA = 32

borde = "+" + "-" * ANCHO_CAJA + "+"

print(borde)
# Título alineado a la izquierda dentro de la caja
print(f"| {'CREDENCIALES DE VISITANTE':<{ANCHO_CAJA - 1}}|")
print(borde)

print(f"| Nombre:      {nombre_recortado:<17} |")
print(f"| Iniciales:   {iniciales:<17} |")
print(f"| Caracteres:  {caracteres:<17} |")
print(borde)