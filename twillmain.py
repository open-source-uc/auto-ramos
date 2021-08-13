from twill.commands import *
import schedule
from functions import obtener_errores_de

avance = 0


def main():
    # Ingresar usuario y contraseña
    print("¡NO CIERRES EL PROGRAMA HASTA QUE ESTE TOME RAMOS Y TE CONFIRME!\n")
    usuario = input("Usuario UC: ")
    password = input("Contraseña UC: ")
    chequeo = verificar_sesion(usuario, password)
    if chequeo[0] is False:
        exit()
    NRC = input("NRC (Separados por un espacio, Ej: 1234 1234 1234): ")
    NRC = NRC.split()
    hora = input("Ingresa la hora en formato 24 hrs (Ej: 08:00 o 16:00): ")
    if hora == 'debug':
        tomar_ramos(usuario, password, NRC)
    print('\n¡Toma agendada! ¡Recuerda no cerrar el programa hasta que este te confirme que tomo tus ramos!')
    reservar(usuario, password, NRC, hora)


def tomar_ramos(usuario, password, NRC):  # Esto debe ser de una corrida ya que usa Sessions
    # Ya logeado, printea que va a tomar ramos y redirige el output
    global avance
    avance = 16
    print('\nTomando ramos...')
    redirect_output('output.log')

    # Ingresar a Menu Principal
    go("http://ssb.uc.cl/ERPUC/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu")
    avance = 32

    # Ingresar a seleccionar periodo
    go("http://ssb.uc.cl/ERPUC/bwskfreg.P_AltPin")
    a = showforms()
    semestre = a[1].fields['term_in']
    avance = 48

    # Seleccionar ultimo semestre
    fv('2', 'term_in', semestre)
    submit('0')
    avance = 64

    # Seleccionar primer plan de estudio
    b = showforms()
    plan = b[1].get_element_by_id('st_path_id').value_options
    fv('2', 'st_path', plan[1])
    submit('0')
    avance = 80

    # go('http://localhost:3000/posts/13')
    # c = showforms()
    # Borrar NRC
    # NRC = c[1].fields['CRN_IN']
    # print(NRC)
    # print("-"*40)
    # retiro = c[1].get_element_by_id('action_id1').value_options
    # fv('2', 17, retiro[1])

    # Aplicar NRC
    if len(NRC) == 1:
        fv('2', 95, NRC[0])
    elif len(NRC) == 2:
        fv('2', 95, NRC[0])
        fv('2', 100, NRC[1])
    elif len(NRC) == 3:
        fv('2', 95, NRC[0])
        fv('2', 100, NRC[1])
        fv('2', 105, NRC[2])
    submit(submit_button=112)
    reset_output()
    avance = 100
    print('\n¡Ramos tomados! Ya puedes cerrar el programa... (Recuerda revisar el archivo \'pruebadetoma.html\' para verificar errores')
    save_html('pruebadetoma.html')
    print(obtener_errores_de('pruebadetoma.html'))
    exit()


def reservar(usuario, password, NRC, hora):
    try:
        schedule.every().day.at(hora).do(tomar_ramos, usuario=usuario, password=password, NRC=NRC)
        while True:
            schedule.run_pending()
    except:
        print('Formato de hora invalido, recuerda ingresarlo en 24hrs')


def verificar_sesion(usuario, password) -> tuple:
    # (True/False, Razón)
    print('\nChequeando credenciales...')
    redirect_output('output.log')
    go('https://ssb.uc.cl/ERPUC/twbkwbis.P_WWWLogin')
    formclear('1')
    fv('1', 'sid', usuario)
    fv('1', 'PIN', password)
    submit('0')
    go("http://ssb.uc.cl/ERPUC/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu")
    reset_output()
    try:
        find('Agregar o Eliminar Clases')
        print('¡Credenciales aceptadas!')
        return(True, '¡Credenciales aceptadas!')
    except:
        print('Credenciales rechazadas, porfavor intenta nuevamente')
        return(False, 'Credenciales rechazadas, porfavor intenta nuevamente')


if __name__ == '__main__':
    main()
