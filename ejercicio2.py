'''
Ejercicio 2: Calculadora de Propina 
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.
'''

'''
print('SOLUCION 1') #Definir unas variables y asignar precio y sumar sobre la comanda

entrante = 10
principal = 15
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
  'principal': 15,
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



print('SOLUCION 3') # definimos funcion para aplicarf a cada comanda y las variables de cada plato

def pagar(precios):
  total = sum(comanda)
  return total * 1.15

entrante = 10
principal = 15
segundo = 20
postre = 8
cafe = 2
copa = 15

comanda = [entrante, principal, segundo,postre,cafe,copa]
print(pagar(comanda))

comanda = [entrante, principal]
print(pagar(comanda))

comanda = [entrante, principal, segundo,postre]
print(pagar(comanda))
'''


print('SOLUCION 4')
def pagar():
  total = 0
  for plato,precio in Menu.items():
    total += (precio)
  propina = 1.15
  cuenta = total * propina
  return cuenta

Menu = {
  'entrante': 10,
  'principal': 15,
  'segundo': 20,
  'postre': 8,
  'cafe': 2,
  'copa': 15
  }





#Menu = ['entrante','segundo','postre']

print(pagar)

'''
print(comanda)

total = 0
for plato,precio in Menu.items():
  total += (precio)
print(total)
propina = 1.15
cuenta = total * propina
print(cuenta)
'''




'''
print('FORMA OPTIMA')

def total_a_pagar(Menu, comanda): 
  return sum(Menu[Key] for Key in comanda if Key in Menu)

Menu = {
  'entrante': 10,
  'principal': 15,
  'segundo': 20,
  'postre': 8,
  'cafe': 2,
  'copa': 15
  }

comanda = ['entrante','segundo','postre']

cuenta = total_a_pagar(Menu,comanda) * 1.15
print(cuenta)  
'''



  
  




