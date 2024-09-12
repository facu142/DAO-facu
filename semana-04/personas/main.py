from Persona import Persona


def cargarPersonasArchivo(archivo):
    personas = {}

    with open(archivo, 'r') as file:
        for linea in file:
            listaPersona = linea.strip().split(',')

            objetoPersona = Persona(listaPersona[0],
                                    listaPersona[1],
                                    listaPersona[2],
                                    listaPersona[3])

            # Usar el documento (listaPersona[0]) como clave en el diccionario
            documento = listaPersona[0]
            personas[documento] = objetoPersona

    return personas


def main():
    personas = cargarPersonasArchivo('personas.csv')

    contMayoresEdad = 0

    print(f'a) Cantidad de personas cargadas: {len(personas)}')
    print(f'b) Cantidad de personas mayores de edad {contMayoresEdad}')
    print(f'c) Listado de nombres y apellidos de aquellas personas cuyo apellido empieze en vocal')

    for documento, persona in personas.items():
        if persona.edad >= 18:
            contMayoresEdad += 1
        if persona.apellido[0].upper() in ['A', 'E', 'I', 'O', 'U']:
            print(f'{persona.nombre} {persona.apellido}')

    apellidos = {}
    for persona in personas.values():
        if persona.apellido in apellidos:
            apellidos[persona.apellido] += 1
        else:
            apellidos[persona.apellido] = 1

    print(f'd) Cantidad de personas por cada apellido: {apellidos}')


if __name__ == '__main__':
    main()
