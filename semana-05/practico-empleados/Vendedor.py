from Empleado import Empleado


class Vendedor(Empleado):
    def __init__(self, tipo_empleado, legajo, nombre, apellido, sueldo_basico, importe_ventas_del_mes):
        super().__init__(tipo_empleado, legajo, nombre, apellido, sueldo_basico)
        self._importe_ventas_del_mes = float(importe_ventas_del_mes)

    def calcular_sueldo(self):
        return self.sueldo_basico + self._importe_ventas_del_mes * 0.01
