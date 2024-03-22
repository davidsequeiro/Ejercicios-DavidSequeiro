'''
Ejercicio 1: Conversor de Temperatura 
Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.

Formula de calculo
a = Temperatura en grados Celsius
b = a*(9/5)+32  # Formula de conversion Celsius a Farenheit
'''

# Soilicitamos valor de a = grados celsius
a = float(input('Ingresa un valor para temperatura en grados Celsius: ')) 

# creamos funcion para convertir mediante formula
def convertir(a): 
  b = a*(9/5)+32  # Formula de conversion Celsius a Farenheit
  return b

#Respuesta de solucion
print(a,'grados Celsius es igual a ',convertir(a), 'grados Farenheit') 




