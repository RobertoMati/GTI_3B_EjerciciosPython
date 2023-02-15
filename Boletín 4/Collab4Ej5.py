#Escribe una función generadora que devuelva una palabra de un fichero cada vez que es llamada.
import random
def generado(fichero):
    with open(fichero) as f:
        fichero = f.read()
        return random.choice(fichero.split())

res = generado("palabras.txt")
print(res)