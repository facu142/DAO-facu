from abc import *
from Mantenimiento import *


class Preventivo(Mantenimiento):

    def __init__(self, tipo_mantenimiento, fecha, operario, importe_repuestos, resultado_mantenimiento, importe_insumos):
        super().__init__(tipo_mantenimiento, fecha, operario, importe_repuestos)
        self.resultado_mantenimiento = resultado_mantenimiento
        self.importe_insumos = importe_insumos
