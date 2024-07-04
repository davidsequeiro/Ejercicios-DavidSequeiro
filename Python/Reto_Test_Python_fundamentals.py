'''
EJERCICIO 1. Función contar_caracteres :
Descripción del ejercicio:
Crea una función que cuente el número de caracteres en una cadena de texto dada.
'''

#solicito al usuario que introduzca una frase
cadena_texto = input(f'Introduzca una frase:\n')
#definimos la funcion
def contar_caracteres(cadena_texto):
  #creamos un diccionario vacio para almacenar los pares letra y el numero de veces repetida
  caracteres = {}
  #establezco condicion:
  for letra in cadena_texto:
    #para cada letra de la frase, si no es un espacio,
    if letra != " ":
      #añade al dicionario la letra y suma 1 al valor
      caracteres[letra] = caracteres.get(letra,0) + 1
  return(caracteres)  
  
#llamo a la funcion    
contar_caracteres(cadena_texto)
print(contar_caracteres(cadena_texto))


'''
EJERCICIO 2. Función calcular_promedio :
Descripción del ejercicio:
Crea una función que calcule el promedio de una lista de números.
'''

#solicito al usuario que introudzca unos numeros separados por comas
entrada = input('introduzca numeros separados por comas:\n')
#transformo las entradas del usuario a formato integer y lo almaceno en una lista 
lista_numeros = [int(num) for num in entrada.split(",")]
#defino la funcion
def calcular_promedio(lista):
  #calculo el numero de elmentos de la lista y la suma de todos los elementos
  numeros = len(lista_numeros)
  total = sum(lista_numeros)
  #calculo el promedio
  promedio = float(total/numeros)
  return promedio

#llamo a la funcion
calcular_promedio(lista_numeros)
print(calcular_promedio(lista_numeros))
print(f'el promedio de {lista_numeros} es: {calcular_promedio(lista_numeros):.2f}')


'''
EJERCICIO 3. Función encontrar_duplicado :
Descripción del ejercicio:
Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
'''

'''caso de uso:
1,2,3,4,5,6,7,8,9,5,4,6 => outpt =  El elemento que se repite primero es 5 y se repite 2 veces.
                                    El primer elemento repetido es 4 y se repite 2 veces. 
(El 5 es el valor que se repite antes, sin embargo en el dicc el primer valor en repetirse seria el 4.)'''


#DOS SOLUCIONES DISTINTAS (DESCOMENTAR AMBAS EJECUCION SIMULTANEA)
#OPCION 1
#buscar el valor que se repite primero segun el orden de los datos introducidos

#solicito al usuario que introudzca unos numeros separados por comas
entrada = input('introduzca elementos separados por comas:\n')

# defino la funcion
def encontrar_primer_duplicado(lista):

  #(OMITIDO) paso innecesario
  #creo una lista vacia para añadir los elementos de la entrada 
  # lista = []
  # for e in entrada:
  #   lista = entrada.split(',')
  
  #creo un dicc vacio
  repetir = {}
  #añadir los elementos de la entrada al dicc y sumo +1 cuando se repite
  for e in entrada:
      if e != ',':    
        repetir[e] = repetir.get(e,0) + 1
        #condicion para encontrar el primer elemento que se repite segun la entrada del usuario
        if repetir[e] > 1:
          #print(repetir)
          print(f'El elemento que se repite primero es {e} y se repite {repetir[e]} veces.')
          return #pass para obtener todos los elementos duplicados
        
#llamo a la funcion
encontrar_primer_duplicado(entrada)


# OPCION 2
#buscar el valor repetido con el indice mas bajo

#solicito al usuario que introudzca unos numeros separados por comas
#entrada = input('introduzca elementos separados por comas:\n')

# defino la funcion
def encontrar_primer_elemento_duplicado(lista):  
  #creo un dicc vacio
  repetir = {}
  #añadir los elementos de la entrada al dicc y sumo +1 cuando se repite        
  for e in entrada:
      if e != ',':    
        repetir[e] = repetir.get(e,0) + 1 
        #print(repetir)         
  #condicion para encontrar el primer duplicado en el dicc
  for r in repetir:  
    if repetir[r] > 1:
      #print(repetir[e]) #devuelve value
      #print(e)          #devuelve key 
      #print(e,repetir[e])  #devuelve key , value
      return print(f'El primer elemento repetido es {r} y se repite {repetir[r]} veces.')

