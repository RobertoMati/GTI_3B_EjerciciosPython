#Realiza un programa que pregunte por un día de la semana y si estamos o no de vacaciones. 
# El programa deberá mostrar un mensaje indicando a qué hora nos suena la alarma. Entre semana, la alarma sonará a las 8:00 y los fines de semana a las 10:00. 
# Sin embargo, si estamos de vacaciones, los días entre semana sonará a las 10:00 y los fines de semana estará apagada.

dia = input("Introduce un día de la semana: ")
vacaciones = input("¿Estoy de vacaciones? Escribe 'S' si es así o 'N' si no: ")

if vacaciones == "S":
    if dia == "sábado" or dia == "domingo" or dia == "sabado":
        print("La alarma está apagada")
    else:
        print("La alarma suena a las 10:00")
else:
    if dia == "sábado" or dia == "domingo" or dia == "sabado":
        print("La alarma suena a las 10:00")
    else:
        print("La alarma suena a las 8:00")