'''
Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.
'''

año_actual = int(input('Introduce año actual: '))
año_nacimiento = int(input('Introduce año de nacimiento: '))

edad= año_actual - año_nacimiento

print(edad)

'''
from datetime import datetime
año_ahora = datetime.now().year
'''