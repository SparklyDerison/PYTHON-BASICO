'''
Ejercicio 1:
Escribe un programa que pida al usuario dos números y muestre:

    La suma

    La resta

    El producto

    La división

    El resto de la división
'''

num1 = int(input('Ingresa el primer valor a operar: '))
num2 = int(input('Ingresa el segundo valor a operar: '))

suma = num1 + num2
rest = num1 - num2
mult = num1 * num2

print(f'El valor de la suma es: {suma}')
print(f'El valor de la resta es: {rest}')
print(f'El valor de la multiplicación es: {mult}')

if num2 != 0:
    div = num1 / num2
    mod_div = num1 % num2
    print(f'El valor de la división es: {div:.2f}')
    print(f'El resto de la división es: {mod_div}')
else:
    print("No se puede dividir entre cero")