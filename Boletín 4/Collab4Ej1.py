#Escribe un programa que genere un fichero de texto con los números del 1 al 5000 y sus cuadrados.
import os
file = open("prueba.txt", "w")
for i in range(1,5001):
    file.write("Número " + str(i) +", y su cuadrado es "+ str(i*i) + os.linesep)
file.close()
