def contar_ocurrencias(lista):

  diccionario = {}

  for elemento in lista:
    if elemento not in diccionario:
      diccionario[elemento] = 1
    else:
      diccionario[elemento] += 1
  return diccionario

numeros = [2,4,6,1,5,7,3,5,8,2]
final = contar_ocurrencias(numeros)

print(final)