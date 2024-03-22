'''Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.
'''

# Solictamos el numero de minutos
minutos = int(input('Introduce el numero de minutos que quieres convertir a horas y minutos: '))

# Definimos el numero de minutos que contiene una hora
hora = 60

# Definimos formulas para calcular horas enteras
total_horas = int(minutos / hora)
# Definmos formula para calcular el numero de minutos restantes
total_minutos = minutos - (total_horas * hora)

# Resultado
print(minutos,'minutos son',total_horas,'horas y',total_minutos,'minutos')
