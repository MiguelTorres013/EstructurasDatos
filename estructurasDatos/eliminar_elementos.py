def eliminar_duplicados(lista):

 conjunto = set(lista)
 lista_no_duplicada = list(conjunto)
 return lista_no_duplicada

arreglo = [1,2,5,2,6,8,4,1,35,8,9,3,4,56,7,2,1,4,79,75,4,3,79,3]

final = eliminar_duplicados(arreglo)
print(final)

