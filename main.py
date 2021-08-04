import schedule
from time import sleep
from autoramos import AutoRamos

def main():

    print('¡Bienvenide a auto-ramos UC, el tomador de ramos automatico de la universidad!')
    print('Primero tendras que ingresar tu usuario y contraseña UC, luego ingresaras tus NRC a tomar y ingresaras a que hora quieres tomar ramos.')
    print('NO CIERRES EL PROGRAMA HASTA DESPUES DE TU TOMA DE RAMOS\n')

    print('Porfavor, ingresa tu usuario UC y contraseña: \n')
    usuario = input('Usuario: ')
    password = input('Contraseña: ')
    ramos = input('Codigos NRC (Separados por un espacio): ')
    ramos = ramos.split()
    hora = input('Ingresa la hora a la que tomaras ramos en formato 24hrs (Ej: 17:00 o 08:00): ')

    while True:
        if len(hora) == 5:
            break
        print('Formato de hora incorrecto, recuerda agregar un 0 en caso de que sea en la mañana, ejemplo 08:00 en vez de 8:00')
        hora = input('Ingresa la hora a la que tomaras ramos en formato 24hrs (Ej: 17:00 o 08:00): ')

    autoramos_ = AutoRamos(ramos, usuario, password)

    print('\n')
    print('Toma agendada, recuerda no apagar ni cerrar el programa hasta que ocurra tu toma de ramos y el programa confirme que tomo tus ramos...')

    schedule.every().day.at(hora).do(autoramos_.start)
    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == "__main__":
    main()
