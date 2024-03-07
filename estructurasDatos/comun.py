def matriz_duplicadas(matriz, matriz1):
    for elemento in matriz:
        if elemento in matriz1:
            return True
    return False

matriz = [1, 2, 5, 7, 8]
matriz1 = [3, 6, 3, 10]

if matriz_duplicadas(matriz, matriz1):
    print("Las listas tienen al menos un número duplicado.")
else:
    print("Las listas no tienen números duplicados.")




