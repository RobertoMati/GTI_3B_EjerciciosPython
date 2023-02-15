#Escribe un función que anonimice el fichero interview.txt. Este fichero contiene una entrevista con Trump, pero su nombre no puede aparecer y hay 
#que cambiarlo a "Mr. X" para anonimizar el fichero. El resultado, será escrito en un fichero anonymous.txt.

def anonimacion():
    with open("/Users/rober/Desktop/Carpeta Compartida Ubuntu/Ejercicios Python/Boletín 4/interview.txt", "r") as f:
        with open("/Users/rober/Desktop/Carpeta Compartida Ubuntu/Ejercicios Python/Boletín 4/anonymous.txt", "w") as f2:
            for line in f:
                f2.write(line.replace("Trump", "Mr. X"))

anonimacion()
