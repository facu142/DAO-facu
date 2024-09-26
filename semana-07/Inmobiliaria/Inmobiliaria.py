from Casa import *
from Departamento import *

class Inmobiliaria:
    def __init__(self):
        self.inmuebles = []
        self.cargar_datos_csv()

    def cargar_datos_csv(self):
        archivo = open('inmuebles.csv')
        for linea in archivo:
            campos = linea.strip().split(',')

            tipo = int(campos[0])
            codigo = int(campos[1])
            propietario = campos[2]
            alquiler_base = float(campos[3])
            superficie = int(campos[4])

            if tipo == 1:
                cantidad_habitaciones = int(campos[5])
                tiene_pileta = int(campos[6])
                inmueble = Casa(tipo, codigo, propietario, alquiler_base, superficie, cantidad_habitaciones, tiene_pileta)
            elif tipo == 2:
                importe_expensas = float(campos[5])
                piso = int(campos[6])
                inmueble = Departamento(tipo, codigo, propietario, alquiler_base, superficie, importe_expensas, piso)

            self.inmuebles.append(inmueble)
        archivo.close()

    def calcular_suma_alquileres(self):
        suma = 0
        for inmueble in self.inmuebles:
            suma += inmueble.calcular_importe_definitivo()

        return suma

    def contar_casas_premium(self):
        contador = 0
        for inmueble in self.inmuebles:
            if isinstance(inmueble, Casa):
                if inmueble.es_casa_premium():
                    contador += 1

        return contador

    def obtener_departamento_alquiler_mas_bajo(self):
        primer_departamento_encontrado = False
        departamento_alquiler_mas_bajo = None
        for inmueble in self.inmuebles:
            if isinstance(inmueble, Departamento):
                if not primer_departamento_encontrado:
                    primer_departamento_encontrado = True
                    departamento_alquiler_mas_bajo = inmueble

                if inmueble.calcular_importe_definitivo() < departamento_alquiler_mas_bajo.calcular_importe_definitivo():
                    departamento_alquiler_mas_bajo = inmueble

        return departamento_alquiler_mas_bajo


