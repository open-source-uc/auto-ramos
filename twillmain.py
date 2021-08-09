from twill.commands import *


# Ingresar usuario y contraseña
usuario = input("Usuario: ")
password = input("Contraseña: ")


def save_response(respuesta):
    html = respuesta
    with open("respuesta2.html", "w") as archivo_respuesta:
        archivo_respuesta.write(html)
    print("Se ha guardado respuesta2.html correctamente")


GET_URL = "http://ssb.uc.cl/ERPUC/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu"
POST_URL = "http://ssb.uc.cl/ERPUC/twbkwbis.P_ValLogin"

go('https://ssb.uc.cl/ERPUC/twbkwbis.P_WWWLogin')
formclear('1')
fv('1', 'sid', usuario)
fv('1', 'PIN', password)
showforms()
submit('0')
go("http://ssb.uc.cl/ERPUC/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu")
showlinks()
go("http://ssb.uc.cl/ERPUC/bwskfreg.P_AltPin")
showforms()
fv('2', 'term_in', '202122')
submit('0')

save_response(show())
showlinks()