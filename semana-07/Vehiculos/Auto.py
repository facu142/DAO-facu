from Vehiculo import *


class Auto(Vehiculo):
    def __init__(self, tipo, marca, matricula, modelo, costo_base, kilometraje):
        super().__init__(tipo, marca, matricula, modelo, costo_base)
        self.kilometraje = kilometraje

    def calcular_costo_mantenimiento(self):
        return self.costo_base * 1.1 if self.kilometraje > 100000 else self.costo_base

    #def __str__(self):
    #return super().__str__()  + f'{self.kilometraje}'
