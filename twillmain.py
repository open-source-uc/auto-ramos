from twill.commands import *
import getpass
import time


# TODO: Agregar Schedule y ver como seleccionar plan de estudios
# Ingresar usuario y contraseña
usuario = input("Usuario: ")
password = input("Contraseña: ")
NRC = input("NRC (Separados por un espacio): ")
inicio = time.time()

# Logearse
go('https://ssb.uc.cl/ERPUC/twbkwbis.P_WWWLogin')
formclear('1')
fv('1', 'sid', usuario)
fv('1', 'PIN', password)
submit('0')

# Ingresar a Menu Principal
go("http://ssb.uc.cl/ERPUC/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu")

# Ingresar a seleccionar periodo
go("http://ssb.uc.cl/ERPUC/bwskfreg.P_AltPin")
fv('2', 'term_in', '202122')
submit('0')

save_html(filename="respuesta2.html")
print(time.time() - inicio)