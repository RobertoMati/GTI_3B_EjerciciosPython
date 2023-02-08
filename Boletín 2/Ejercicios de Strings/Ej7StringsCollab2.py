#Dados dos strings, muestra por pantalla un mensaje indicando si uno de los dos aparece al final del otro, ignorando diferencias de mayúsculas y minúsculas. 
# Por ejemplo, el string "AbC" y "HiaBc" debería mostrar que si que aparece uno al final del otro.

palabra1 = input("Introduce una palabra: ")
palabra2 = input("Introduce otra palabra: ")

if palabra1.lower().endswith(palabra2.lower()):
    print("La palabra", palabra1, "acaba con", palabra2)
elif palabra2.lower().endswith(palabra1.lower()):
    print("La palabra", palabra2, "acaba con", palabra1)
else:
    print("Ninguna de las palabras acaba con la otra")