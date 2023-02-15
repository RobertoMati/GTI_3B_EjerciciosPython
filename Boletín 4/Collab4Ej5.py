#Escribe una función generadora que devuelva una palabra de un fichero cada vez que es llamada.
import random
def generado(fichero):
    with open(fichero) as f:
        fichero = f.read()
        return random.choice(fichero.split())

res = generado("/Users/rober/Desktop/Carpeta Compartida Ubuntu/Ejercicios Python/Boletín 4/palabras.txt")
print(res)