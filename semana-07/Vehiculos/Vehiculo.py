from abc import *


class Vehiculo(ABC):
    def __init__(self, tipo, marca, matricula, modelo, costo_base):
        self.tipo = tipo
        self.marca = marca
        self.matricula = matricula
        self.modelo = modelo
        self.costo_base = costo_base

    def __str__(self):
        return f'{self.marca}'

    @abstractmethod
    def calcular_costo_mantenimiento(self):
        pass
