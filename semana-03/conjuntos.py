def principal():
    # conjuntos
    # no tienen repetidoss
    conjunto = set()  # conjunto vacio
    conjunto_enumeracion = {1, 2, 3, 4}

    conjunto_comprension = {x for x in range(10)}
    conjunto_comprension2 = {x ** 2 for x in range(10)}
    print(conjunto_comprension2)

    # agregar
    # add  (agrega un valor)
    # update (agrega todos los valores del iterables)
    # En ambos casos ignorando los repetidos
    conjunto_enumeracion.add(5)
    conjunto_enumeracion.update([1, 2, 3, 41, 2412, 412124, 1, 23, 4, 5, 6, 7, 1])
    print(conjunto_enumeracion)
    for x in conjunto_enumeracion:
        print(x)  # quedan ordenados porque son numeros
    dias = {'lunes', 'martes', 'miercoles'}

    for dia in dias:
        print(dia)  # No los muestra ordenados

    # pertenencia
    # in y not
    print('sabado' in dias)

    # interseccion de conjuntos
    A = {2, 3, 41, 51, 2, 3, 41, 23, 4, 1}
    pares = {x * 2 for x in range(10)}
    # print(A & pares)
    # print(A.intersection_update((pares)))
    # union
    print(A | pares)
    # diferencia excluyente
    print(A ^ pares)

    # diccionario: guarda la clave y el objeto
    materias = {"AED": "Algoritmos", "MAD": "Matematica discreta", "AM1": "Analisis matematico 1"}
    print(materias['AED'])
    print('GDA' in materias)
    materias['GDA'] = 'Gestion de datos'
    print('GDA' in materias)

    for sigla, nombre in sorted(materias.items()):
        print(f"{sigla} : {nombre}")


if __name__ == '__main__':
    principal()
