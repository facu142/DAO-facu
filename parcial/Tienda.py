
from Electronico import *
from Ropa import *
from Alimento import *

class Tienda():
    def __init__(self):
        self.productos = []
        self.cargar_csv()

    def cargar_csv(self):
        archivo = open('productos.csv', 'rt')

        for linea in archivo:
            campos = linea.strip().split(',')
            tipo = int(campos[0])
            codigo = campos[1]
            nombre = campos[2]
            precio_base = float(campos[3])

            if tipo == 1:
                numero_garantia = int(campos[4])
                recargo = float(campos[5])
                producto = Electronico(tipo, codigo,nombre, precio_base, numero_garantia, recargo)
            elif tipo == 2:
                talla = campos[4]
                es_de_temporada = campos[5]
                producto = Ropa(tipo, codigo,nombre, precio_base, talla, es_de_temporada)
            elif tipo == 3:
                fecha_vencimiento = campos[4]
                producto = Alimento(tipo, codigo,nombre, precio_base, fecha_vencimiento )


            self.productos.append(producto)

        archivo.close()

    def mostrar_articulos(self):
        print('*** Listado de articulos ***')
        for p in self.productos:
            print(p)

    def calcular_promedio_de_precios_finales(self):
        acumulador = 0
        for p in self.productos:
            acumulador += p.calcular_precio_final()

        return acumulador / len(self.productos)

    def obtener_producto_precio_final_mas_alto(self):
        producto_mas_caro = self.productos[0]
        for p in self.productos:
            if p.calcular_precio_final() > producto_mas_caro.calcular_precio_final():
                producto_mas_caro = p

        return producto_mas_caro

    def mostrar_productos_por_categoria(self):
        contador_ropa = 0
        contador_alimento = 0
        contador_electronico = 0

        for p in self.productos:
            if isinstance(p, Ropa):
                contador_ropa += 1
            elif isinstance(p, Electronico):
                contador_electronico += 1
            elif isinstance(p,Alimento):
                contador_alimento += 1

        print('***** Cantidad de productos por categoria ****')
        print('Cantidad alimentos: ', contador_alimento)
        print('Cantidad ropa: ', contador_ropa)
        print('Cantidad electronico: ', contador_electronico)


    def mostrar_cantidad_ropa_de_temporada_por_talle(self):

        contador_S = 0
        contador_M = 0
        contador_L = 0
        contador_XL = 0

        for p in self.productos:
            if isinstance(p, Ropa):
                #print(p.talla, p.es_de_temporada)
                if p.talla == 'S' and p.es_de_temporada == 'True':
                    contador_S += 1
                elif p.talla == 'M' and p.es_de_temporada == 'True':
                    contador_M += 1
                elif p.talla == 'L' and p.es_de_temporada == 'True':
                    contador_L += 1
                elif p.talla == 'XL' and p.es_de_temporada == 'True':
                    contador_XL += 1

        print('Cantidad de ropa de temporada por talle:')
        print(f'Talle S: {contador_S}')
        print(f'Talle M: {contador_M}')
        print(f'Talle L: {contador_L}')
        print(f'Talle XL: {contador_XL}')

    def buscar_producto_por_codigo(self, codigo):
        for p in self.productos:
            if str(p.codigo) == str(codigo):
                return p

        return None

