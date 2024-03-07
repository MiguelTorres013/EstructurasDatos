def multiplicacion(matriz):
    if not matriz:
        return 0

    fila_inicio = 0
    fila_fin = len(matriz) - 1
    columna_inicio = 0
    columna_fin = len(matriz[0]) - 1

    resultado = 1

    while fila_inicio <= fila_fin and columna_inicio <= columna_fin:

        for i in range(columna_inicio, columna_fin + 1):
            resultado *= matriz[fila_inicio][i]

        for i in range(fila_inicio + 1, fila_fin + 1):
            resultado *= matriz[i][columna_fin]

        if fila_inicio < fila_fin:
            for i in range(columna_fin - 1, columna_inicio - 1, -1):
                resultado *= matriz[fila_fin][i]

        if columna_inicio < columna_fin:
            for i in range(fila_fin - 1, fila_inicio, -1):
                resultado *= matriz[i][columna_inicio]

        fila_inicio += 1
        fila_fin -= 1
        columna_inicio += 1
        columna_fin -= 1

    return resultado

matriz = [
    [1,4,5],
    [4,4,2],
    [3,4,7]
]

resultado = multiplicacion(matriz)
print("El resultado de la multiplicación en forma de espiral", resultado)
