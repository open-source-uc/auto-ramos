# Auto-ramos v2.0
Tomador de ramos UC automatico para Windows, Linux y macOS

## Resumen
Este script de Python tiene como principal objetivo hacer que la toma de ramos sea rapida y segura, donde el usuario solo debe ingresar sus
credenciales UC y los NRC que quiere tomar, automaticamente se logeara y se tomaran los NRC a la hora que el usuario fije.

## IMPORTANTE

- Aunque tenemos casi certeza de que el programa funcionará y tomará los cupos más rápido que cualquier usuario humano en condiciones normales, se recomienda verificar de todas formas que los ramos se hayan tomado, ya que no podemos garantizarlo.
- Este programa toma solo el primer plan de estudios. Esto se mejorará en una versión futura

## Librerias/Paquetes/Programas requeridos

- Python 3.8
- twill
- schedule

## ¿Como instalar?

1. Instalar twill: `pip install twill`
2. Instalar schedule: `pip install schedule`
3. Clonar la libreria: `github clone https://github.com/open-source-uc/auto-ramos.git`

### Alternativamente puedes clonar primero el repositorio, y luego usar requirements.txt
1. Clonar la libreria: `github clone https://github.com/open-source-uc/auto-ramos.git`
2. Instalar twill y schedule: `pip install -r requirements.txt`

## ¿Como ejecutar?

### El programa se puede correr mediante la CLI (Usuarios avanzados) o mediante la interfaz gráfica
1. CLI: `python twillmain.py`
2. Interfaz gráfica: `python main.py`

## ¿Es seguro poner mi contraseña en su programa?

Absolutamente! La librería utilizada, twill, "simula" un navegador el cual se comunica directamente con el servicio de toma de ramos. El programa no cuenta con telemetría y no se nos transmite ningún dato. Esto es completamente verificable en el propio código de fuente.
