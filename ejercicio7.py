'''Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.
'''


a = int(input('Intruduzca valor 1: '))
b = int(input('Intruduzca valor 2: '))

sumar = a + b
restar = a - b
multiplicar = a * b
dividir = a / b

operaciones = {
    1: sumar,
    2: restar,
    3: multiplicar,
    4: dividir
    }


print('1.- sumar, 2.-restar, 3.-multiplicar, 4.-dividir')
operacion = int(input('Introduzca operacion: '))


print(operaciones[operacion])


#def operar(a,b):
  #for operacion in 
  
'''

operaciones = [sumar, restar, multiplicar, dividir]


operaciones = {
    1: 'sumar',
    2: 'restar',
    3: 'multiplicar',
    4: 'dividir'
    }
'''