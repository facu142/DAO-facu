from Auto import *
from Moto import *
from Camioneta import *


class Empresa:
    def __init__(self):
        self.vehiculos = []
        self.cargar_datos_csv()

    def cargar_datos_csv(self):
        archivo = open('vehiculos.csv', 'rt')
        for linea in archivo:
            campos = linea.strip().split(',')
            tipo = int(campos[0])
            marca = campos[1]
            matricula = campos[2]
            modelo = campos[3]
            costo_base = float(campos[4])

            if tipo == 1:
                kilometraje = int(campos[5])
                vehiculo = Auto(tipo, marca, matricula, modelo, costo_base, kilometraje)
            elif tipo == 2:
                capacidad_carga = int(campos[5])
                vehiculo = Camioneta(tipo, marca, matricula, modelo, costo_base, capacidad_carga)
            elif tipo == 3:
                cilindrada = int(campos[5])
                vehiculo = Moto(tipo, marca, matricula, modelo, costo_base, cilindrada)

            self.vehiculos.append(vehiculo)
        archivo.close()

    def calcular_costo_total_mantenimientos(self):
        acumulador = 0
        for v in self.vehiculos:
            acumulador += v.calcular_costo_mantenimiento()

        return acumulador

    def obtener_vehiculo_coste_mas_alto(self):
        vehiculo_coste_mas_alto = self.vehiculos[0]
        for v in self.vehiculos:
            if v.calcular_costo_mantenimiento() > vehiculo_coste_mas_alto.calcular_costo_mantenimiento():
                vehiculo_coste_mas_alto = v

        return vehiculo_coste_mas_alto

    def contar_camionetas_cap_carga_mayor_a_1000(self):
        contador = 0
        for v in self.vehiculos:
            if isinstance(v, Camioneta):
                if v.tiene_capacidad_de_carga_mayor_a_1000():
                    contador += 1

        return contador

    def contar_motos_alta_cilintrada(self):
        contador = 0
        for v in self.vehiculos:
            if isinstance(v, Moto):
                if v.es_alta_cilindrada():
                    contador += 1

        return contador

    def obtener_vehiculo_costo_mas_alto(self):
        vehiculo_costo_mas_alto = self.vehiculos[0]

        for v in self.vehiculos:
            if v.calcular_costo_mantenimiento() > vehiculo_costo_mas_alto.calcular_costo_mantenimiento():
                vehiculo_costo_mas_alto = v

        return vehiculo_costo_mas_alto

