### Operadores Aritméticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 2)
print(10 // 2) # Flor división, cociente sin decimales
print(2 ** 3) # Potencia
print(2 ** 3 + 3 - 7 / 1 // 4) # Combinar

print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5))
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

print("-----")

print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa") # Ordenación Alfabética por ASCII
print(len("aaaa") <= len("abaa")) # Cuenta carácteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

print("-----")

### Operadores Lógicos ###

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4))
