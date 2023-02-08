#Dado un string, muestra por pantalla un nuevo string que sea 3 copias de los últimos dos caracteres del string original. 
# La longitud mínima del string será de 2, si no, el programa mostrará un mensaje y terminará. 

palabra = input("Introduce una palabra: ")

if len(palabra) < 2:
    print("La palabra debe tener al menos 2 caracteres")
else:
    print(palabra[-2:]*3)

    