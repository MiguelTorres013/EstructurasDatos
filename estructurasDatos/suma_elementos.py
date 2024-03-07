def suma_numeros(arreglo_numeros):


    suma = 0
    for n1 in arreglo_numeros:
        suma += n1
    return suma

arreglo_numeros = [0,4,6,1,35,6,2,42,1,6,3,67,2,15]
suma_total = suma_numeros(arreglo_numeros)
print("La suma total es:", suma_total)