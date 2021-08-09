import sys

from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QApplication

from frontend.login_window import LoginWindow
from frontend.main_window import MainWindow

class MainWidget(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.login_window = LoginWindow()
        self.main_window = MainWindow() 

        self.addWidget(self.login_window)
        self.addWidget(self.main_window)

def hook(type_error, traceback):
    print(type_error)
    print(traceback)


if __name__ == '__main__':

    sys.__excepthook__ = hook
    app = QApplication([])
    main_widget = MainWidget()

    main_widget.show()
    sys.exit(app.exec())
