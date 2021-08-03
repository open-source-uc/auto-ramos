from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import getpass

print('¡Bienvenide a auto-ramos UC, el tomador de ramos automatico de la universidad!\n')
print('FUNCIONAMIENTO:\n')
print('Primero tendras que ingresar tu usuario y contraseña UC, luego ingresaras tus NRC a tomar y apretaras ENTER cuando sea tu hora de banner\n')
print('Porfavor, ingresa tu usuario UC y contraseña: \n')
usuario = input('Usuario: ')
password = getpass.getpass('Contraseña: ')
NRC = input('Codigos NRC (Separados por un espacio) (AQUI ES CUANDO APRETAS ENTER CUANDO SEA TU HORA): ')
NRC = NRC.split(" ")

driver = webdriver.Firefox()
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
agregarbutton = driver.find_element_by_xpath('/html/body/div[3]/table[2]/tbody/tr[2]/td[2]/a')
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
