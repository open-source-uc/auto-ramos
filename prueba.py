# Datos: fdsmith, !Password1!
import json
import urllib3

POST_URL = "http://ssb.uc.cl/ERPUC/twbkwbis.P_ValLogin"
GET_URL = "http://ssb.uc.cl/ERPUC/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu"

usuario = "fdsmith"
password = "!Password1!"


def save_response(respuesta):
    html = respuesta.data
    with open("respuesta2.html", "wb") as archivo_respuesta:
        archivo_respuesta.write(html)
    print("Se ha guardado respuesta2.html correctamente")


def extraer_sessid(sessid_str):
    # Se asume que sessid_str es de la forma: SESSID={DATO}
    return sessid_str[sessid_str.find("=") + 1:]


payload = {
    "Host": "ssb.uc.cl",  # Estará bien forzarla  (?
    "Cookie": "TESTID=set"
    }
data = "sid=" + usuario + "&PIN=" + password


http = urllib3.PoolManager()
r = http.request(
    'POST',
    POST_URL,
    headers=payload,
    body=data.encode("utf-8")
)
sessid = extraer_sessid(r.getheaders()["Set-Cookie"])
print(sessid)





