import abc
import dataclasses

class Factura:
    def __init__(self, numero, fecha, total):
        self.numero = numero
        self.fecha = fecha
        self.total = total
        self.contar()

    cantidad = 0

    @classmethod
    def contar(cls):
        cls.cantidad += 1
        return cls.cantidad

    @staticmethod
    def con_iva(importe):
        return importe * 1.21


# Clase abstracta
@dataclasses.dataclass
class Persona(abc.ABC):
    nombre = ''
    apellido = ''
    documento = 0

    @property
    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'


    @abc.abstractmethod
    def saludar(self):
        pass


def main():
    f1 = Factura(1, '18/08/2024', 10000)
    print(f1.contar())
    print(Factura.contar())


if __name__ == '__main__':
    main()
