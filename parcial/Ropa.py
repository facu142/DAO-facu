from Producto import *


class Ropa(Producto):
    def __init__(self, tipo, codigo, nombre, precio_base, talla, es_de_temporada):
        super().__init__(tipo, codigo, nombre, precio_base)
        self.talla = talla
        self.es_de_temporada = es_de_temporada

    def calcular_precio_final(self):
        return self.precio_base * 1.25 if self.es_de_temporada == 'True' else self.precio_base


