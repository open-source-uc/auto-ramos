from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore
from PyQt5 import uic
import twillmain
import params
import sys
import os

window_name, base_class = uic.loadUiType(params.PATH_RAMOS_WINDOW)


class RamosWindow(window_name, base_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        '''
        Elementos gráficos y configuración adicional
        '''
        self.nrc_frames = {
            "1": self.nrc_frame_1,
            "2": self.nrc_frame_2,
            "3": self.nrc_frame_3
        }
        self.ramos_labels = {
            "1": [
                self.label_ramo_tit_1, self.label_ramo_1,
                self.eliminar_button_1
            ],
            "2": [
                self.label_ramo_tit_2, self.label_ramo_2,
                self.eliminar_button_2
            ],
            "3": [
                self.label_ramo_tit_3, self.label_ramo_3,
                self.eliminar_button_3
            ]
        }
        for nrc_layout in list(self.nrc_frames.values())[1:]:
            nrc_layout.hide()
        for tit, label, eliminar_button in list(self.ramos_labels.values()):
            tit.hide()
            label.hide()
            eliminar_button.hide()

        self.confirmar_button_1.clicked.connect(lambda:
                                                self.show_nrc_layout("2"))
        self.confirmar_button_2.clicked.connect(lambda:
                                                self.show_nrc_layout("3"))
        self.confirmar_button.clicked.connect(lambda: print("Holi"))

    def show_nrc_layout(self, id_):
        self.nrc_frames[id_].show()

    def show_confirmed_nrc(self, nrc):
        '''
        - Se debe elegir el label de menor índice para mostrar el nuevo ramo
        - Se asume que habrá al menos una label oculta para mostrar
        '''
        labels = []
        for label_list in self.ramos_labels.values():
            if label_list[0].isVisible():
                labels = label_list
        labels[1].setText(nrc)
        labels[0].show()
        labels[1].show()

    def del_confirmed_nrc(self, id_):
        labels = self.ramos_labels[id_]
        labels[0].hide()
        labels[1].hide()


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = RamosWindow()
    ventana.show()
    app.exec()
