from Tienda import *

def main():
    tienda = Tienda()
    tienda.mostrar_articulos()
    print('Promedio de precios finales:', tienda.calcular_promedio_de_precios_finales())
    tienda.mostrar_productos_por_categoria()
    tienda.mostrar_cantidad_ropa_de_temporada_por_talle()
    print('Producto Mas caro: ', tienda.obtener_producto_precio_final_mas_alto())

    codigo = input('Ingrese el codigo para buscar (q para salir): ')
    while(codigo != 'q'):
        p = tienda.buscar_producto_por_codigo(codigo)
        if(p):
            print('Producto encontrado:', p)
        else:
            print('No se encontro')

        codigo = input('Ingrese el codigo para buscar (q para salir): ')


if __name__ == '__main__':
    main()
