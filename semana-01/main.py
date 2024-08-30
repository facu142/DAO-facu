import random


def principal():
    x = -100000
    y = 100000
    lista = []
    n = 1000
    sumatoria = 0
    sumatoria_positivos = 0
    cant_positivos = 0
    cant_negativos = 0
    menor = y
    mayor = x
    existe_numero_que_termina_con_000 = False

    for i in range(1000):
        num = random.randint(x, y)
        lista.append(num)
        sumatoria += num
        if num > 0:
            cant_positivos += 1
            sumatoria_positivos += n
        if num < 0:
            cant_negativos += 1

        if num < menor: menor = num
        if num > mayor: mayor = num

        if (str(num)[-3:] == '000'):
            existe_numero_que_termina_con_000 = True
            print('numero que termina con 000', num)

    promedio = sumatoria / n
    promedio_positivos = sumatoria_positivos / cant_positivos

    print('cantidad positivos', cant_positivos)
    print('cantidad positivos', cant_negativos)
    print('promedio', promedio)
    print('promedio positivos', promedio_positivos)
    print('Menor', menor)
    print('Mayor', mayor)
    print('si') if existe_numero_que_termina_con_000 else print('no')


if __name__ == '__main__':
    principal()
