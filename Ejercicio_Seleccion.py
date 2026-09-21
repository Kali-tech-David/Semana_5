def Ordenamiento_Seleccion(array):
    for idx1 in range(len(array)):
        Min = idx1
        for idx2 in range(idx1 + 1, len(array)):
            if(array[idx2] < array[Min]):
                Min = idx2
        if(Min != idx1):
            array[idx1], array[Min] = array[Min], array[idx1]
        

    
array = [2, 8, 5, 3, 9, 4, 1]
Ordenamiento_Seleccion(array)
print(array)
    