'''
Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
'''

dia= int(input('ingreasa un numero del 1 al 7:'))-1

semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Viernes', 'Sabado', 'Domingo']

if dia > 7:
  print('Numero no valido')
  
print(semana[dia])

print(('El '), dia+1, ('dia de la semana es: '), semana[dia])

