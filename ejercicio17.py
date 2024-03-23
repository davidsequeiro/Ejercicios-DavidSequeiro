'''Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros.
'''
# Solicitamos variable al usuario
milla = int(input('Introduce el numero de kilometros a convertir en millas: '))

# definimos factor de conversion
km = 1.60934

# Definimos formula de calculo
resultado = km * milla

# Resultado
print(milla,'millas son',resultado,'kilometros')
