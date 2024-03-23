'''Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.
'''
# Solicito frase al usuario
frase = input('Introduce una frase:')
# Transformo en lista con los valores introducidos 
palabra = frase.split()
# Solucion
print('el numero de palabras es:',len(palabra))

# solucion con bucle
total = 0
for letra in palabra:
  total += 1
print('el numero de palabras es:',total)
