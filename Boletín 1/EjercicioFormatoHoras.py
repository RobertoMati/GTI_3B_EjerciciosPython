#Implementa un programa que lea la hora en formato 24 horas y lo convierta a formato 12 horas. 
a = int(input("Introduce la hora "))
b = int(input("Introduce los minutos "))
c = int(input("Introduce los segundos "))


if 24> a > 12:
    a = a - 12
    print("La hora es ", a, ":", b, ":", c, "PM")

elif a>24:
    print("La hora no es correcta")

else:
    print("La hora es ", a, ":", b, ":", c, "AM")


