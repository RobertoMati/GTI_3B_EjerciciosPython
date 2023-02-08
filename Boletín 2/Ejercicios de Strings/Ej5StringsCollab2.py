#Dado un string, muestra por pantalla un nuevo string que sea el original, repitiendo cada caracter dos veces.
#Ejemplo: "Hola" -> "HHeelllloo"

palabra = input("Introduce una palabra: ")
nueva_palabra = ""

for letra in palabra:
    nueva_palabra += letra * 2

print(nueva_palabra)