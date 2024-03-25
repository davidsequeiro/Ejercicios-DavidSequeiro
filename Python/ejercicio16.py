'''
Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.
'''
'''
def pares(num):
    if num % 2 == 0:
        return False
    else:
        return True
'''

# Solicitamos al usuario que ingrese los numeros a su elecion
numero_selec = input('Ingresa los valores separados por coma: ')

# Definimos una lista con los numeros elegidos por el usuario
lista = [int(numero) for numero in numero_selec.split(',')]  

# Definimos la funcion para encontrar los numero pares, mostrarlos y contarlos
def pares(numero):
    contar = 0
    for numero in lista:
        if numero % 2 == 0: 
          contar += 1
          print(numero, 'es par')
    print('hay un total de ',contar,'numeros pares')
print(pares(lista))
