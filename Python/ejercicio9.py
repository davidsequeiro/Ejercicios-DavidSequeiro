'''
Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.
'''
# Solicitamos al usuario el importe en dolares
valor = float(input('Introduce el valor en dolares: '))

# Establecemos el cambio de moneda
cambio = 0.85

# Definimos la formula y devolvemos resultado
def conversor():
  return valor * cambio
print(conversor())