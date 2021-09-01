from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTime, QTimer, QThread
from PyQt5.QtCore import pyqtSignal
from threading import Thread
from PyQt5 import QtCore
from PyQt5 import uic
import twillmain
import params
import sys
import os


window_name, base_class = uic.loadUiType(params.PATH_RAMOS_WINDOW)


# class ThreadReserva(Thread):
# 
#     def __init__(self, reservar_signal, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.reservar_signal = reservar_signal
#         self.tiempo = "00:00"
# 
#     def run(self):
#         self.reservar_signal.emit(self.tiempo)


class RamosWindow(window_name, base_class):

    add_nrc_signal = pyqtSignal(str)
    del_nrc_signal = pyqtSignal(str)
    reservar_signal = pyqtSignal(str)
    cancelar_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        '''
        Elementos gráficos y configuración adicional
        '''
        # self.reservar_thread = ThreadReserva(self.reservar_signal)
        # self.reservar_thread.setInterval(100)
        # self.reservar_thread.setSingleShot(True)
        # self.reservar_thread.timeout.connect(self.send_time)
        self.timer_progressbar = QTimer(self)
        self.timer_progressbar.setInterval(100)
        self.timer_progressbar.timeout.connect(self.update_progressbar)
        # self.tiempo_progressbar.setValue(0)
        self.nrc_frames = {
            "1": self.nrc_frame_1,
            "2": self.nrc_frame_2,
            "3": self.nrc_frame_3
        }
        self.ramos_labels = [
            [
                self.label_ramo_tit_1, self.label_ramo_1,
                self.eliminar_button_1
            ],
            [
                self.label_ramo_tit_2, self.label_ramo_2,
                self.eliminar_button_2
            ],
            [
                self.label_ramo_tit_3, self.label_ramo_3,
                self.eliminar_button_3
            ]
        ]
        self.nrcs_lineedits = {
            "1": self.nrc_lineedit_1,
            "2": self.nrc_lineedit_2,
            "3": self.nrc_lineedit_3
        }
        for nrc_layout in list(self.nrc_frames.values())[1:]:
            nrc_layout.hide()
        for tit, label, eliminar_button in self.ramos_labels:
            tit.hide()
            label.hide()
            eliminar_button.hide()

        self.add_button_1.clicked.connect(lambda:
                                          self.show_nrc_layout("2"))
        self.add_button_1.clicked.connect(lambda:
                                          self.enable_confirmar_button(True))
        self.add_button_2.clicked.connect(lambda:
                                          self.show_nrc_layout("3"))
        self.add_button_1.clicked.connect(lambda:
                                          self.add_button_1.setEnabled(False))
        self.add_button_2.clicked.connect(lambda:
                                          self.add_button_2.setEnabled(False))
        self.add_button_3.clicked.connect(lambda:
                                          self.add_button_3.setEnabled(False))
        self.add_button_1.clicked.connect(lambda: self.add_nrc("1"))
        self.add_button_2.clicked.connect(lambda: self.add_nrc("2"))
        self.add_button_3.clicked.connect(lambda: self.add_nrc("3"))
        self.eliminar_button_1.clicked.connect(
            lambda: self.del_confirmed_nrc("1")
        )
        self.eliminar_button_2.clicked.connect(
            lambda: self.del_confirmed_nrc("2")
        )
        self.eliminar_button_3.clicked.connect(
            lambda: self.del_confirmed_nrc("3")
        )
        self.confirmar_button.setEnabled(False)
        self.confirmar_button.clicked.connect(self.reservar)
        self.cancelar_button.clicked.connect(self.cancel)

    def add_nrc(self, id_):
        nrc_nuevo = self.nrcs_lineedits[id_].text()
        self.add_nrc_signal.emit(nrc_nuevo)

    def enable_confirmar_button(self, enable):
        if enable:
            self.confirmar_button.setEnabled(True)
        else:
            self.confirmar_button.setEnabled(False)

    def show_nrc_layout(self, id_):
        self.nrc_frames[id_].show()

    def show_confirmed_nrc(self, nrc):
        '''
        - Se debe elegir el label de menor índice para mostrar el nuevo ramo
        - Se asume que habrá al menos una label oculta para mostrar
        '''
        labels = []
        for label_list in self.ramos_labels:
            if not label_list[0].isVisible():
                labels = label_list
                break
        labels[1].setText(nrc)
        labels[0].show()
        labels[1].show()
        labels[2].show()

    def del_confirmed_nrc(self, id_):
        labels = self.ramos_labels[int(id_) - 1]
        labels[0].hide()
        labels[1].hide()
        labels[2].hide()
        self.del_nrc_signal.emit(labels[1].text())
        if id_ == "1":
            self.add_button_1.setEnabled(True)
        elif id_ == "2":
            self.add_button_2.setEnabled(True)
        elif id_ == "3":
            self.add_button_3.setEnabled(True)

    def reservar(self):
        # Enviamos señal con el tiempo a request_time de logica ventana
        # self.reservar_thread.tiempo = self.timeEdit.time().toString()[:-3]

        hora = self.timeEdit.time().toString()[:-3]
        self.reservar_signal.emit(hora)

        print("Justo ANTES de ejecutar el thread")
        # self.reservar_thread.start()
        print("Justo DESPUÉS de ejecutar el thread")
        # print(self.timeEdit.time().toString()[:-3])
        # self.tiempo_progressbar.setValue(10)
        print("Justo ANTES de ejecutar el TIMER")
        # self.timer_progressbar.start()
        print("Justo DESPUÉS de ejecutar el TIMER")
        self.statusbar.showMessage('¡Toma de ramos agendada! Ahora solo espera'
                                   ' y mira la magia...', 10000)

    def update_progressbar(self):
        print("Debug: El avance es:")
        avance = twillmain.avance
        print(avance)
        # self.tiempo_progressbar.setValue(avance)
        self.update()
        if avance >= 100:
            self.timer_progressbar.stop()

    def send_time(self):
        print("Emitiendo la señal de enviar tiempo...")
        tiempo = self.timeEdit.time().toString()[:-3]
        self.reservar_signal.emit(tiempo)
        print("Emití la señal de enviar tiempo")

    def cancel(self):
        self.cancelar_signal.emit()
        self.timeEdit.setTime(QTime(0, 0, 0))
        for nrc_lineedit in self.nrcs_lineedits.values():
            nrc_lineedit.setText("")
        for nrc_layout in list(self.nrc_frames.values())[1:]:
            nrc_layout.hide()
        for id_ in range(1, 4):
            self.del_confirmed_nrc(str(id_))
        self.enable_confirmar_button(False)


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = RamosWindow()
    ventana.show()
    app.exec()
