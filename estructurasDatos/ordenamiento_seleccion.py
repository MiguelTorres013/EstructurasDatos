def ordenamiento_por_seleccion(arreglo):
  for i in range(len(arreglo) - 1):
    minimo = i
    for j in range(i + 1, len(arreglo)):
      if arreglo[j] < arreglo[minimo]:
        minimo = j
    arreglo[i], arreglo[minimo] = arreglo[minimo], arreglo[i]

arreglos = [6,4,6,33,2,1,7,5,75,3,1]
ordenamiento_por_seleccion(arreglos)
print(arreglos)