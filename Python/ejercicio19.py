'''
Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.
'''

'''
Cualquier año divisible por 4 es bisiesto
'''

# Solicitamos año al usuario para definir variable
año = int(input('Introduzca año para saber si es bisiesto: '))

# Aplicamos la formula
if año % 4 == 0:
  print('El año ',año,' es bisiesto')
else:
  print('El año ',año,' no es bisiesto')