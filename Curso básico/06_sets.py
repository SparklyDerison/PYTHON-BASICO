### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario.

my_other_set = {"Juan", "Chacón", 19}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Sparkly")

print(my_other_set) #Los sets no son una estructura ordenada

my_other_set.add("Sparkly")

print(my_other_set) #Un set no admite repetidos.

print("Juan" in my_other_set)
print("José" in my_other_set)

my_other_set.remove("Juan")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set

#print(my_other_set) name 'my_other_set' is not defined.

my_set = {"Juan", "Chacón", 19}
my_list = list(my_set)

print(my_list)
print(my_list[0])

my_other_set = {"Python", "Java", "MySQL"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Malbolge", "C#"}))

print(my_new_set.difference(my_set))