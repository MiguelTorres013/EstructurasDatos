numeros = [1,2,5,77,44,33,226,43,72,9,2,4]

numero_mayor = None

for n1 in numeros:
    if numero_mayor is None or n1 > numero_mayor:
        numero_mayor = n1

print("El numero mayor es: ", numero_mayor)