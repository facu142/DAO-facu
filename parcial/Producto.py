from abc import *

class Producto(ABC):
    def __init__(self,tipo, codigo, nombre, precio_base):
        self.tipo = tipo
        self.codigo = codigo
        self.nombre = nombre
        self.precio_base = precio_base

    def __str__(self):
        return f'Articulo: {self.nombre} Precio base: {self.precio_base} Precio final: {self.calcular_precio_final()} codigo {self.codigo}'


    @abstractmethod
    def calcular_precio_final(self):
        pass


