from PyQt5.QtCore import QObject
from threading import Thread
from PyQt5.QtCore import pyqtSignal
import twillmain


class Usuario:

    def __init__(self) -> None:
        self.username = ""
        self.password = ""
        self.nrcs_list = []


class Logica(QObject):

    login_signal = pyqtSignal(list)
    show_nrc_signal = pyqtSignal(str)
    # color: rgb(0, 85, 0); --> El color verde bueno =)

    def __init__(self, login_window, main_window):
        super().__init__()
        self.time = '00:00'
        self.usuario = Usuario()
        self.main_window = main_window
        self.login_window = login_window
        self.login_signal.connect(self.verify_login)
        self.thread_reservar = None

    def verify_login(self, credenciales):
        respuesta = twillmain.verificar_sesion(*credenciales)
        if respuesta[0]:
            self.usuario.username, self.usuario.password = [credenciales[0],
                                                            credenciales[1]]
            self.login_window.switch_window_signal.emit()
        else:
            self.login_window.failed_login_signal.emit(respuesta[1])

    def add_nrc(self, nrc):
        '''
        Revisar:
        - Que NRCs no se repitan
        - Que sean numericos y válidos
        '''
        self.usuario.nrcs_list.append(str(nrc))
        print(f"Backend DEBUG: Se ha añadido el nrc {nrc} de pana!")
        print(self.usuario.nrcs_list)
        self.show_nrc_signal.emit(nrc)

    def del_nrc(self, nrc):
        try:
            self.usuario.nrcs_list.remove(str(nrc))
            print(f"Backend DEBUG: Se ha ELIMINADO el nrc {nrc} de pana!")
            print(self.usuario.nrcs_list)
        except Exception as error:
            print("Warning: Se intentó eliminar un nrc no existente!")

    def request_time(self, time):
        self.time = time
        self.thread_reservar = Thread(target=self.reservar)
        self.thread_reservar.start()

    def reservar(self):
        twillmain.reservar(
            self.usuario.username, self.usuario.password,
            self.usuario.nrcs_list, self.time
        )
