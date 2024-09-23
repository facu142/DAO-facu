from Empleado import Empleado


class Administrativo(Empleado):
    def __init__(self, tipo_empleado, legajo, nombre, apellido, sueldo_basico, presentismo):
        super().__init__(tipo_empleado, legajo, nombre, apellido, sueldo_basico)
        self._presentismo = presentismo

    def calcular_sueldo(self):
        if self._presentismo:
            return self.sueldo_basico + self.sueldo_basico * 0.13
        else:
            return self.sueldo_basico

