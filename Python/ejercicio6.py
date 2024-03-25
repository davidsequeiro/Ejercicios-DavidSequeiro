'''Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''
# Solicitamos palabra al usuario
palabra = str(input('¿Cual es tu palabra?: '))

# Definimos funcion para saber si es igual al derecho que al reves y devolvemos resultado
def es_palindromo(palabra):
  palabra = palabra.lower()
  return palabra == palabra[::-1]
if es_palindromo(palabra) is True:
  print('es palindromo')
else:
  print('No es palindromo')


  