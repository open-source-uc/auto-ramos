from twill.commands import *
import schedule

# Ingresar usuario y contraseña
print("¡NO CIERRES EL PROGRAMA HASTA QUE ESTE TOME RAMOS Y TE CONFIRME!\n")
usuario = input("Usuario UC: ")
password = input("Contraseña UC: ")
NRC = input("NRC (Separados por un espacio, Ej: 1234 1234 1234): ")
NRC = NRC.split()
hora = input("Ingresa la hora en formato 24 hrs (Ej: 08:00 o 16:00): ")
print('\n¡Toma agendada! ¡Recuerda no cerrar el programa hasta que este te confirme que tomo tus ramos!')


def main():
    global usuario
    global password
    global NRC
    # Logearse
    print('\nTomando ramos...')
    redirect_output('output.log')
    go('https://ssb.uc.cl/ERPUC/twbkwbis.P_WWWLogin')
    formclear('1')
    fv('1', 'sid', usuario)
    fv('1', 'PIN', password)
    submit('0')

    # Ingresar a Menu Principal
    go("http://ssb.uc.cl/ERPUC/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu")

    # Ingresar a seleccionar periodo
    go("http://ssb.uc.cl/ERPUC/bwskfreg.P_AltPin")
    a = showforms()
    # print("*")
    # print(a[1].fields.keys())
    semestre = a[1].fields['term_in']
    # print("*")

    # Seleccionar ultimo semestre
    fv('2', 'term_in', semestre)
    submit('0')

    # Seleccionar primer plan de estudio
    b = showforms()
    plan = b[1].get_element_by_id('st_path_id').value_options
    fv('2', 'st_path', plan[1])
    submit('0')

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
    print('\n¡Ramos tomados! Ya puedes cerrar el programa...')
    save_html('pruebadetoma.html')


schedule.every().day.at(hora).do(main)
while True:
    schedule.run_pending()
