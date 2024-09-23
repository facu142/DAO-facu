from Obrero import Obrero
from Administrativo import Administrativo
from Vendedor import Vendedor
from Empleado import Empleado


class Empresa:
    def __init__(self, empleados):
        self._empleados = empleados

    @property
    def empleados(self):
        return self._empleados


def leer_empleados_archivo(archivo):
    empleados = []

    with open(archivo, 'r') as file:
        for linea in file:
            linea_empleado = linea.strip().split(',')
            if linea_empleado[0] == '1':  # Obrero
                clase = Obrero
            elif linea_empleado[0] == '2':  # Administrativo
                clase = Administrativo
            elif (linea_empleado[0] == '3'):  # Vendedor
                clase = Vendedor

            empleado = clase(linea_empleado[0],
                             linea_empleado[1],
                             linea_empleado[2],
                             linea_empleado[3],
                             linea_empleado[4],
                             linea_empleado[5])

            empleados.append(empleado)

    return empleados


if __name__ == '__main__':
    NOMBRE_ARCHIVO = 'empleados.csv'
    empleados = leer_empleados_archivo(NOMBRE_ARCHIVO)
    empresa = Empresa(empleados)

    cantidad_obreros = 0
    cantidad_vendedores = 0
    cantidad_administradores = 0

    total_sueldos = 0
    for empleado in empresa.empleados:
        total_sueldos += empleado.calcular_sueldo()
        print(empleado.tipo_empleado)
        if empleado.tipo_empleado == '1':
            cantidad_obreros += 1
        elif empleado.tipo_empleado == '2':
            cantidad_administradores += 1
        elif empleado.tipo_empleado == '3':
            cantidad_vendedores += 1

    print('Total sueldos: ', total_sueldos)
    print('Cantidad obreros: ', cantidad_obreros)
    print('Cantidad administradores: ', cantidad_administradores)
    print('Cantidad vendedores: ', cantidad_vendedores)

