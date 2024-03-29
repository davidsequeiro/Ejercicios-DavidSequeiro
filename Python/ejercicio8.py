'''
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''

# Solicitamos las variables al usuario
altura = float(input('¿Cual es tu altura en metros?: '))
peso = float(input('¿Cual es tu peso en kilogramos?: '))

# Definimos la formula de calculo
def imc(peso,altura):
  imc = peso / (altura **2) 
  return imc

# Devolvemos resultado con 2 decimales
print(f'Tu indice IMC es: {imc(peso,altura):.2f}')

