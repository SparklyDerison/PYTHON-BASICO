'''
Estás creando un sistema básico para una tienda virtual.

    Pide al usuario su nombre completo y muestra un saludo con su nombre en mayúsculas

    Muestra una lista de productos disponibles con sus precios (usa un diccionario)

    Pide al usuario que elija 3 productos por su nombre

    Guarda esos 3 productos en una tupla

    Muestra el total a pagar

    Muestra las letras únicas en los nombres de los productos elegidos (usa un set)

    Finalmente, muestra un resumen de la compra
'''

nombre_usuario = input("¿Cómo te llamas?: ")
print(f'Hola {nombre_usuario.upper()}. Bienvenido a mi tienda, ¡Pide lo que quieras!')

productos = {
    "Galletas": 25,
    "Leche": 32,
    "Salsa": 45,
    "Pollo": 50,
    "Mayonesa": 39
}
for producto, precio in productos.items():
    print(f'{producto}: ${precio}')

print("Elige tres productos por su nombre:")

eleccion_usuario = list()
valores = []
for i in range(3):
    compra = input().lower().capitalize()
    if compra in productos:
        eleccion_usuario.append(compra)
        valores.append(productos[compra])
    
    else:
        print("Ese producto no está en la lista.")
        exit()

eleccion_usuario_tupla = tuple(eleccion_usuario)
print("La tupla de tus productos es:", eleccion_usuario_tupla)
total_pagar = sum(valores)

set1 = set(eleccion_usuario_tupla[0])
set2 = set(eleccion_usuario_tupla[1])
set3 = set(eleccion_usuario_tupla[2])

print(f'Las palabras únicas de la palabra {eleccion_usuario_tupla[0]} {set1}')
print(f'Las palabras únicas de la palabra {eleccion_usuario_tupla[1]} {set2}')
print(f'Las palabras únicas de la palabra {eleccion_usuario_tupla[2]} {set3}')

print("El total a pagar de toda tu lista es de: $" + str(total_pagar))
