from Inmueble import *
from abc import *

class Casa(Inmueble):
    def __init__(self, tipo, codigo, propietario, alquiler_base, superficie, cantidad_habitaciones, tiene_pileta):
        super().__init__(tipo, codigo, propietario, alquiler_base, superficie )
        self.cantidad_habitaciones = cantidad_habitaciones
        self.tiene_pileta = tiene_pileta

    def calcular_importe_definitivo(self):
        return self.alquiler_base + 30000 * self.cantidad_habitaciones + 100000 if self.tiene_pileta else self.alquiler_base + 30000 * self.cantidad_habitaciones

    def es_casa_premium(self):
        return self.cantidad_habitaciones > 2 and self.superficie > 150 and self.tiene_pileta

