'''
Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el
usuario.
'''

# Solicitamos al usuario que ingrese los numeros a su elecion
numero_selec = input('Ingresa los valores separados por coma: ')

# Definimos una lista con los numeros elegidos por el usuario
lista = [int(numero) for numero in numero_selec.split(',')]  

# Sumamos los valores
suma = sum(lista)

# Resultado
print ('la suma de los valores introducidos es:',suma)
   