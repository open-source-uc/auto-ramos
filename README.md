# auto-ramos
Tomador de ramos automatico para Windows y Linux

## Funcion
Este script de Python tiene como principal objetivo hacer que la toma de ramos sea rapida y segura, donde el usuario solo debe ingresar sus
credenciales UC y los NRC que quiere tomar, automaticamente se logeara y se tomaran los NRC a la hora que el usuario fije.

## Modulos/Paquetes/Programas requeridos

- Python 3.8
- Selenium
- Firefox Webdriver (https://github.com/mozilla/geckodriver/releases)
- Schedule
- Firefox

## ¿Como instalar?

1. Instalar Selenium: `pip install selenium`
2. Instalar Schedule: `pip install schedule`
3. Instalar Firefox: https://www.mozilla.org/es-CL/firefox/new/
4. Clonar el repositorio `git clone https://github.com/open-source-uc/auto-ramos`

## ¿Como ejecutar?

1. Simplemente ejecutar con `python main.py`