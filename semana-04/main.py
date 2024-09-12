import random

from codecarbon import EmissionsTracker
from Punto import Punto


def main():
    # Inicialización del tracker
    tracker = EmissionsTracker()

    # Comienza el trackeo de emisiones
    tracker.start()

    # Ejecución del código a medir
    for i in range(100000000):
        A = Punto(random.randint(-100, 100), random.randint(-100, 100))
        B = Punto(random.randint(-100, 100), random.randint(-100, 100))

        print('cuadrante punto A:', A.cuadrante)
        print(f'distancia entre A={A} y B={B}:', A.distancia(B))

    # Detiene el trackeo de emisiones
    emisiones = tracker.stop()

    print(f"Emisiones estimadas de CO2eq: {emisiones} kg")


if __name__ == '__main__':
    main()
