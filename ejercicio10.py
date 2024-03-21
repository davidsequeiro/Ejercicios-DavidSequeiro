'''
Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
'''

dia= int(input('ingreasa un numero del 1 al 7:'))

semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Viernes', 'Sabado', 'Domingo']

if dia > 7:
  print('Numero no valido')
 
if dia < 7:  
  print(semana[dia-1])

  print(('El '), dia, ('dia de la semana es: '), semana[dia-1])

