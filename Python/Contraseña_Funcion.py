#creamos lista en blanco para almacenar los diccionarios de los datos de contraseñas
Lista_contraseñas = []

def almacenar_contraseña():
    

    #variable n para definir el numero de digitos de la contraseña
    n = 3
    #bucle while para repetir el proceso hasta crear contraseña correcta
    while True:
        #solicitamos que introduzca la contraseña
        print(f'Recuerda que debe contener {n} caracteres, una mayuscula, una minuscula y un digito)\n')
        contraseña = input(f'Escriba su contraseña: \n')
        #establecemos condicion de contraseña segura (n caracteres, 1 mayuscula, 1 minuscula, 1 digito)
        if len(contraseña) == n and any(letra.isupper() for letra in contraseña) and any(letra.islower() for letra in contraseña) and any(letra.isdigit() for letra in contraseña):
            #si cumple condiciones solictamos repita la contraseña
            confirmar_contraseña = input(f'Repita su contraseña:\n')
            #comparamos las dos contraseñas introducidas para que sean igual
            if confirmar_contraseña == contraseña:
                print(f'La contraseña ha sido creada con exito')
                #paramos el programa
                break
            #en caso de no coincidencia repetimos el proceso
            if confirmar_contraseña != contraseña:
                print(f'Las contraseñas no coinciden')
        
            #mas facil ahorrando un paso if 
            #else:
            #print(f'Las contraseñas no coinciden. Por favor, inténtelo de nuevo.')  
            
        #reto diferentes comparaciones para avisar al usuario de cual es el fallo en la contraseña.
        elif len(contraseña) != n:
            print(f'la longitud de de la contraseña no es correcta, debe contener {n} caracteres')
        elif not any(letra.isupper() for letra in contraseña):
            print(f'La contraseña creada no cumple los criterios requeridos\n(Recuerda que debe contener al menos una mayuscula)')
        elif not any(letra.islower() for letra in contraseña):
            print(f'La contraseña creada no cumple los criterios requeridos\n(Recuerda que debe contener al menos una minuscula)')
        elif not any(letra.isdigit() for letra in contraseña):
            print(f'La contraseña creada no cumple los criterios requeridos\n(Recuerda que debe contener al menos un digito)')
        #solucion a cualquier otro tipo de error de contraseña
        else:
            print(f'La contraseña creada no cumple los criterios requeridos\n(Recuerda que debe contener {n} caracteres, una mayuscula, una minuscula y un digito)\n')
            
    #solictud de datos para almacenar la contraseña
    usuario = input(f'introduzca usuario:\n')
    web = input(f'introduzca sitio web:\n')
    #definimos dicionario con las {claves : valor} nuevos
    nueva_contraseña = {'web': web , 'usuario': usuario , 'contraseña': contraseña}
    #print(f'Los datos de la contraseña creada son:\n{nueva_contraseña}')
    return nueva_contraseña
  
#BUCLE FINAL
#Establecemos un contador  num para calcular de forma incremental 
#el numero de la contraseña creada
num = len(Lista_contraseñas)
#Bucle while para repetir el proceso cada vez que el usuario responda "si" 
while True:
    #preguntamos al usuario si quiere crear nueva contraseña.
    repetir = input('¿Quiere crear una contraseña nueva?: si/no\n')
    #Establecemos condicion y sumamos 1 por cada "si".
    if repetir == 'si':
        num += 1
        #Llamamos a la funcion almacenar contraseña para iniciar proceso de crear nueva contraseña
        nueva = almacenar_contraseña()
        #devolvemos el valor de la contraseña creada
        print(f'Los datos de la contraseña{num} son:\n{nueva}')
        #almacenar_contraseña (añadimos diccionario nueva contraseña a lista_contraseñas)
        Lista_contraseñas.append(nueva) 
       #devolvemos listado de contraseñas creadas
        print ((f'La lista contiene estas contraseñas:'),*Lista_contraseñas, sep='\n')   
    #Cerramos el programa cuando el usuario responde no
    elif repetir == 'no':
        print("Programa terminado")
        break
    else:
        print('Respuesta incorrecta')
        
        
'''        
PRUEBA DE CONCEPTO
Llamar a la funcion varias veces seguidas e ir añadiendo los diferentes diccionarios de contraseñas a la lista de contraseñas:

#almacenar_contraseña (añadimos diccionario nueva_contraseña a lista_contraseñas)  
contraseña1 = almacenar_contraseña()
Lista_contraseñas.append(contraseña1)
print (f'La lista contiene estas contraseñas:\n{Lista_contraseñas}')      

contraseña2 = almacenar_contraseña()
Lista_contraseñas.append(contraseña2)
#print (contraseña2)
#print ('La lista contiene estas contraseñas:')
print ((f'La lista contiene estas contraseñas:'),*Lista_contraseñas, sep='\n')

contraseña3 = almacenar_contraseña()
Lista_contraseñas.append(contraseña3)
#print (contraseña3)
#print ('La lista contiene estas contraseñas:')
print ((f'La lista contiene estas contraseñas:'),*Lista_contraseñas, sep='\n')

#output de todas las contraseñas almacenadas (ERROR solo muestra la ultima!!!!!)
#print ('La lista contiene estas contraseñas:')
#print ((f'La lista contiene estas contraseñas:'),*Lista_contraseñas, sep='\n')
'''  