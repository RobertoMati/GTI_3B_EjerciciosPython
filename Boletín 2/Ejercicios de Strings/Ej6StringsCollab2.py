#Dados dos strings, muestra por pantalla la cantidad de veces que el segundo string aparece en el primero.

palabra1 = input("Introduce una palabra: ")
palabra2 = input("Introduce otra palabra: ")

print("La palabra", palabra2, "aparece", palabra1.count(palabra2), "veces en la palabra", palabra1)

