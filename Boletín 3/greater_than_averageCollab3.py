#Crea una función llamada greater_than_average que tome un parámetro x de tipo numérico, y una lista llamada data_array. 
#La función deberá devolver cierto en caso de que el valor x sea mayor que la media de la lista, y falso en caso contrario.

def greater_than_average(x, data_array):
    media = sum(data_array)/len(data_array)
    if x > media:
        return True
    else:
        return False

res = greater_than_average(6, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(res)