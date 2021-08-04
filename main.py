from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import getpass
import schedule

print('¡Bienvenide a auto-ramos UC, el tomador de ramos automatico de la universidad!\n')
print('FUNCIONAMIENTO:\n')
print('Primero tendras que ingresar tu usuario y contraseña UC, luego ingresaras tus NRC a tomar y ingresaras a que hora quieres tomar ramos.')
print('NO CIERRES EL PROGRAMA HASTA TU TOMA DE RAMOS\n')
sistema = input('¿Cual es tu sistema operativo? (windows/linux): ')
while True:
    if sistema == 'windows' or sistema == 'linux':
        break
    sistema = input('¿Cual es tu sistema operativo? (windows/linux): ')
print('\n')
print('Porfavor, ingresa tu usuario UC y contraseña: \n')
usuario = input('Usuario: ')
password = getpass.getpass('Contraseña: ')
NRC = input('Codigos NRC (Separados por un espacio) (AQUI ES CUANDO APRETAS ENTER CUANDO SEA TU HORA): ')
NRC = NRC.split(" ")
hora = input('Ingresa la hora a la que tomaras ramos en formato 24hrs (Ej: 17:00): ')
print('\n')
print('Toma agendada...')


def main():
    global usuario
    global password
    global NRC
    global sistema
    if sistema == 'linux':
        driver = webdriver.Firefox(executable_path='geckodriver')
    elif sistema == 'windows':
        driver = webdriver.Firefox(executable_path='geckodriver.exe')
    driver.get('https://ssb.uc.cl/ERPUC/twbkwbis.P_WWWLogin')
    # Inicio de sesion
    usuariobox = driver.find_element_by_xpath('//*[@id="UserID"]')
    passwordbox = driver.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[2]/td[2]/input')
    loginbutton = driver.find_element_by_xpath('/html/body/div[3]/form/p/input')
    usuariobox.send_keys(usuario)
    passwordbox.send_keys(password)
    loginbutton.click()
    time.sleep(1)
    # Ingreso a pagina NRC
    try:
        agregarbutton = driver.find_element_by_xpath('/html/body/div[3]/table[2]/tbody/tr[2]/td[2]/a')
    except:
        driver.close()
        print('Usuario o contraseña incorrecta, favor intentar denuevo')
        usuario = input('Usuario: ')
        password = getpass.getpass('Contraseña: ')
        main()
    agregarbutton.click()
    time.sleep(1)
    enviarbutton = driver.find_element_by_xpath('/html/body/div[3]/form/input')
    enviarbutton.click()
    time.sleep(1)
    seleccionarlist = driver.find_element_by_xpath('//*[@id="st_path_id"]')
    seleccionarlist = Select(seleccionarlist)
    seleccionarlist.select_by_index(1)
    enviarplan = driver.find_element_by_xpath('/html/body/div[3]/form/input[19]')
    enviarplan.click()
    time.sleep(1)
    # Ingreso a plataforma de ramos
    i = 1
    while i <= 3:
        if i == 1:
            nrc1 = driver.find_element_by_xpath('//*[@id="crn_id1"]')
            nrc1.send_keys(NRC[0])
        elif i == 2 and len(NRC) >= 2:
            nrc2 = driver.find_element_by_xpath('//*[@id="crn_id2"]')
            nrc2.send_keys(NRC[1])
        elif i == 3 and len(NRC) == 3:
            nrc3 = driver.find_element_by_xpath('//*[@id="crn_id3"]')
            nrc3.send_keys(NRC[2])
        i += 1
    enviarcambios = driver.find_element_by_xpath('/html/body/div[3]/form/input[19]')
    enviarcambios.click()


schedule.every().day.at(hora).do(main)
while True:
    schedule.run_pending()
    time.sleep(1)
