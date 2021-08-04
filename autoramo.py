import os
from selenium import webdriver
from time import sleep

class AutoRamos:
    drivers = {
            'nt': 'geckodriver.exe',
            'posix': 'geckodriver'}

    def __init__(self, ramos: list, usuario: str, clave: str) -> None:
        

        self.usuario = usuario
        self.clave = clave
        self.ramos = ramos

        self.os = os.name
        self.driver = None

        self.get_driver()
    
    def get_driver(self) -> None:
        try:
            driver_path = AutoRamos.drivers[self.os]
            self.driver = webdriver.Firefox(executable_path=driver_path)

        except KeyError as err:
            print('SISTEMA OPERATIVO NO SOPORTADO')
            print(err)

    def login(self) -> None:
        if self.driver:
            usuariobox = self.driver.find_element_by_xpath('//*[@id="UserID"]')
            passwordbox = self.driver.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[2]/td[2]/input')
            loginbutton = self.driver.find_element_by_xpath('/html/body/div[3]/form/p/input')

            usuariobox.send_keys(self.usuario)
            passwordbox.send_keys(self.clave)
            loginbutton.click()

            sleep(1)
