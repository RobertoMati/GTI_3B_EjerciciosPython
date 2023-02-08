#Calcular la cantidad de números impares que hay en una lista de enteros.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cont = 0
for i in lista:
    if i % 2 != 0:
        cont += 1
print("La cantidad de números impares es: ", cont)
