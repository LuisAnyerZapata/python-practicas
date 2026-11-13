frase = input("Introduce una frase: ")
palabra = input("Introduce la palabra a buscar: ")

# Versiones en minúsculas solo para buscar y contar sin errores de mayúsculas
frase_lower = frase.lower()
palabra_lower = palabra.lower()

aparece = palabra_lower in frase_lower
veces = frase_lower.count(palabra_lower)

print(f"¿Aparece '{palabra}'? {aparece}")
print(f"Veces que aparece: {veces}")

sustituta = input("Introduce la palabra sustituta: ")
frase_modificada = frase.replace(palabra, sustituta)

print(f"Frase modificada: {frase_modificada}")

# Experimento: si busco "Café" con mayúscula, in y count SÍ lo encuentran,
# porque estoy comparando contra las versiones en minúsculas (.lower()).
# En cambio replace("Café", ...) NO cambia nada: replace() distingue
# mayúsculas y minúsculas, así que solo sustituye coincidencias exactas.