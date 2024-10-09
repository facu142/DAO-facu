from Empresa import *


def main():
    empresa = Empresa()
    print('Costo total mantenimientos:', empresa.calcular_costo_total_mantenimientos())
    print('Cantidad de camionetas con capacidad mayor a 1000:', empresa.contar_camionetas_cap_carga_mayor_a_1000())
    print('Cantidad de motos de alta cilindrada:', empresa.contar_motos_alta_cilintrada())
    print('Vehiculo con el costo de mantenimiento mas alto:', empresa.obtener_vehiculo_costo_mas_alto())


if __name__ == '__main__':
    main()
