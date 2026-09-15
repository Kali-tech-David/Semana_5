def Ordenamiento_Burbuja(carga):
    cantidad = len(carga)
    for paso in range(cantidad):
        for pos in range(0, cantidad - paso - 1):
            if carga[pos] > carga[pos + 1]:
                carga[pos], carga[pos + 1] = carga[pos + 1], carga[pos]            
    return carga

barco = [2, 8, 5, 3, 9, 4, 1]
print("Carga original:", barco)
print("Carga ordenada:", Ordenamiento_Burbuja(barco))