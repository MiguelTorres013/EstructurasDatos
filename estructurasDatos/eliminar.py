def eliminar_numeros(matriz):
    return list(set(matriz))

matriz_original=[1,5,7,2,4,6,1,6,9,1,3,7,3,7,1]
print(eliminar_numeros(matriz_original))