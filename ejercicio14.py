'''Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.
'''

# Definimos el descuento
dto = 0.20
descuento = 1 - dto

# Solicitamos el importe del articulo
precio = int(input('Introduzac el importe de su articulo: '))

# Calculamos el imprte final despues de aplicar el descuento
Total = precio * descuento

# Respuesta
print(f'el importe de su articulo despues del descuento es: {Total:.2f}')