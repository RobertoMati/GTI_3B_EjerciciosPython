#Crea una función llamada without_first_letter que dada una lista de palabras, devuelva una nueva lista con la primera letra de cada palabra eliminada.

def without_first_letter(lista):
    lista2 = []
    for i in lista:
        lista2.append(i[1:])
    return lista2

lista = ["hola", "adios", "buenos dias"]
print(without_first_letter(lista))
