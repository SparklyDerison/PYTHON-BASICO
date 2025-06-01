### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La condición continúa")

while my_condition < 20:
    my_condition += 2
    if  my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La condición continúa")

# For

my_list = [16, 13, 20, 20, 17, 22, 34]

for element in my_list:
    print(element)

my_tuple = (19, 1.74, "Juan", "Chacón", "Juan")

for element in my_tuple:
    print(element)

my_set = {"Python", "Java", "MySQL"}

for element in my_set:
    print(element)

my_dict = {"Nombre":"Juan", "Apellido":"Chacón", "Edad": 20, 1:"Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        continue # Continúa devolviendose en el for
    print("Se ejecuta")
else:
    print("El bucle for para mi diccionario ha finalizado")

print("La condición continúa")
