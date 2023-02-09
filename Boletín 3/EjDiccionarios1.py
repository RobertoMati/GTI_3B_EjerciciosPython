#Escribe una función que reciba dos diccionarios con claves de tipo string y valores de tipo numérico, 
#y que devuelva un nuevo diccionario que contenga los dos anteriores. Muestra el resultado por pantalla.

def mezclaDiccionarios(diccionario1, diccionario2):
    diccionario3 = {}
    diccionario3.update(diccionario1)
    diccionario3.update(diccionario2)
    return diccionario3

diccionario1 = {"uno":1, "dos":2, "tres":3}
diccionario2 = {"cuatro":4, "cinco":5, "seis":6}
diccionario3 = mezclaDiccionarios(diccionario1, diccionario2)
print(diccionario3)