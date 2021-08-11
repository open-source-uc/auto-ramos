from PyQt5.QtCore import QObject


class Usuario:

    def __init__(self) -> None:
        self.username = ""
        self.password = ""


class Logica(QObject):

    def __init__(self):
        super().__init__()
        self.nrcs_list = []

    def add_nrc(self, nrc):
        self.nrcs_list.append(str(nrc))

    def del_nrc(self, nrc):
        self.nrcs_list.remove(str(nrc))
