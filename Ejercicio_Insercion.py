def Ordenamiento_Insercion(monedas):
    for compartimento in range (1, len(monedas)):
        valorMoneda = compartimento
        while valorMoneda > 0 and monedas[valorMoneda - 1] > monedas[valorMoneda]:
            monedas[valorMoneda - 1], monedas[valorMoneda] = monedas[valorMoneda], monedas[valorMoneda - 1]
            valorMoneda -= 1
    return monedas
    
monedas = [2, 8, 5, 3, 9, 4, 1]
print("Cantidad de entrada: ", monedas)
print("Riel ordenado:    ", Ordenamiento_Insercion(monedas))

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"{self.nombre} ({self.edad})"
