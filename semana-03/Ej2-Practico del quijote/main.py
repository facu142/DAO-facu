import re


def principal():
    archivoQuijote = open('quijote.txt')
    archivoDiccionario = open('words_alpha.txt')


    palabras_quijote = set()
    palabras_diccionario = set()

    for linea in archivoQuijote:
        palabras_linea = re.findall(r'\b\w+\b', linea.lower())

        for palabra in palabras_linea:
            palabras_quijote.add(palabra.lower())

    for linea in archivoDiccionario:
        palabras_diccionario.add(linea.strip().lower())

    palabras_que_no_existen = palabras_quijote - palabras_diccionario

    print(f'1) Cantidad de palabras únicas (sin repetición) del libro: {len(palabras_quijote)} ')
    print(f'2) Cantidad de palabras del diccionario: {len(palabras_diccionario)} ')
    print(f'3) Cantidad de palabras del libro que no existen en el diccionario.: {len(palabras_que_no_existen)} ')
    print(f'4) Listado ordenados de todas las palabras que no existen:')

    print( sorted(palabras_que_no_existen) )

if __name__ == '__main__':
    principal()
