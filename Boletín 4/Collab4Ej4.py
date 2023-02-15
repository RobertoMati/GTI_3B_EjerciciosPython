#Escribe una función que reciba el nombre de un fichero y que muestre por pantalla cuántas veces aparece cada palabra.

def palabrasConLetra(fichero):
    f = open(fichero, "r")
    contador = 0
    for linea in f:
        for palabra in linea.split():
            if palabra == "Roberto":
                contador += 1
    f.close()
    return contador

print(palabrasConLetra("palabras.txt"))