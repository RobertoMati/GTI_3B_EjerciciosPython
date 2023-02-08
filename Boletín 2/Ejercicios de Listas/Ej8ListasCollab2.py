#Dada una lista de enteros, mostrar por pantalla si hay algún número que esté repetido en dos posiciones consecutivas.

lista = [1,2,3,4,5,6,8,8,9,10,11,12,13,14,16,17,18,19,20]

for i in range(len(lista)-1):
    if lista[i] == lista[i+1]:
        print("El número", lista[i], "está repetido en dos posiciones consecutivas")

