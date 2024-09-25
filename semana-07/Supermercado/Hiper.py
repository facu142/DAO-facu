from Sucursal import *


class Hiper(Sucursal):
    def __init__(self, tipo, numero, superficie, facturacion, importe_alquileres):
        super().__init__(tipo, numero, superficie, facturacion)
        self.importe_alquileres = importe_alquileres

    def calcular_resultado_comercial(self):
        return self.facturacion + self.importe_alquileres

    def es_rentable(self):
        return self.calcular_indice_rentabilidad() > 50

    def __str__(self):
        return super().__str__()
