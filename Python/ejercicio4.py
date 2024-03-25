'''Ejercicio 4: Contador de Vocales 
Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.
'''

# establecemos un contador y solicitamos la palabra al usuario y definimos los valores a buscar
contar = 0
palabra = input('escribe una palabra: ')
vocales = 'a,e,i,o,u,A,E,I,O,U'

# Establecemos condicion y devolvemos resultado
for letra in palabra:
  if letra in vocales:
    contar += 1
    print(letra)
print('El total de vocales es: ' ,contar)
    