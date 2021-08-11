from frontend.login_window import LoginWindow
from frontend.ramos_window import RamosWindow
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QApplication
import params
import sys


class MainWidget(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.login_window = LoginWindow()
        self.main_window = RamosWindow()

        self.addWidget(self.login_window)
        self.addWidget(self.main_window)

        self.setWindowTitle('Login')
        self.setFixedSize(*params.SIZE_LOGIN_WINDOW)
        self.login_window.switch_window_signal.connect(self.switch_windows)

    def switch_windows(self):
        print("Switching windows...")
        self.setCurrentIndex(1)
        self.setFixedSize(*params.SIZE_RAMOS_WINDOW)
        self.setWindowTitle('Auto-Ramos V. ' + params.VERSION)


def hook(type_error, traceback):
    print(type_error)
    print(traceback)


if __name__ == '__main__':

    sys.__excepthook__ = hook
    app = QApplication([])
    main_widget = MainWidget()
    main_widget.show()
    sys.exit(app.exec())
