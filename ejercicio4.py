palabra = input('escribe una palabra:')
vocales = 'a,e,i,o,u,A,E,I,O,U'
for letra in palabra:
  if letra in vocales:
    print(letra)
    