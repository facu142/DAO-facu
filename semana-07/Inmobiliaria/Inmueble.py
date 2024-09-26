from abc import *

class Inmueble(ABC):
    def __init__(self, tipo, codigo, propietario, alquiler_base, superficie):
        self.tipo = tipo
        self.codigo = codigo
        self.propietario = propietario
        self.alquiler_base = alquiler_base
        self.superficie = superficie

    @abstractmethod
    def calcular_importe_definitivo(self):
        pass

    def __str__(self):
        return f'numero: {self.codigo} Propietario: {self.propietario}'


