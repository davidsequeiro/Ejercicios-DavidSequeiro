'''
Ejercicio 2: Calculadora de Propina 
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.
'''

'''
print('SOLUCION 1') #Definir unas variables y asignar precio y sumar sobre la comanda

entrante = 10
principal = 18
segundo = 20
postre = 8
cafe = 2
copa = 15

comanda = [entrante, principal, segundo,postre,cafe,copa]

total = sum(comanda)
propina = 1.15
cuenta = total * propina
print(total)
print(cuenta)


print('SOLUCION 2')   #Definimos un diccionario donde se incluyen los platos y precios

Menu = {
  'entrante': 10,
  'principal': 18,
  'segundo': 20,
  'postre': 8,
  'cafe': 2,
  'copa': 15}
  
Total_tiquet = 0
for plato,precio in Menu.items():
    Total_tiquet += precio
Cuenta = Total_tiquet * 1.15
print(Total_tiquet)
print(Cuenta)



print('SOLUCION 3') # definimos funcion para aplicar a cada comanda sobre las variables de cada plato

def pagar(precios):
  total = sum(comanda)
  return total * 1.15

entrante = 10
principal = 18
segundo = 20
postre = 8
cafe = 2
copa = 15

comanda = [entrante, principal, segundo, postre, cafe, copa]
print(pagar(comanda))

comanda = [entrante, principal]
print(pagar(comanda))


comanda = [entrante, principal, segundo,postre]
print(pagar(comanda))



print('SOLUCION 4') #Definimos un dictionario desde el que calcular el importe segun las distintas comandas

# Definimos funcion para el calculo de cada comanda
def pagar(Menu,comanda):
  total = 0     
  for plato,precio in Menu.items():
      if plato in comanda:
         total += precio
  propina = 1.15
  cuenta = total * propina
  return cuenta
# Definimos un diccionario con los platos y su importe
Menu = {
  'entrante': 10,
  'principal': 18,
  'segundo': 20,
  'postre': 8,
  'cafe': 2,
  'copa': 15
  }

# Introduciomos comandas y obtenemos importe llamando a la funcion definida
comanda = ['entrante','segundo','postre']
print(pagar(Menu,comanda))

comanda = ['entrante','principal','segundo','postre']
print(pagar(Menu,comanda))
'''



print('SOLUCION DINAMICA') # Solucion con ayuda de ChatGPT para transformar en lista los numeros introducidos por el usuario

# Definimos variables de los platos y sus precios
entrante = 10
principal = 18
segundo = 20
postre = 8
cafe = 2
copa = 15

# Definimos variable e importe de propina
propina = 1.15

# Creamos un diccionario con los platos
menu = {
  1 : entrante,
  2 : principal,
  3 : segundo,
  4 : postre,
  5 : cafe,
  6 : copa 
}

# Solicitamos introduzcan numero correspondiente a los platos
comanda = input('elija los numeros de los platos, separadaos por comas : (1-entrante, 2-principal, 3-segundo, 4-postre, 5-cafe, 6-copa)' )

# Transformamos en lista
lista = [int(numero) for numero in comanda.split(',')]

# Definimos la funcion para calcular la suma del importe de los platos elegidos
def pagar(menu,lista):
  total = 0     
  for plato,precio in menu.items():
      if plato in lista:
         total += precio
          
  cuenta = total * propina
  return cuenta

# Resultado
print(f'El total de la cuenta con propina es:  {pagar(menu,lista):.2f} euros')



'''
# Solucion ChatGPT
total = sum(menu[plato] 
            for plato in lista 
            if plato in menu)

print(f'El total de la cuenta con propina es:  {cuenta:.2f} euros')



# Solucion2 adaptando consulta2 chatGpt

def total_a_pagar(Menu, comanda): 
  return sum(Menu[plato] for plato in comanda if plato in Menu) * 1.15
Menu = {
  'entrante': 10,
  'principal': 18,
  'segundo': 20,
  'postre': 8,
  'cafe': 2,
  'copa': 15
  }

comanda = ['entrante','segundo','postre']
print(total_a_pagar(Menu,comanda))

comanda = ['entrante','segundo','postre','copa'] 
print(total_a_pagar(Menu,comanda))
'''