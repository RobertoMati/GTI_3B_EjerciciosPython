#Modifica el siguiente código para que repita sólo los 3 primeros caracteres del string. 
"""palabra = input("Introduce una palabra: ")
n = int(input("Introduce un número: "))
if n > 0:
    for i in range(n):
        print(palabra, end=", ")
else:
    print("El número introducido es no es válido.")

"""
#La longitud mínima del string será de 3, si no, el programa mostrará un mensaje y terminará.

palabra = input("Introduce una palabra: ")
n = int(input("Introduce un número: "))
if n > 0:
    if len(palabra) >= 3:
        for i in range(n):
            print(palabra[0:3], end=", ")
    else:
        print("La palabra introducida no tiene la longitud mínima.")
else:
    print("El número introducido es no es válido.")


