### Functions ###

def my_function():
    print("Esta es una función")

my_function()
my_function()
my_function()

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(543242, 712312)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(10, 5) # None
print(my_result)

my_result = sum_two_values_with_return(10, 5) # Retorna el valor de 10 + 5
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname = "Chacón", name = "Juan") # Se puede reasignar el orden

def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname}  {alias}")

print_name_with_default("Juan", "Chacón")
print_name_with_default("Juan", "Chacón", "Sparkly")

def print_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_texts("Hola", "Python", "Sparkly")
print_texts("Hola")
