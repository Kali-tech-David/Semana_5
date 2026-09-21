def BusquedaBinaria(array,elemento):
    low = 0
    higher = len(array) - 1
    while(higher - low > 1):
        mid = (higher + low)//2
        if(array[mid] == elemento):
            return True
        elif(array[mid] < elemento):
            low = mid
        else:
            higher = mid
    if(array[low] == elemento or array[higher] == elemento):
        return True
    else:
        return False

