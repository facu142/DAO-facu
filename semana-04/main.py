from Punto import Punto


def main():
    A = Punto(3, 4)
    B = Punto()
    print(A)
    print(B)
    print(A.x)
    A.x = 5  # Parece asignacion pero llama al setter
    print('cuadrante:', A.cuadrante)
    print('distancia Origen:', A.distanciaOrigen())
    print('distancia entre A y B:', A.distancia(B))
    print('A + B:', A + B)


if __name__ == '__main__':
    main()
