# Registro de Gym

limit = True

def kcal_hombres(edad_m, peso_m, altura_m):
    return (10 * peso_m) + (6.25 * altura_m) - (5 * edad_m) + 5

def kcal_mujeres(edad_f, peso_f, altura_f):
    return (10 * peso_f) + (6.25 * altura_f) - (5 * edad_f) - 161

# Lista Masculina

list_nombres_m = []
list_cedula_m = []
list_edad_m = []
list_peso_m = []
list_altura_m = []

#Lista Femenina

list_nombres_f = []
list_cedula_f = []
list_edad_f = []
list_peso_f = []
list_altura_f = []

for i in range(1, 3):
    sexo = input("Eres 'Hombre' o 'Mujer': ").lower()
    if sexo == "hombre":
        nombre = input("¿Cuál es tu Nombre?:\n").title()
        list_nombres_m.append(nombre)
        cedula = int(input("Ingresa tu C.C:\n"))
        list_cedula_m.append(cedula)
        edad = int(input("¿Cuántos años tienes?:\n"))
        list_edad_m.append(edad)
        peso = float(input("Ingresa tu Peso:\n"))
        list_peso_m.append(peso)
        altura = int(input("Ingresa tu Altura:\n"))
        list_altura_m.append(altura)
        print(f"¡¡Bienvenido {nombre}!! Has sido registrado exitosamente con tu cédula: {cedula}.")
    elif sexo == "mujer":
        nombre = input("¿Cuál es tu Nombre?:\n").title()
        list_nombres_f.append(nombre)
        cedula = int(input("Ingresa tu C.C:\n"))
        list_cedula_f.append(cedula)
        edad = int(input("¿Cuántos años tienes?:\n"))
        list_edad_f.append(edad)
        peso = float(input("Ingresa tu Peso:\n"))
        list_peso_f.append(peso)
        altura = int(input("Ingresa tu Altura:\n"))
        list_altura_f.append(altura)
        print(f"¡¡Bienvenido {nombre}!! Has sido registrado exitosamente con tu cédula: {cedula}.")
    else:
        print("Sexo no incorrecto, vuelve a intentarlo")

print("Bienvenido maestro, escribe le nombre de cualquier estudiante de la lista:")

while limit:
    list_all = list_nombres_m + list_nombres_f
    
    for i in range(len(list_all)):
        print("*", list_all[i - 1])

    busqueda = input("Nombre: ").title()

    if busqueda in list_nombres_m:
        indice_nom = list_nombres_m.index(busqueda)
        indice_edad = list_edad_m[indice_nom]
        indice_peso = list_peso_m[indice_nom]
        indice_altura = list_altura_m[indice_nom]

        print(f"Accediste al usuario {busqueda}, identificado con {list_cedula_m[indice_nom]}\nSu TMB es: {kcal_hombres(indice_edad, indice_peso,indice_altura)}")

    elif busqueda in list_nombres_f:
        indice_nom = list_nombres_f.index(busqueda)
        indice_edad = list_edad_f[indice_nom]
        indice_peso = list_peso_f[indice_nom]
        indice_altura = list_altura_f[indice_nom]

        print(f"Accediste al usuario {busqueda}, identificado con {list_cedula_f[indice_nom]}\nSu TMB es: {kcal_hombres(indice_edad, indice_peso,indice_altura)}")

    else:
        print("La persona no se encuentra en la lista")
    close_limit = input("Presiona C para cerrar o P para volver a la lista: ").upper()
    if close_limit == "C":
        limit = False