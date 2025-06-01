'''
Crea un diccionario que contenga 3 productos y su precio. Luego:

    Muestra todos los productos con su precio

    Permite al usuario ingresar el nombre de un producto y muestra su precio

    Si el producto no está en el diccionario, muestra un mensaje indicando que no se encontró
'''

productos = {
    "Mouse": 40000,
    "Maletin": 70000,
    "Gafas": 360000
}
print("Tabla de productos:")
for producto, precio in productos.items():
    print(f'{producto}: ${precio}')

peticion = input("Ingresa el nombre de un producto: ").lower()
peticion = peticion.capitalize()

if peticion in productos:
    print(f'El valor de {peticion} es: ${productos[peticion]}')
else:
    print("Producto no encontrado, lo sentimos.")