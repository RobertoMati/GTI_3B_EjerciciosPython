#Realiza un programa que pregunte tres valores enteros y muestre un mensaje por pantalla indicando si los dos primeros tienen una diferencia máxima de 1 
# mientras que el tercero tiene una diferencia mayor que 2 con los otros dos. Utiliza la función abs(sum) para calcular el valor absoluto de un número.

a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
c = int(input("Introduce el tercer número: "))
if abs(a-b) <= 1 and abs(a-c) > 2 and abs(b-c) > 2:
    print ("Los dos primeros números tienen una diferencia máxima de 1 y el tercer número tiene una diferencia mayor que 2 con los otros dos.")
    print ("La diferencia entre el primer y segundo número es: ", abs(a-b))
    print ("La diferencia entre el primer y tercer número es: ", abs(a-c))
    print ("La diferencia entre el segundo y tercer número es: ", abs(b-c))
else:
    print ("No se cumple la condición especificada.")
    print ("La diferencia entre el primer y segundo número es: ", abs(a-b))
    print ("La diferencia entre el primer y tercer número es: ", abs(a-c))
    print ("La diferencia entre el segundo y tercer número es: ", abs(b-c))