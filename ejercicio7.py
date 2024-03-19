'''Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.
'''
a = 0
b = 0

suma = a + b
resta = a - b
multiplicar = a * b
dividir = a / b

operacion = [suma, resta , multiplicar, dividir]

def operar(a,b):
  for operacion in 