#llamo a la funcion
encontrar_primer_elemento_duplicado(entrada)

'''
EJERCICIO 4. Función  enmascarado_datos :
Descripción del ejercicio:
Crea una función que convierta una variable en una cadena de texto y 
enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
'''

#solicito al usuario que introduzca unos caracteres que almaceno en una variable "cadena"
cadena = (input('Introduca una serie de caracteres:\n'))

# defino la funcion
def enmascarado_datos(cadena):
  #establezco el rango de caracteres visibles como variable "n" para facil modifcacion
  n = 4
  # establezco el rango de caracteres a ocultar
  longitud_rango = len(cadena) - n
  # establezco el rango de caracteres visibles contando desde el final [-n:]
  rango_visibles = cadena[-n:]
  #establezco la formula de ocultacion
  ocultar = '#' * longitud_rango
  #establezco la nueva cadena con caracteres ocultos y visibles
  cadena_oculta = ocultar + rango_visibles
  #retorno
  print(f'la cadena introducioda es:\n{cadena}')
  print(f'la cadena enmascarada es:\n{cadena_oculta}')
  return

#llamo a la funcion
enmascarado_datos(cadena)


'''
Ejercicio 5. Función  es_anagrama :
Descripción del ejercicio:
Crea una función que determine si dos palabras son anagramas, es decir, 
si están formadas por las mismas letras pero en diferente orden.
'''

#solicito al usuario que introduzca dos palabras
a = input('ingresa la primera palabra:\n')
b = input('ingresa la segunda palabra:\n')

# defino la funcion
def es_anagrama(a,b):
  #compruebo que la longitud es igual
  if len(a) == len(b):
    #comparo si las letras de la primera palabra estan en la segunda palabra
    for letra in a:
      if letra in b:
        anagrama = True
    return anagrama
#solucion
if es_anagrama(a,b) == True:
  print(f'Las palabras {a} y {b} son anagrama')
else:
  print(f'Las palabras {a} y {b} no son anagrama')


'''
Ejercicio 6. Función  buscar_nombre :
Descripción del ejercicio:
Crea una función que solicite al usuario ingresar una lista de nombres y luego 
solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se 
imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
Caso de uso:
Incorpora los siguientes nombres a la lista y comprueba que la función 
funciona correctamente: "Jaime", "Silvia" y "Ana"
'''


#solicito al usuario que introduzca nombres separados por comas
entrada = input(f'Ingresa nombres separados por comas:\n')
#almaceno los nombres en una lista
lista_nombres = entrada.split(",")
#solicito al usuario que ingrese un nombre para comparar con los nombres de la lista
nombre = input(f'Ingresa un nombre para comparar:\n')

#solucion
if nombre in lista_nombres:
  print(f'El nombre {nombre} esta en la lista')
else:
  print(f'El nombre {nombre} no esta en la lista')


'''
Ejercicio 7. Función  fibonacci :
Descripción del ejercicio:
Crea una función que calcule el término n de la serie de Fibonacci utilizando 
recursión.
Definición de la secuencia de Fibonacci:
La secuencia de Fibonacci es una serie de números en la que cada número es 
la suma de los dos números anteriores, comenzando con 0 y 1. La posición 0 
es la primera.
'''

# definimos elemento de la serie fibonacci que queremos calcular
n = int(input('introduzca un numero entero:\n'))
#lista = list(range(0,n))
#print(lista) #[0, 1, 2,........, n]

#definimos la funcion
def fibonacci(n):
    # para n = 1 o 2 devuelve 1
    if n == 1 or n == 2:
      return 1
    #para n>2 devuelve: (recursividad)
    # resultado de funcion fibonacci de n-1 
    # + 
    # resultado de funcion fibonacci de n-1 
    else:  
      return fibonacci(n-1) + fibonacci(n-2)
#resultado 
print(f'El numero {n} de la serie fibonacci es:\n{fibonacci(n)}')  

