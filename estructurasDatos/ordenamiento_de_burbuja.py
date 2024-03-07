def ordenamientoBurbuja(una_lista):
    for num_pasada in range(len(una_lista)-1,0,-1):
        for i in range(num_pasada):
            if una_lista[i]>una_lista[i+1]:
                temp = una_lista[i]
                una_lista[i] = una_lista[i+1]
                una_lista[i+1] = temp

una_lista = [54,26,93,17,77,31,44,55,20]
ordenamientoBurbuja(una_lista)
print(una_lista)
