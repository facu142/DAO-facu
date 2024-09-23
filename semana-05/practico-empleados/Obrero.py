from Empleado import Empleado


class Obrero(Empleado):
    def __init__(self, tipo_empleado, legajo, nombre, apellido, sueldo_basico, dias):
        super().__init__(tipo_empleado, legajo, nombre, apellido, sueldo_basico)
        self._dias = int(dias)

    def calcular_sueldo(self):
        return (self.sueldo_basico / 20) * self._dias

