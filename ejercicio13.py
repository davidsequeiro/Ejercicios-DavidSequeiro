'''
Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no.

Para determinar si un número es primo, puedes utilizar el siguiente método matemático:
División por tentativa: Divide el número ( n ) entre cada número primo desde el 2 hasta la raíz cuadrada de ( n ). Si ( n ) es divisible por cualquiera de estos números primos, entonces no es primo1.'''


# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número para verificar si es primo: "))

# Definimos rango de valores para operar
a = range(2, int(numero ** 0.5) + 1) #raiz cuadrada

# Aplicamos formula al numero seleccionado y el rango obtenido
for i in a:
  if numero % i == 0:
    print('El numero',numero,'no es primo')
  else:
    print('El numero',numero,'es primo')


'''
# Solucion ChatGPT
def primo(num): #define funcion con variable generica IMPORTANTE
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1): #rango desde el 2 hasta la raíz cuadrada de num 
        if num % i == 0: # divide num entre cada valor del rango para i y debe dar 0
            return False
    return True

# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número para verificar si es primo: "))

# Verificar si el número es primo
if primo(numero):#aplica funcion sobre variable numero no num IMPORTANTE
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")
    '''