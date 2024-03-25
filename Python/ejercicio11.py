'''
Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.
'''
# Solictamos año actual y año nacimiento
año_actual = int(input('Introduce año actual: '))
año_nacimiento = int(input('Introduce año de nacimiento: '))

# Aplicamos calculo
edad= año_actual - año_nacimiento

# Resultado
print(edad)

'''
# Obtener fecha hoy y mostrar formato año (consulta ChatGPT
from datetime import datetime
año_ahora = datetime.now().year
'''