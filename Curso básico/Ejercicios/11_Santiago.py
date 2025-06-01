### Problema ###

from datetime import datetime

# nombre, fecha de ingreso, fecha de cuando trabaja, cedula, habilidades

posibles_empleados = []
identificaciones = []
fechas_ingreso = []
fechas_inicio = []
habilidades = []

for i in range(1):
    nombre_emple = input("Ingresa tu nombre: ")
    posibles_empleados.append(nombre_emple)

    identificacion = int(input("Ingresa tu C.C: "))
    identificaciones.append(identificacion)

    fecha_ingreso = str(datetime.now())
    fechas_ingreso.append(fecha_ingreso)

    fecha_inicio = str(input("Ingresa la fecha en la que vas a iniciar a trabajar (AA/MM/DD): "))
    fechas_inicio.append(fecha_inicio)

    habilidad = input("¿En qué te desempeñas?: ")
    habilidades.append(habilidad)

print(posibles_empleados)
print(identificaciones)
print(fechas_ingreso)
print(fechas_inicio)
print(habilidades)


