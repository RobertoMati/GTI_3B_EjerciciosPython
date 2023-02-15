#Implementa un juego que genere un número entero aleatorio entre 1 y 100. Entonces, el usuario deberá introducir números por teclado para intentar adivinar el número generado.
#Cada vez que el usuario introduzca un número por teclado, el programa deberá determinar si el número es el generado inicialmente (ganando el usuario la partida), 
#si el número introducido por el usuario es múltiplo o divisor del número (informando de que el número introducido es múltiplo o divisor), o si no es ninguno de 
#los otros dos casos. Al final de la partida, el número de puntos obtenido por el usuario es 100 menos el número de intentos del usuario. La puntuación debe 
#imprimirse al final del juego.

import random
def numAleatorio():
    print("Juego de adivinar el número")
    print("**************************")
    print("Introduce un número entero entre 1 y 100")
    num = int(input("Introduce un número: "))
    numAleatorio = random.randint(1, 100)
    intentos = 0
    while num != numAleatorio:
        if num % numAleatorio == 0:
            print("El número introducido es múltiplo del número generado")
        elif numAleatorio % num == 0:
            print("El número introducido es divisor del número generado")
        else:
            print("El número introducido no es múltiplo ni divisor del número generado")
        num = int(input("Introduce un número: "))
        intentos = intentos + 1
    print("Has acertado el número generado")
    print("Puntuación: ", 100 - intentos)


numAleatorio()

