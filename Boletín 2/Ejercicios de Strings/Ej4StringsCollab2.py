#Dado un string, muestra por pantalla un nuevo string que tenga los dos últimos caracteres movidos al inicio. 
#La longitud mínima del string será de 2.

palabra = input("Introduce una palabra: ")

if len(palabra) < 2:
    print("La palabra debe tener al menos 2 caracteres")
else:
    print(palabra[-2:] + palabra[:-2])
    