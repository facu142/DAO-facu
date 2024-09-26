from Preventivo import Preventivo
from Correctivo import Correctivo


class Maquina:
    def __init__(self):
        self.mantenimientos = []
        self.cargar_datos_desde_csv()

    def cargar_datos_desde_csv(self):
        archivo = open('mantenimientos.csv', 'rt')

        for linea in archivo:
            campos = linea[:-1].split(',')

            tipo_mantenimiento = int(campos[0])
            fecha = campos[1]
            operario = campos[2]
            importe_repuestos = float(campos[3])
            if tipo_mantenimiento == 1:  # Preventivo
                resultado_mantenimiento = int(campos[4])
                importe_insumos = float(campos[5])
                mantenimiento = Preventivo(tipo_mantenimiento, fecha, operario, importe_repuestos,
                                           resultado_mantenimiento, importe_insumos)
            elif tipo_mantenimiento == 2: # Correctivo
                cantidad_horas_parada = int(campos[4])
                importe_tecnico = float(campos[5])
                mantenimiento = Correctivo(tipo_mantenimiento, fecha, operario, importe_repuestos,
                                           cantidad_horas_parada, importe_tecnico)


            self.mantenimientos.append(mantenimiento)
        archivo.close()

