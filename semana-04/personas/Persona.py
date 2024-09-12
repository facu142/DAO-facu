class Persona:
    def __init__(self, documento, nombre, apellido, edad):
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.edad = int(edad)

    def __str__(self):
        return f'{self.documento} {self.nombre} {self.apellido} {self.edad}'
