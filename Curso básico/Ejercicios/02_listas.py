'''
Ejercicio 3:
Crea una lista con al menos 5 nombres. Luego:

    Agrega un nombre nuevo

    Ordena la lista alfabéticamente

    Muestra los 3 primeros nombres

    Elimina el último nombre
'''
nombres = ["Juan", "Diego", "Miguel", "María", "Rosa"]
print("Aquí tienes la lista original", nombres)

nombres.append("Josefa")
print("Le agregamos un nombre", nombres)

orden_alfabetico = nombres.copy()

orden_alfabetico.sort()
print("Ordenamos alfabéticamente: ", orden_alfabetico)
print('Aquí tienes los primero tres nombres en orden alfabético: ', orden_alfabetico[:3])

del orden_alfabetico[-1]
print("La lista sin el último nombre: ", orden_alfabetico)