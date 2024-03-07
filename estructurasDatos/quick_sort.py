def quicksort(lista):

    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 6]
    menores = [elemento for elemento in lista if elemento < pivote]
    mayores = [elemento for elemento in lista if elemento > pivote]
    return quicksort(menores) + [pivote] + quicksort(mayores)

arreglo = [5,2,4,7,4,2,7,8,5,3,6,31,3,5]
final = quicksort(arreglo)

print(final)