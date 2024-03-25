'''
Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo.
'''
# Solicitamos variables al usuario
longitud = int(input('Introduzca longitud en centimetros: '))
anchura = int(input('Introduzca anchura en centimetros: '))

# Definimos formula
area = longitud * anchura

# Resultado
print('El area es: ', area, 'centimetros cuadrados')
