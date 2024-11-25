def quickSort(lista: list, rPointer = 0, lPointer = 0):
    if rPointer == 0:
        rPointer = len(lista) - 1
    
    pivot = lPointer
    lPointer += 1

    while not rPointer < lPointer:
        if lista[lPointer] < lista[pivot]:
            lPointer += 1
        elif lista[rPointer] > lista[pivot]:
            rPointer -= 1
        else:
            lista[lPointer], lista[rPointer] = lista[rPointer], lista[lPointer]
    
    lista[pivot], lista[rPointer] = lista[rPointer], lista[pivot]
    rPointer -= 1

    if rPointer > 0:
        quickSort(lista, lPointer= 0, rPointer = rPointer)
    
    if lPointer < len(lista) - 1:
        quickSort(lista, lPointer = lPointer, rPointer = len(lista) - 1)

    

quickSort([54, 11, 16, 93, 55])