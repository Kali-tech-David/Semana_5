def Ordenamiento_Burbuja(barco):
    for mar in range(len(barco)):
        for burbuja in range(len(barco) - mar - 1):
            if(barco[burbuja] > barco[burbuja + 1]):
                barco[burbuja], barco[burbuja + 1] = barco[burbuja + 1], barco[burbuja]
    return barco
barco = [2, 8, 5, 3, 9, 4, 1]
print("Carga original:", barco)
print("Carga ordenada:", Ordenamiento_Burbuja(barco))