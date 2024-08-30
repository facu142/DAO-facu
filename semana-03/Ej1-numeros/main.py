def principal():

    with open('numeros.txt', 'r') as archivo:
        lineas = archivo.readlines()

    numeros = set()
    sumatoria = 0
    contador_impares = 0
    contador_pares = 0
    sumatoria_pares = 0

    for linea in lineas:
        numero = int(linea.strip())
        numeros.add(numero)
        if numero % 2 != 0:
            contador_impares += 1
        else:

            sumatoria_pares += numero
            contador_pares += 1

        print(sumatoria_pares)
        print(contador_pares)
        sumatoria += numero

    promedio_pares = sumatoria_pares / contador_pares

    print('1) Cantidad de numeros no repetidos: ' + str(len(numeros)))
    print('2) Suma de los numeros:' + str(sumatoria))
    print(f'3) Cantidad de impares: {contador_impares}')
    print(f'4) Promedio de pares: {promedio_pares}')


if __name__ == '__main__':
    principal()
