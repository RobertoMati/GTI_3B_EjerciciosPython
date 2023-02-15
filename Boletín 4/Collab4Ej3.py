#Escribe una función que recibe el nombre de un fichero (cada línea puede tener varias palabras) 
#y una letra, y que muestre por pantalla las palabras del fichero que contienen la letra.

def palabrasConLetra(fichero, letra):
    f = open(fichero, "r")
    for linea in f:
        palabras = linea.split()
        for palabra in palabras:
            if letra in palabra:
                print(palabra)
    f.close()

res = palabrasConLetra("/Users/rober/Desktop/Carpeta Compartida Ubuntu/Ejercicios Python/Boletín 4/palabras.txt", "a")

