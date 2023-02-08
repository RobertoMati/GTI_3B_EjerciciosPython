#Realiza un script que genere 10 identificadores de socio aleatoriamente. Un identificador de socio está basado en 3 letras y 2 números del 0 al 9. 
# Si se genera un identificador repetido, tendrá que generarse otro hasta que no salga repetido.

import random

def generarIdentificador():
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    identificador = ""
    for i in range(3):
        identificador += letras[random.randint(0, len(letras)-1)]
    for i in range(2):
        identificador += numeros[random.randint(0, len(numeros)-1)]
    return identificador

def main():
    identificadores = []
    for i in range(10):
        identificador = generarIdentificador()
        while identificador in identificadores:
            identificador = generarIdentificador()
        identificadores.append(identificador)
    print(identificadores)

main()