#Pide 4 números y añádelos a una lista. Después, rota los elementos y guárdalos en una nueva lista (el último es el primero, etc.), mostrando por pantalla esta nueva lista.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))
num4 = int(input("Introduce el cuarto número: "))
lista = [num1, num2, num3, num4]

#Recorremos la lista y la guardamos en una nueva lista
lista2 = []
for i in range(len(lista)):
    lista2.append(lista[i])

#Rota los elementos de la lista
lista2.insert(0, lista2.pop())

print("La lista original es: ", lista)
print("La lista rotada es: ", lista2)