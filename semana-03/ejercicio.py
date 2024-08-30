archivo = open('Ej2-Practico del quijote/words_alpha.txt')
palabas = set()

for linea in archivo.readline():
    palabas.add(linea)

frase = "today is monday 12 september"
ingresadas = frase.split((' '))
corregidas = {p + "\n" for p in ingresadas}
print(set(ingresadas) - corregidas)