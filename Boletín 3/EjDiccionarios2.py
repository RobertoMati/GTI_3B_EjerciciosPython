#Escribe una función que reciba un diccionario y una lista de palabras. La función debe devolver un nuevo diccionario con los items del diccionario cuyas 
#claves correspondan a alguna de las palabras de la lista. Muestra el resultado por pantalla.

def DiccionarioLista(diccionario,lista):
    diccionario2={}
    for i in lista:
        if i in diccionario:
            diccionario2[i]=diccionario[i]
    return diccionario2

diccionario={"uno":1,"dos":2,"tres":3,"cuatro":4,"cinco":5}
lista=["uno","tres","cinco"]
print(DiccionarioLista(diccionario,lista))
