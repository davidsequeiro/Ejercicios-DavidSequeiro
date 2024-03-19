'''
Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.
'''

valor = float(input('Introduce el valor en dolares: '))

def conversor():
  return valor * 0.85
print(conversor())