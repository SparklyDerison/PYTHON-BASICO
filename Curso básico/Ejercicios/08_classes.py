'''
🧩 Ejercicio 1: Crear una clase simple

Crea una clase llamada Perro que tenga los siguientes atributos:

    nombre

    raza

Y un método que diga "Guau, soy {nombre}".
'''

class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"Guau, soy {self.nombre}")
perrazo = Perro("Rocko", "Criollo")
perrazo.ladrar()
#-----------------------------------------------------------------------------------------
'''
🧩 Ejercicio 2: Clase con método que realiza una operación

Crea una clase llamada Rectangulo con:

    atributos: ancho y alto

    un método que calcule y devuelva el área del rectángulo
'''

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def area(self):
        return f'El area del rectángulo es {self.ancho * self.alto}'

area_rectangulo = Rectangulo(5, 4)
print(area_rectangulo.area())
#-----------------------------------------------------------------------------------------
'''
🧩 Ejercicio 3: Contador de instancias

Objetivo:
Crear una clase Usuario que:

    Tenga un atributo de clase llamado contador que cuente cuántos usuarios se han creado.

    Cada vez que se cree un nuevo objeto Usuario, el contador aumente en 1.

(((((NO LO LOGRÉ))))) /// Chat-GPT Ganó
'''

class Usuario:
    contador = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Usuario.contador += 1

u1 = Usuario("María")
u2 = Usuario("Karla")
u3 = Usuario("Juan")

print(f'Entraron {Usuario.contador} usuarios.')
#-----------------------------------------------------------------------------------------