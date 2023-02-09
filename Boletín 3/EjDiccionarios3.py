#Escribe una función que reciba un diccionario de valores numéricos y devuelva el valor mínimo de este diccionario. Muestra el resultado por pantalla.

def minimo(diccionario):
    minimo = diccionario[1]
    for i in diccionario:
        if diccionario[i] < minimo:
            minimo = diccionario[i]
    return minimo

diccionario = {1: 80, 2: 60, 3: 30, 4: 20, 5: 50}
print(minimo(diccionario))