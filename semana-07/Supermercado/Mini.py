from Sucursal import *


class Mini(Sucursal):
    def __init__(self, tipo, numero, superficie, facturacion, importe_pagado_alquiler):
        super().__init__(tipo, numero, superficie, facturacion)
        self.importe_pagado_alquiler = importe_pagado_alquiler

    def calcular_resultado_comercial(self):
        return self.facturacion - self.importe_pagado_alquiler

    def es_rentable(self):
        return self.calcular_indice_rentabilidad() > 35

    def __str__(self):
        return super().__str__()
