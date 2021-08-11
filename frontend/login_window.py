from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QMessageBox
import params
from PyQt5 import uic

window_name, base_class = uic.loadUiType(params.PATH_LOGIN_WINDOW)


class LoginWindow(window_name, base_class):

    switch_window_signal = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self) -> None:
        self.invalid_session_popup = QMessageBox(self)
        self.invalid_session_popup.setWindowTitle('ERROR')
        self.invalid_session_popup.setText(
            "USUARIO O CONTRASEÑA INCORRECTAS")
        self.invalid_session_popup.setIcon(QMessageBox.Critical)

        self.login_button.clicked.connect(self.switch_window)
        self.mostrar_clave_checkbox.stateChanged.connect(self.show_password)

    def show_password(self):
        if self.mostrar_clave_checkbox.isChecked():
            self.password_box.setEchoMode(QLineEdit.Normal)
        else:
            self.password_box.setEchoMode(QLineEdit.Password)

    def raise_popup(self):
        self.invalid_session_popup.exec_()

    def switch_window(self):
        self.switch_window_signal.emit()
