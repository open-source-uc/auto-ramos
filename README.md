# auto-ramos
Tomador de ramos automatico. (Por ahora solo funciona en Linux)

## Funcion
Este script de Python tiene como principal objetivo hacer que la toma de ramos sea rapida y segura, donde el usuario solo debe ingresar sus
credenciales UC y los 3 NRC que quiere tomar, automaticamente se logeara y se tomaran los 3 NRC.

## Modulos/Paquetes requeridos

- Python 3.8
- Selenium
- Firefox Webdriver (https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)
- Schedule

## ¿Como instalar?

1. Instalar Selenium: `pip install selenium`
2. Descargar la version del driver Firefox Webdriver (https://github.com/mozilla/geckodriver/releases)
3. Colocar 'geckodriver' en el mismo directorio que main.py

## ¿Como ejecutar?

1. Simplemente ejecutar con `python main.py`