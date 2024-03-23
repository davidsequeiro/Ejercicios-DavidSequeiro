'''Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.
'''

frase = input('Introduce una frase:')
palabra = frase.split()
print(len(palabra))


total = 0
for letra in palabra:
  total += 1
print(total)
