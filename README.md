# auto-ramos v2.0
Tomador de ramos UC automatico para Windows, Linux y macOS

## Funcion
Este script de Python tiene como principal objetivo hacer que la toma de ramos sea rapida y segura, donde el usuario solo debe ingresar sus
credenciales UC y los NRC que quiere tomar, automaticamente se logeara y se tomaran los NRC a la hora que el usuario fije.

## IMPORTANTE

- Intentar no usar el computador a la hora de tomar ramos
- Este programa toma solo el primer plan de estudios de la persona, osea, no utilizar si tienes más de un plan de estudios

## Librerias/Paquetes/Programas requeridos

- Python 3.8
- twill
- schedule

## ¿Como instalar?

1. Instalar twill: `pip install twill`
2. Instalar schedule: `pip install schedule`
3. Clonar la libreria `github clone https://github.com/open-source-uc/auto-ramos.git`

## ¿Como ejecutar?

1. Simplemente ejecutar con `python twillmain.py`