#Crea una función llamada clean_list que tome una lista de nombres 
#de usuarios y una lista de nombres de usuarios baneados y devuelva una nueva lista con los usuarios no baneados.

def clean_list(list1, list2):
    for i in list2:
        if i in list1:
            list1.remove(i)
    return list1

lista1 = ["Marta", "Juan", "Roberto", "Luis", "Ana", "Maria"]
lista2 = ["Juan", "Ana"]

print(clean_list(lista1, lista2))