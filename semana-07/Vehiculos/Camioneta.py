from Vehiculo import *


class Camioneta(Vehiculo):
    def __init__(self, tipo, marca, matricula, modelo, costo_base, capacidad_carga):
        super().__init__(tipo, marca, matricula, modelo, costo_base)
        self.capacidad_carga = capacidad_carga

    def calcular_costo_mantenimiento(self):
        return self.costo_base * 1.15 if self.capacidad_carga > 1000 else self.costo_base

    def tiene_capacidad_de_carga_mayor_a_1000(self):
        return self.capacidad_carga > 1000