#Escribe una función que reciba el nombre de un fichero que contiene palabras 
#(cada línea tiene una palabra) y que devuelva la palabra que tiene una longitud máxima y su longitud.

def maximo(fichero):
    maximo = 0
    palabra = ''
    for linea in fichero:
        if len(linea) > maximo:
            maximo = len(linea)
            palabra = linea
    #El strip es para quitar el salto de linea (buscado en internet)
    return palabra.strip(), maximo-1

fichero = open('palabras.txt', 'r')
palabra = maximo(fichero)
print(palabra)