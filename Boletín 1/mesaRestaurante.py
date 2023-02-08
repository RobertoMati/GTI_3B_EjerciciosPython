#Otra persona y tú queréis reservar mesa en un restaurante. Queremos un programa que nos pregunte el estilo de vestir nuestro y el de nuestro compañero, que serán valores entre 0 y 10. 
#Si uno de los dos tenemos un estilo de 8 o superior, entonces sí que tendremos mesa para cenar y deberá mostrar un mensaje por pantalla. 
# Esto es así siempre y cuando uno de los dos no tenga un 2, en cuyo caso no tendremos mesa. En cualquier otro caso, el mensaje que debe mostrar es que no sabemos si tendremos mesa.
a = int(input("Introduce el estilo de vestir de la persona 1: "))
b = int(input("Introduce el estilo de vestir de la persona 2: "))
if a >= 8 or b >= 8:
    if a == 2 or b == 2:
        print("No tendréis mesa")
    else:
        print("Tendréis mesa")

elif a == 2 or b == 2:
    print("No tendréis mesa")
else:
    print("No sabemos si tendréis mesa")