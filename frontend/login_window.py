from PyQt5.QtWidgets import QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QMessageBox


class LoginWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()

    def init_ui(self) -> None:
        self.main_vbox = QVBoxLayout()
        self.setLayout(self.main_vbox)

        # LINEAS DE INGRESO DE NOMBRE Y CLAVE
        self.username_layout = QHBoxLayout()
        self.username_label = QLabel('Usuario:')
        self.username_box = QLineEdit()
        
        self.username_layout.addWidget(self.username_label)
        self.username_layout.addWidget(self.username_box)

        self.password_layout = QHBoxLayout()
        self.password_label = QLabel('Contraseña:')
        self.password_box = QLineEdit()

        # Asi la clave no se ve cuando la escribes
        self.password_box.setEchoMode(QLineEdit.Password)


        self.password_layout.addWidget(self.password_label)
        self.password_layout.addWidget(self.password_box)
        
        self.main_vbox.addLayout(self.username_layout)
        self.main_vbox.addLayout(self.password_layout)

        #Boton login
        self.login_button = QPushButton('Login')
        self.main_vbox.addWidget(self.login_button)


        self.invalid_session_popup = QMessageBox(self)
        self.invalid_session_popup.setWindowTitle('ERROR')
        self.invalid_session_popup.setText(
            "USUARIO O CONTRASEÑA INCORRECTAS")
        self.invalid_session_popup.setIcon(QMessageBox.Critical)

    def raise_popup(self):
        self.invalid_session_popup.exec_()