fibonacci_lambda = lambda n: 1 if n == 1 or n == 2 else fibonacci(n-1) + fibonacci(n-2) 
print(f'El numero {n} de la serie fibonacci es:\n{fibonacci_lambda(n)}')


'''
Ejercicio 8. Función  encontrar_puesto_empleado :
Descripción del ejercicio:
Descripción:
Crea una función que tome un nombre completo y una lista de empleados, 
busque el nombre completo en la lista y devuelve el puesto del empleado si 
está en la lista, de lo contrario, devuelve un mensaje indicando que la persona 
no trabaja aquí.
'''

#Caso de uso:
#Lista de empleados dada en el ejercicio
empleados  = [{'nombre': "Juan", 'apellido': "García", 'puesto': "Secretario"},
              {'nombre': "Mabel", 'apellido': "García", 'puesto': "Product Manager"},
              {'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}]

#solicitamos la entrada del nombre completo al usuario
entrada = input('Introuduzca el nombre y el apellido separados por un espacio en blanco:\n')
#almacenamos en una lista el nombre y el apellido separadondolos por el espacio en blanco
nombre_completo = entrada.split()
#print(nombre_completo)
#definmos el nombre como la posicion 0 de la lista nombre_completo
nombre = nombre_completo[0]
#print(nombre)
#definmos el apellido como la posicion 1 de la lista nombre_completo
apellido = nombre_completo[1]
#print(apellido)

#definimos la funcion
def encontrar_puesto_empleado(nombre,apellido):
  #itera por los elementos (dicc0, dicc1, dicc2) en la lista empleados
  for empleado in empleados:
    #si coinciden el value nombre Y apellido con las key 'nombre' Y 'apellido')
    if nombre == empleado['nombre'] and apellido == empleado['apellido']:
      #devuelve el puesto
      puesto = empleado['puesto']
      print (f'El puesto de la persona {nombre} {apellido} es: {puesto}')
    #En otro caso devuelve 'no trabaja aqui'
    else:
      print(f'La persona {nombre} {apellido} no trabaja aqui.')
      
    return
#llamo a la funcion
encontrar_puesto_empleado(nombre,apellido)
#print(f'El puesto de la persona {nombre} {apellido} es: {encontrar_puesto_empleado(nombre,apellido)}') 


'''
Ejercicio 9. Función  cubo_numero  usando lambdas:
Descripción del ejercicio:
Crea una función que calcule el cubo de un número dado mediante una 
función lambda
'''

#definimos el numero que queremos elevar al cubo:
n = int(input('Introduzca un numero entero:\n'))
cubonumero = lambda n: n ** 3
print(f'El cubo del número {n} es:\n{cubonumero(n)}')

#funcion sin lambda:
# def cubo(n):
#   return n ** 3
# print(cubo(n))


'''
Ejercicio 10. Función  resto_division  usando lambdas:
Descripción del ejercicio:
Descripción:
Crea una función lambda  que calcule el resto de la división entre dos números dados.
'''

# #definimos el numero que queremos de dividendo y el divisor:
a = float(input('Introduzca un numero para dividendo:\n'))
b = float(input('Introduzca el numero para divsor:\n'))

#definimos funcion lambda
resto_division = lambda a,b: a % b    # = a - (b * (a / b))
#resultado
print(round(resto_division(a,b),2))

#funcion sin lambda:
def resto(n,m):
  r= a % b # = a - (b*(a / b))
  return r
print(round(resto(a,b),2))


'''
Ejercicio 11. Función  numeros_pares  usando lambdas y 
filter :
Descripción del ejercicio:
Descripción:
Crea una función 
lambda  que filtre los números pares de una lista dada.
'''

#Caso de uso: 
lista_numeros = [24, 56, 2.3, 19, -1, 0]
#iteramos por todos los num de la lista_numeros
for num in lista_numeros:
  #funcion lambda para buscar los num pares en la lista_numeros 
  pares = list(filter(lambda num: num % 2 == 0,lista_numeros))
#solucion
print(pares)

#explicacion funcion lambda
# for num in lista_numeros:
#   if num % 2 == 0:
#     print(num)
# print(pares)


'''
Ejercicio 12. Función  numeros_suma usando lambdas y map :
Descripción del ejercicio:
Crea una función lambda  que sume 3 a cada número de una lista dada
'''

#Caso de uso: 
lista_numeros = [24, 56, 2.3, 19, -1, 0]

#funcion lambda que devuelve lista_suma despues de sumar 3 a cada num de lista_numeros
lista_suma = list(map(lambda num: num + 3,lista_numeros))
print(lista_suma)

# lista_suma =[]
# for num in lista_numeros:
#   num += 3
#   lista_suma.append(num) 
# print(lista_numeros)
# print(lista_suma)


'''
Ejercicio 13. Función  sumar_listas  usando lambdas:
Descripción del ejercicio:
Descripción:
Crea una función 
lambda  que sume elementos correspondientes de dos listas dadas.
'''

#Caso de uso:
lista_numeros_1 = [1, 4, 5, 6 , 7 , 7]
lista_numeros_2 = [3, 11, 34, 56]

#NO RESUELTO##
sumar_listas = lambda n,m: n + m 
lista_combinada = list(map(sumar_listas,lista_numeros_1,lista_numeros_2))
print(lista_combinada)

#prueba funcion
# lista_combinada = [n + m for n,m in zip(lista_numeros_1,lista_numeros_2)]
# print(lista_combinada)


'''
Ejercicio 14.  No te vayas por las ramas :
Explicación del ejercicio:
Crea la clase Arbol 
define un árbol genérico con un tronco y ramas como atributos. 
Los métodos disponibles son:
crecer_tronco ,  nueva_rama ,  crecer_ramas ,  quitar_rama  e info_arbol.
 
El objetivo es implementar estos métodos para manipular la estructura del árbol.
Código a seguir:
1.-Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.2.2-Implementar el método  crecer_tronco  para aumentar la longitud del tronco 
en una unidad.
3.-Implementar el método  nueva_rama  para agregar una nueva rama de 
longitud 1 a la lista de ramas.
4.-Implementar el método  crecer_ramas  para aumentar en una unidad la 
longitud de todas las ramas existentes.
5.-Implementar el método  quitar_rama  para eliminar una rama en una posición 
específica.
6.-Implementar el método  info_arbol  para devolver información sobre la 
longitud del tronco, el número de ramas y las longitudes de las mismas.

Caso de uso:
Crear un árbol.
Hacer crecer el tronco del árbol una unidad.
Añadir una nueva rama al árbol.
Hacer crecer todas las ramas del árbol una unidad.
Añadir dos nuevas ramas al árbol.
Retirar la rama situada en la posición 2.Obtener información sobre el árbol
'''

#definimos la clase arbol
class Arbol:
  #constructor de clase con argumentos tronco y ramas
  def __init__(self,tronco,ramas):
    self.tronco = tronco
    self.ramas = ramas #self.ramas = []#definimos como lista vacia
  #definimos metodo crecer tronco para sumar +1     
  def crecer_tronco(self):
    self.tronco += 1
    return self.tronco
  #definimos metodo nueva rama para añadir nueva rama a la lista  
  def nueva_rama(self):    
    self.ramas.append(1)
    return self.ramas
  #definimos metodo crecer rama para incremtar en 1 cada rama de la lista    
  def crecer_rama(self):
    self.ramas = list(map(lambda r: r + 1, self.ramas))
    return self.ramas
  #definimos metodo quitar rama para eliminar una rama de la lista segun la posicion indicada 
  def quitar_rama(self,indice):
    self.rama = self.ramas.pop(indice)
    return self.ramas
  #definimos metodo info para devolver informacion 
  def info_arbol(self):
    info = ""
    info += "Longitud del tronco: " + str(self.tronco) + "\n"
    info += "Numero de ramas: " + str(len(self.ramas)) + "\n"
    info += "Longitud de las ramas: " + str(self.ramas) + "\n"
    return info
    
#instanciamos el objeto arbol1 con los valores
#tronco = 1
#ramas = [] #lista vacia  
arbol1 = Arbol(1,[0])

print("tronco arbol1: ",arbol1.tronco)
print("ramas arbol1: ",arbol1.ramas) 
print(f'info arbol1:\n{arbol1.info_arbol()}')

#metodo crecer tronco para objeto arbol1
arbol1.crecer_tronco()
print("crecer tronco arbol1: ")
print(f'info arbol1:\n{arbol1.info_arbol()}')

#metodo nueva rama para objeto arbol1
arbol1.nueva_rama()
print("nueva rama arbol1: ")
print(f'info arbol1:\n{arbol1.info_arbol()}')

#metodo crecer rama para objeto arbol1
arbol1.crecer_rama()
print("crecer ramas arbol1: ")
print(f'info arbol1:\n{arbol1.info_arbol()}')

#metodo nueva rama para objeto arbol1 
#llamamos dos veces para crear 2 nuevas ramas
arbol1.nueva_rama()
arbol1.nueva_rama()
print("2 nuevas rama arbol1: ")
print(f'info arbol1:\n{arbol1.info_arbol()}')

#metodo quitar rama para objeto arbol1
arbol1.quitar_rama(1)
print("quitar ramas arbol1:")
print(f'info arbol1:\n{arbol1.info_arbol()}')


'''
Ejercicio 15. Clase UsuarioBanco : 
Explicación del ejercicio:
Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. 
Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

Código a seguir:

Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente
mediante True y False .

Implementar el método retirar_dinero para retirar dinero del saldo del
usuario. Lanzará un error en caso de no poder hacerse.

Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.

Implementar el método agregar_dinero para agregar dinero al saldo del usuario.

Caso de uso:

Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de
50, ambos con cuenta corriente.

Agregar 20 unidades de saldo de "Alicia".

Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".

Retirar 50 unidades de saldo a "Alicia".
'''

#creamos la clase usuario banco
class UsuarioBanco: 
  #constructor de clase con argumentos nombre (str), cuenta (boolean) y saldo (float = 0)
    def __init__(self,nombre,cuenta,saldo : float = 0):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta = True

    #metodo retirar dinero si el saldo lo permite    
    def retirar_dinero(self):
        cantidad = float(input(f'Indique cantidad a retirar:\n'))
        if cantidad < self.saldo:
            self.saldo -= cantidad
        else:
            print('No se puede realizar la operacion\nImporte superior al saldo')
        
        return self.saldo

    #metodo agregar dinero si el importe es correcto     
    def agregar_dinero(self):
        cantidad = float(input(f'Indique cantidad a ingresar:\n'))
        if cantidad > 0:
            self.saldo += cantidad
        else:
            print('No se puede realizar la operacion\nImporte erroneo')

        return self.saldo
        
    #metodo transferir dinero si el saldo lo permite y el importe es correcto
    def transferir_dinero(self,usu2):
        cantidad = float(input(f'Indique cantidad a transferir:\n'))
        if self.saldo > cantidad and cantidad > 0:
            self.saldo -= cantidad
            usu2.saldo += cantidad
            return "transferencia realizada"    
        else:
          print('No se puede realizar la operacion\nImporte superior al saldo')  

#instanciamos dos objetos 
#Alicia con los valores ("Alicia",True,100.00)
#Bob con los valores ("Bob",True,50.00)

Alicia = UsuarioBanco("Alicia",True,100.00)
Bob = UsuarioBanco("Bob",True,50.00)
print(Alicia.saldo)
print(Bob.saldo)

#metodo agregar dinero para alicia
Alicia.agregar_dinero()
print(Alicia.saldo)
print(Bob.saldo)

#metodo transferir dinero de Bob para Alicia
Bob.transferir_dinero(Alicia)
print(Alicia.saldo)
print(Bob.saldo)

#metodo retirar dinero para alicia
Alicia.retirar_dinero()
print(Alicia.saldo)
print(Bob.saldo)



'''
Ejercicio 16. Función procesar_texto : 
Explicación del ejercicio:
Crea una función llamada procesar_texto que procesa un texto según la opción especificada:
contar_palabras , reemplazar_palabras , eliminar_palabra . 
Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto . 

Código a seguir:
-Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.

-Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.

-Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.

-Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.

Caso de uso:
texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."

Dado el texto de ejemplo, llama a la función procesar_texto para probar sus funcionalidades:
1 Cuenta el número de veces que aparece cada palabra. 
2 Reemplaza la palabra texto por relato.
3 Elimina la palabra ejemplo.
'''

#texto de ejemplo:
texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."
#solicitamos introducion de cadena de texto
#texto = input('introduzca una cadena de texto:\n')

#definimos funcion para contar las palabras de un texto
def contar_palabra(texto):
  #definimos lista de caracteres especiales para no duplicar palabras (texto. y texto)
  caracteres = [',' , '.' , ':' , '/' , '&' , '%' , '%' , '$' , '¿' , '?' , '!' , '¡']
  #iteramos por lista caracteres 
  for caracter in caracteres:
    #buscamos en texto
    if caracter in texto:
      #eliminamos caracteres especiales en el texto
      texto_limpio = texto.replace(caracter,'')
  
  #creamos una lista con cada palabra como elemento
  lista = texto_limpio.split()
  #print(lista)
  #longitud = len(lista)
  #print(longitud)
  
  #creamos dicc vacio para almacenar pares {palabra : valor} 
  #cada palabra como clave y recuento como valor
  cuenta = {}
  #iteramos por lista  
  for palabra in lista:
      #si palabra esta en dicc sumamos 1 al valor  
      if palabra in cuenta:
          cuenta[palabra] += 1
      #si palabra no esta en dicc asignamos valor 1
      else:
          cuenta[palabra] = 1
  
  print(f'El numero de palabras en el texto es:\n{len(lista)} palabras,\nLas palabras son:')
  
  for clave,valor in cuenta.items():#devolvemos el par clave valor de dicc cuenta en renglones separados
    print(f'{clave}:{valor}')

  #devuelve dicc cuenta con los pares palabra:recuento
  return (cuenta)
#llamo a la funcion contar_palabra para el argumento texto
#print(contar_palabra(texto))

#definimos funcion para reemplazar las palabras de un texto
def reemplazar_texto():
  #definimos la palabra a reemplazar y la palabra nueva a introducir
  palabra_seleccion = "texto" #input('introduzca una palabra del texto para reemplazar:\n')
  palabra_nueva = "relato" #input('introduzca la palabra de reemplazo:\n')
  
  #buscamos la palabra_seleccion en texto
  if palabra_seleccion in texto:
    #si la encuentra reemplazamos por palabra_nueva 
    nuevo_texto = texto.replace(palabra_seleccion, palabra_nueva)
  #si no la encuentra devuelve mensaje de error 
  else: 
    print(f'La palabra {palabra_seleccion} no esta en el texto.')
  
  print(f'El nuevo texto despues de reemplazar "{palabra_seleccion}" por "{palabra_nueva}" es:')
  #devuelve nueva cadena de texto con la palabra reemplazada
  return(nuevo_texto)
#llamo a la funcion reemplazar_texto para el argumento texto
#print(reemplazar_texto())

#definimos funcion para reemplazar las palabras de un texto
def elimninar_palabra():
  #definimos la palabra a eliminar
  palabra_eliminar = "ejemplo" #input('introduzca una palabra del texto para eliminar:\n')
  #buscamos la palabra_eliminar en texto
  if palabra_eliminar in texto:
    #si la encuentra reemplazamos por nada
    nuevo_texto = texto.replace(palabra_eliminar, "")
  #si no la encuentra devuelve mensaje de error 
  else: 
    print(f'La palabra {palabra_eliminar} no esta en el texto.')
  print(f'El nuevo texto despues de eliminar {palabra_eliminar} es:')
  #devuelve nueva cadena de texto con la palabra eliminada
  return(nuevo_texto)
#llamo a la funcion eliminar_palabra para el argumento texto
#print(elimninar_palabra())

def procesar_texto(texto):
  #solicitamos al usu que introduzaca la opreacion elegida segun criterio dado
  opcion = input(f'introduzca la operacion a realizar:\n( 1=contar, 2=reemplazar, 3=eliminar)\n')
  if opcion == "1":
    print(contar_palabra(texto))
  elif opcion == "2":
    print(reemplazar_texto())
  elif opcion == "3":
    print(elimninar_palabra())
  else:
    print('operacion incorrecta')
#llamo a la funcion procesar_texto para el argumento texto  
procesar_texto(texto)

