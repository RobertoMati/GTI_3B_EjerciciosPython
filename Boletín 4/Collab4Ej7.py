#Escribe un programa que lee el nombre del fichero de texto del teclado y muestra por pantalla el texto codificado de forma que sólo las letras minúsculas 
# se sustituyen por las siguientes según el abecedario (una a por una b, una b por una c, etc.).
import string
#string.ascii_letters

def codificado(fichero):
    with open("/Users/rober/Desktop/Carpeta Compartida Ubuntu/Ejercicios Python/Boletín 4/"+fichero, "r") as f:
        for linea in f:
            for letra in linea:
                if letra in string.ascii_lowercase:
                    print(chr(ord(letra)+1), end="")
                else:
                    print(letra, end="")
            print()

res=input("Introduce el nombre del fichero: ")
imprimir=codificado(res + ".txt")