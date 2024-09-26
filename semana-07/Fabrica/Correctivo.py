from abc import *
from Mantenimiento import *


class Correctivo(Mantenimiento):

    def __init__(self, tipo_mantenimiento, fecha, operario, importe_repuestos, cantidad_horas_parada, importe_tecnico):
        super().__init__(tipo_mantenimiento, fecha, operario, importe_repuestos)
        self.cantidad_horas_parada = cantidad_horas_parada
        self.importe_tecnico = importe_tecnico
