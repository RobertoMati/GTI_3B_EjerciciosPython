#Dada una lista de enteros, averiguar si el primer o el último elemento es el mayor y sustituir el resto de elementos por éste (sin contar el primero el último). 
# Por ejemplo, la lista [11, 5, 9, 7] debería quedar como [11, 11, 11, 7].


lista = [11, 5, 9, 7]
mayor = max(lista)
if lista[0] == mayor:
    for i in range(1, len(lista)-1):
        lista[i] = mayor
else:
    for i in range(1, len(lista)-1):
        lista[i] = mayor
print(lista)
