### Tuples ###
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (19, 1.74, "Juan", "Chacón", "Juan")
my_other_tuple = (30, 25, 19)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Juan"))
print(my_tuple.index("Chacón"))
print(my_tuple.index("Juan"))

#my_tuple[1] = 1.80 Las tuplas son constantes, no se pueden modificar.

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Sparkly"
my_tuple.insert(1, "Rojo")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

#del my_tuple name 'my_tuple' is not defined
print(my_tuple)