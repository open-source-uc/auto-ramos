import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
      super().__init__()
      self.initUI()

    def initUI(self):
      self.statusBar().showMessage("Ready")

      self.setGeometry(300,300,250,150)
      self.setWindowTitle('Auto-Ramos')
      self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.exit(app.exec_())
