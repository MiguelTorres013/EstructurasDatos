def multiplicar_matrices(matriz1,matriz2):

    filas_a = len(matriz1)
    columnas_a = len(matriz1[0])
    columnas_b = len(matriz2[0])

    matriz3 = [[0 for j in range(columnas_b)] for i in range(filas_a)]

    for i in range(filas_a):
        for j in range(columnas_b):
            for k in range(columnas_a):
                matriz3[i][j] += matriz1[i][k] * matriz2[k][j]

    return matriz3

matriz1 =[[1,8],[2,6]]
matriz2 =[[4,2],[6,2]]

final = multiplicar_matrices(matriz1,matriz2)
print(final)