from Inmobiliaria import *


def main():
    inmobliaria = Inmobiliaria()
    print('Suma de alquileres:', inmobliaria.calcular_suma_alquileres())
    print('Cantidad casas premium:', inmobliaria.contar_casas_premium())
    print('Departamento con importe mas bajo:', str(inmobliaria.obtener_departamento_alquiler_mas_bajo()))


if __name__ == '__main__':
    main()
