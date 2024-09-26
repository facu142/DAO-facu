from abc import *


class Mantenimiento(ABC):

    def __init__(self, tipo_mantenimiento, fecha, operario, importe_repuestos):
        self.tipo_mantenimiento = tipo_mantenimiento
        self.fecha = fecha
        self.operario = operario
        self.importe_repuestos = importe_repuestos
