'''
Ejercicio 4:
Crea una tupla con 5 números. Luego:

    Muestra el número mayor y el menor

    Cuenta cuántas veces aparece un número que el usuario elija
'''

my_tuple = (3, 2, 6, 2, 1)
print("La tupla es:", my_tuple)
veces = int(input("Elige un número a revisar: "))

print(f'El número mayor es: {max(my_tuple)}')
print(f'El número menor es: {min(my_tuple)}')

if veces in my_tuple:
    print(f'El número {veces} se repite {my_tuple.count(veces)} veces.')
else:
    print(f'El número {veces} no está en la tupla.')
