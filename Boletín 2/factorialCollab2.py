#Realiza un programa para calcular el factorial de un número entero introducido por el teclado (sin utilizar la librería). 

numero = int(input("Introduce un número entero: "))
factorial = 1
#El range es así porque
for i in range(factorial, numero+1):
    factorial = factorial * i
print("El factorial de", numero, "es", factorial)