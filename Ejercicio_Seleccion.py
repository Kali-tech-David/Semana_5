def Ordenamiento_Seleccion(array):
    n = len(array)
    for i in range (n-1):
        iMin = i
        for j in range (i+1, n):
            if array[j] < array[iMin]:
                iMin = j
        if(iMin != i):
            Cambiar_Valores(array, i, iMin)

def Cambiar_Valores(array, j, iMin):
    aux = array[j]
    array[j] = array[iMin]
    array[iMin] = aux
    
array = [2, 8, 5, 3, 9, 4, 1]
Ordenamiento_Seleccion(array)
print(array)
    