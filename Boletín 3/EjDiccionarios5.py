#Escribe una función que reciba el siguiente diccionario:
"""# 
{
 1 : {'id': 1, 
 'success': True, 
 'name': 'Lary'
 }, 
 2 : {'id': 2, 
 'success': False, 
 'name': 'Rabi'
 }, 
 3 : {'id': 3, 
 'success': True, 
 'name': 'Alex'
 }
}
# """
#  y cuente la cantidad de items que tienen True el campo success:

def contar(diccionario):
    contador = 0
    for i in diccionario:
        if diccionario[i]['success'] == True:
            contador += 1
    return contador

diccionario = {
 1 : {'id': 1, 
 'success': True, 
 'name': 'Lary'
 }, 
 2 : {'id': 2, 
 'success': False, 
 'name': 'Rabi'
 }, 
 3 : {'id': 3, 
 'success': True, 
 'name': 'Alex'
 }
}

print(contar(diccionario))