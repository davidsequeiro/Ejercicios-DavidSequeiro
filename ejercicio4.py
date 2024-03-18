'''Ejercicio 4: Contador de Vocales 
Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.
'''
contar = 0
palabra = input('escribe una palabra: ')
vocales = 'a,e,i,o,u,A,E,I,O,U'
for letra in palabra:
  if letra in vocales:
    contar += 1
    print(letra)
print('El total de letras es: ' ,contar)
    