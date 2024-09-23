from abc import abstractmethod, ABC


class Empleado(ABC):
    def __init__(self, tipo_empleado, legajo, nombre, apellido, sueldo_basico):
        self.tipo_empleado = tipo_empleado
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo_basico = float(sueldo_basico)

    @abstractmethod
    def calcular_sueldo(self):
        pass
