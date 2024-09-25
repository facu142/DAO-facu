from Empresa import *


def main():
    empresa = Empresa()
    print('Suma de ganancia', empresa.calcular_suma_de_ganancia())
    print('Cantidad de locales no rentables:', empresa.cantidad_locales_no_rentables())
    print('Local mas rentable', str(empresa.obtener_sucursal_mas_rentable()))


if __name__ == '__main__':
    main()
