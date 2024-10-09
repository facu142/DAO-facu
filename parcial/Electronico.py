from Producto import *


class Electronico(Producto):
    def __init__(self, tipo, codigo, nombre, precio_base, numero_garantia, recargo):
        super().__init__(tipo, codigo, nombre, precio_base)
        self.numero_garantia = numero_garantia
        self.recargo = recargo

    def calcular_precio_final(self):
        return self.precio_base + self.recargo

