'''Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.
'''

# Definimos variables para los numeros
a = int(input('Intruduzca valor 1: '))
b = int(input('Intruduzca valor 2: '))

# Definimos variables para las operaciones
sumar = a + b
restar = a - b
multiplicar = a * b
dividir = a / b

# Creamos un diccionario para asignar claves numericas a las variables de operaciones
operaciones = {
    1: sumar,
    2: restar,
    3: multiplicar,
    4: dividir
    }
# Definimos un diccionario para asignar nombres a las aperaciones
texto = {
    1: 'sumar',
    2: 'restar',
    3: 'multiplicar',
    4: 'dividir'
    }

# Solicitamos las variables numericas y la operacion
print('1.- sumar, 2.-restar, 3.-multiplicar, 4.-dividir')
operacion = int(input('Introduzca operacion: '))

# Resultado
#print(operaciones[operacion])

print('el resultado de ', texto[operacion], a, ' y ', b, ' es ',operaciones[operacion])


