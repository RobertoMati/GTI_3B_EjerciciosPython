#Dada una lista de enteros, muestra por pantalla si un número introducido por teclado está en la primera o en la última posición. 
# La longitud mínima de la lista será de 1, en caso contrario, el programa terminará.


#Crear lista random
import random
lista = []
for i in range(0,random.randint(1,10)):
    lista.append(random.randint(1,10))
print(lista)

#Pedir número
num = int(input("Introduce un número: "))
#Comprobar si está en la primera o última posición
if num == lista[0]:
    print("El número está en la primera posición")
elif num == lista[-1]:
    print("El número está en la última posición")
else:
    print("El número no está en la primera o última posición")
    