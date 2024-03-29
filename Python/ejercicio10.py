'''
Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
'''
# Solicitamos valor de la variable dia al usuario
dia= int(input('ingresa un numero del 1 al 7:'))

# Creamos lista de los dias de la semana
semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

# Acotamos los dias de la semana en numero
if dia > 7:
  print('Numero no valido')
# Solicitamos la posicion de la variable dia en la lista semana
if dia <= 7:  
  print(semana[dia-1])

# Resultado
  print('El ', dia, 'dia de la semana es: ', semana[dia-1])

