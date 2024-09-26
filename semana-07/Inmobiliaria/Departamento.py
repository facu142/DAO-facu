from Inmueble import *
from abc import *

class Departamento(Inmueble):
    def __init__(self, tipo, codigo, propietario, alquiler_base, superficie, importe_expensas, piso):
        super().__init__(tipo, codigo, propietario, alquiler_base, superficie )
        self.importe_expensas = importe_expensas
        self.piso = piso

    def calcular_importe_definitivo(self):
        importe = self.alquiler_base + self.importe_expensas
        if self.piso < 3:
            importe += 20000
        return importe




