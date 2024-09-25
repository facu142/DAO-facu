from abc import *


class Sucursal(ABC):
    def __init__(self, tipo, numero, superficie, facturacion):
        self.tipo = tipo
        self.numero = numero
        self.superficie = superficie
        self.facturacion = facturacion

    def __str__(self):
        return f'Tipo: {self.tipo} | Numero: {self.numero}'

    @abstractmethod
    def calcular_resultado_comercial(self):
        pass

    def calcular_indice_rentabilidad(self):
        return self.calcular_resultado_comercial() / self.superficie

    @abstractmethod
    def es_rentable(self):
        pass
