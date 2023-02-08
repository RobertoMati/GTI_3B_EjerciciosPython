#Se nos ha solicitado programar el calculador de la tarifa a pagar por los usuarios de una compañía de telefonía móvil. Todos los usuarios pagan una tarifa base de 10 euros al mes siempre que no hablen más de 180 minutos al mes. A partir de los 180 minutos, los usuarios pagan 10 céntimos por cada minuto hablado desde los 180 hasta los 240 minutos. A partir de ese momento, los usuarios pagan 20 céntimos por cada minuto por cada minuto extra consumido a partir de los 240. El calculador debe pedir al usuario los minutos hablados y devolver los euros a pagar.
a = int(input("Introduce los minutos hablados: "))
if a <= 180:
    print("La tarifa a pagar es de 10€")
elif a > 180 and a <= 240:
    print("La tarifa a pagar es de", (a - 180) * 0.1 + 10, "€")
else:
    print("La tarifa a pagar es de", (a - 240) * 0.2 + 10 + 6, "€")
    