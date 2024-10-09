from Producto import *


class Alimento(Producto):
    def __init__(self, tipo, codigo, nombre, precio_base, fecha_vencimiento):
        super().__init__(tipo, codigo, nombre, precio_base)
        self. fecha_vencimiento = fecha_vencimiento

    def calcular_precio_final(self):
        anio_vencimiento = self.fecha_vencimiento.split('-')[-1]
        return self.precio_base * 0.9 if anio_vencimiento < '2026' else self.precio_base


