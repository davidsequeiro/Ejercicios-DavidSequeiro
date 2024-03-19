'''
Ejercicio 1: Conversor de Temperatura 
Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.

Formula de calculo
a = 32  # Temperatura en grados Celsius
b = a*(9/5)+32  # Formula de conversion Celsius a Farenheit
print(a,'Celsius, es igual a ',b,'Farenheit')  #Respuesta de solucion
'''

def convertir(a):
  b = a*(9/5)+32  # Formula de conversion Celsius a Farenheit
  print(a)
  print(b)
  print(a,'Celsius es igual a ',b,'Farenheit')  #Respuesta de solucion

a = 25
print(convertir(a))

a = 32
print(convertir(a))

