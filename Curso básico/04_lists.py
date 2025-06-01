### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [16, 13, 20, 20, 17, 22, 34]

print(my_list)
print(len(my_list))

my_other_list = [19, 1.74, "Juan", "Chacón"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(20))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3],
print(age)

print(my_list + my_other_list)

my_other_list.append("Sparkly")
print(my_other_list)

my_other_list.insert(1, "Azul")
print(my_other_list)

my_other_list[1] = "Rojo"
print(my_other_list)

my_other_list.remove("Rojo")
print(my_other_list)

my_list.remove(20) #Elimina un elemento que conozco, en este caso el 20
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2] #Elimina el elemento sin retornar. Elimina un elemento por índice.
print(my_list)

my_new_list = my_list.copy() #Copi la lista a una nueva variable.

my_list.clear() #Limpia la lista.
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort() #Ordenar una lista. Por defecto es de menor a mayor.
print(my_new_list)

print(my_new_list[1:2])

my_list = "Hola Python" # Tipado dinámico
print(my_list)
print(type(my_list))