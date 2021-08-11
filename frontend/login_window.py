from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit,
    QMessageBox
)
import params
from PyQt5 import uic

window_name, base_class = uic.loadUiType(params.PATH_LOGIN_WINDOW)


class LoginWindow(window_name, base_class):

    switch_window_signal = pyqtSignal()
    login_request_signal = pyqtSignal(list)
    failed_login_signal = pyqtSignal(str)

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

        self.failed_login_signal.connect(self.raise_popup)
        self.login_button.clicked.connect(self.login)
        self.mostrar_clave_checkbox.stateChanged.connect(self.show_password)

    def show_password(self):
        if self.mostrar_clave_checkbox.isChecked():
            self.password_box.setEchoMode(QLineEdit.Normal)
        else:
            self.password_box.setEchoMode(QLineEdit.Password)

    def raise_popup(self, reason):
        self.invalid_session_popup.exec_()

    def login(self):
        credenciales = [self.username_lineedit.text(),
                        self.password_box.text()]
        self.login_request_signal.emit(credenciales)
