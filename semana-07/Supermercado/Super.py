from Sucursal import *


class Super(Sucursal):
    def __init__(self, tipo, numero, superficie, facturacion, es_mayorista):
        super().__init__(tipo, numero, superficie, facturacion)
        self.es_mayorista = es_mayorista

    def calcular_resultado_comercial(self):
        return self.facturacion

    def es_rentable(self):
        indice_rentabilidad = self.calcular_indice_rentabilidad()
        if self.es_mayorista:
            return indice_rentabilidad > 45
        else:
            return indice_rentabilidad > 40

    def __str__(self):
        return super().__str__()
