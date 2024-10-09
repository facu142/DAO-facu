from Vehiculo import *


class Moto(Vehiculo):
    def __init__(self, tipo, marca, matricula, modelo, costo_base, cilindrada):
        super().__init__(tipo, marca, matricula, modelo, costo_base)
        self.cilindrada = cilindrada

    def calcular_costo_mantenimiento(self):
        return self.costo_base * 1.20 if self.cilindrada > 500 else self.costo_base


    def es_alta_cilindrada(self):
        return self.cilindrada > 500