'''
Pide al usuario que escriba 2 frases. Luego:

    Muestra las letras únicas de cada frase

    Muestra qué letras tienen en común

    Muestra las letras que aparecen en la primera frase pero no en la segunda
'''

frase1 = input("Escribe una frase: ")
frase2 = input("Escribe otra frase: ")

print("Primera Frase: ", frase1)
print("Segunda Frase: ", frase2)

set1 = set(frase1.replace(" ", ""))
set2 = set(frase2.replace(" ", ""))
print("Letras únicas de la primera frase: ", set1)
print("Letras únicas de la segunda frase: ", set2)

letras_comun = set1 & set2
print("Letras en común de ambas frases: ", letras_comun)

print("Estas son las letras que aparecen en la primera frase: ", set1 - set2)