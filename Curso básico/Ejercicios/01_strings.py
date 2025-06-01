'''
Ejercicio 2:
Pide al usuario una frase e imprime:

    La frase en mayúsculas y en minúsculas

    Cuántas letras tiene (sin contar espacios)

    Cuántas veces aparece una vocal que el usuario elija
'''
frase = input("Ingresa una frase: ")
contar_vocal = input("¿Qué vocal quieres contar?: ")

# Mostrar frase en mayúsculas y minúsculas
print("Mayúsculas:", frase.upper())
print("Minúsculas:", frase.lower())

# Contar letras sin espacios
cantidad_letras = len(frase.replace(" ", ""))
print("Cantidad de letras (sin espacios):", cantidad_letras)

# Contar cuántas veces aparece la vocal (sin importar mayúscula/minúscula)
veces = frase.lower().count(contar_vocal.lower())
print(f"La vocal '{contar_vocal}' aparece {veces} veces.")
