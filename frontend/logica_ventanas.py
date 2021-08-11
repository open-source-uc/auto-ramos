from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal
import twillmain


class Usuario:

    def __init__(self) -> None:
        self.username = ""
        self.password = ""
        self.nrcs_list = []


class Logica(QObject):

    login_signal = pyqtSignal(list)

    def __init__(self, login_window, main_window):
        super().__init__()
        self.usuario = Usuario()
        self.main_window = main_window
        self.login_window = login_window
        self.login_signal.connect(self.verify_login)

    def verify_login(self, credenciales):
        respuesta = twillmain.verificar_sesion(*credenciales)
        if respuesta[0]:
            self.usuario.username, self.usuario.password = [credenciales[0],
                                                            credenciales[1]]
            self.login_window.switch_window_signal.emit()
        else:
            self.login_window.failed_login_signal.emit(respuesta[1])

    def add_nrc(self, nrc):
        self.nrcs_list.append(str(nrc))

    def del_nrc(self, nrc):
        self.nrcs_list.remove(str(nrc))
