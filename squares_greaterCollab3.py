#Crea una función llamada squares_greater que dada una lista de números, devuelva una nueva lista con los cuadrados de aquellos números mayores que 10.
def squares_greater(list):
    new_list = []
    for i in list:
        if i > 10:
            new_list.append(i**2)
    return new_list

#---------------------Pruebas---------------------
print(squares_greater([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
