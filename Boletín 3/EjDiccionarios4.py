#Escribe un programa que lea un texto por teclado. Posteriormente debe crear un diccionario donde las claves sean las palabras del texto y sus 
#valores el número de apariciones de cada una de éstas en el texto. Muestra el resultado por pantalla.

def creaDiccionario(texto):
    diccionario = {}
    for palabra in texto.split():
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario

def main():
    texto = input("Introduce un texto: ")
    diccionario = creaDiccionario(texto)
    print("El diccionario es: ", diccionario)

main()