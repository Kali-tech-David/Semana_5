def Ordenamiento_Insercion(carril):
    for brazo in range(1, len(carril)):
        moneda = carril[brazo]
        while moneda > 0 and carril[brazo - 1] > moneda:
            carril[brazo],carril[brazo - 1] = carril[brazo - 1],carril[brazo]   
    return carril

monedas = [2, 8, 5, 3, 9, 4, 1]
print("Cantidad de entrada: ", monedas)
print("Riel ordenado:    ", Ordenamiento_Insercion(monedas))
