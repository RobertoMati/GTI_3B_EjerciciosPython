#Dadas dos listas de longitudes diferentes, averiguar si el primero o el último elemento de ambas listas es el mismo. 
# En este caso, eliminar dicho elemento y mostrar las listas resultantes.


def ListasElementosPrimeroUltimoIguales():
    print("***************************************")
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lista2 = [1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print("La lista 1 original es: ", lista1)
    print("La lista 2 original es: ", lista2)
    print("***************************************")
    if lista1[0] == lista2[0]:
        lista1.pop(0)
        lista2.pop(0)
    elif lista1[-1] == lista2[-1]:
        lista1.pop(-1)
        lista2.pop(-1)

    print("***************************************")
    print("La lista 1 con la condición es: ", lista1)
    print("La lista 2 con la condición es: ", lista2)
    print("***************************************")

ListasElementosPrimeroUltimoIguales()