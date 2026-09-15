def Ordenamiento_Insercion(carril):
    for brazo in range(1, len(carril)):
        moneda = brazo
        while moneda > 0 and carril[moneda - 1] > carril[moneda]:
            carril[moneda],carril[moneda- 1] = carril[moneda - 1],carril[moneda]
            moneda -= 1
    return carril

monedas = [2, 8, 5, 3, 9, 4, 1]
print("Cantidad de entrada: ", monedas)
print("Riel ordenado:    ", Ordenamiento_Insercion(monedas))
