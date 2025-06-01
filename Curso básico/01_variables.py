# Variables

my_string_variable = 'My string Variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_string_variable = str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable))

my_bool_variable = False
print(my_bool_variable)
# Variables en una sola linea ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Juan", "Chacón", "Sparkly", 19
print("Me llamo:", name, surname, ". Tengo:", age, ". Y me dicen:", alias)

# Inputs

name = input("¿Cuál es tu nombre?: ")
age = input("¿Cuál es tu edad?: ")
print(name)
print(age)

# Cambiamos su tipo
name = 35
age = "Brais"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = 32
address = True
address = 1.2
print(type(address))