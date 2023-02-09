#Crea una función llamada get_minimum que dado una lista de números,devuelva el valor mínimo encontrado el dicho array. 

def get_minimum(lista):
    minimo = lista[0]
    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
    return minimo

res = get_minimum([5,6,2,8,9,10])
print(res)
