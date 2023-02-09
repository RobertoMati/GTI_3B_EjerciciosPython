#Crea una función llamada every_element_greater_than que tome por parámetro un número y una lista numérica y devuelva True si 
#todos los elementos son mayores que el número pasado por parámetro y False en caso contrario.

def every_element_greater_than(number, list):
    for i in list:
        if i <= number:
            return False
    return True

print(every_element_greater_than(5, [6, 3, 8, 9]))