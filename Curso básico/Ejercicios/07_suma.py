tabla_multi = int(input("Ingresa un número para crear una tabla: "))

for i in range(11):
    respuesta = tabla_multi * i
    print(f'{tabla_multi} x {i} = {respuesta}')