import math


class Punto:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return f'x: {self._x}  y: {self._y}'

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, nuevo):
        self._x = nuevo  # Acá debería validar

    @y.setter
    def y(self, nuevo):
        self._y = nuevo  # Acá debería validar

    # Metodo cuyo nombre es un sustantivo
    @property
    def cuadrante(self):
        if self._x > 0:
            if self._y > 0:
                return 1
            else:
                return 4
        else:
            if self._y > 0:
                return 2
            else:
                return 3

    # Distancia desde el origen
    def distanciaOrigen(self):
        # pitagoras
        return math.sqrt((self._x ** 2 + self._y ** 2))

    # Distancia entre dos puntos
    def distancia(self, otro):
        dx = self._x - otro.x
        dy = self._y - otro.y

        return math.sqrt((dx ** 2 + dy ** 2))

    # Sobrecarga de operador +
    def __add__(self, other):
        return Punto(self._x + other.x, self._y + other.y)

