#Escribe un programa que, dado un string y un valor n no negativo, muestre por pantalla el string repetido n veces con una coma y un espacio entre cada repetición. Por ejemplo, si el string es "Hola" y el valor n es 3, el resultado debería ser "Hola, Hola, Hola". Si el valor n es 0, el resultado debería ser vacío.

palabra = input("Introduce una palabra: ")
n = int(input("Introduce un número: "))
if n > 0:
    for i in range(n):
        print(palabra, end=", ")
else:
    print("El número introducido es no es válido.")

