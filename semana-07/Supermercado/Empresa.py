from Hiper import *
from Super import *
from Mini import *


class Empresa:
    def __init__(self):
        self.sucursales = []
        self.cargar_datos_desde_csv()

    def cargar_datos_desde_csv(self):
        file = open('./sucursales.csv', 'rt')
        for linea in file:
            campos = linea[:-1].split(',')
            tipo = int(campos[0])
            numero = int(campos[1])
            superficie = float(campos[2])
            facturacion = float(campos[3])

            if (tipo == 1):  # hiper
                importe_alquileres = float(campos[4])
                sucursal = Hiper(tipo, numero, superficie, facturacion, importe_alquileres)
            elif (tipo == 2):  # super
                es_mayorista = int(campos[4])
                sucursal = Super(tipo, numero, superficie, facturacion, es_mayorista)
            elif (tipo == 3):  # mini
                importe_pagado_alquiler = float(campos[4])
                sucursal = Mini(tipo, numero, superficie, facturacion, importe_pagado_alquiler)

            self.sucursales.append(sucursal)
        file.close()

    def calcular_suma_de_ganancia(self):
        sumatoria = 0
        for s in self.sucursales:
            sumatoria += s.calcular_resultado_comercial()
        return sumatoria

    def cantidad_locales_no_rentables(self):
        contador = 0
        for s in self.sucursales:
            if not s.es_rentable():
                contador += 1

        return contador

    def obtener_sucursal_mas_rentable(self):
        sucursal_mas_rentable = self.sucursales[0]

        for s in self.sucursales:
            if s.calcular_indice_rentabilidad() > sucursal_mas_rentable.calcular_indice_rentabilidad():
                sucursal_mas_rentable = s

        return sucursal_mas_rentable


