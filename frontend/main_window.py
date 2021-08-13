import sys

from PyQt5.QtWidgets import QApplication, QComboBox, QDateTimeEdit, QHBoxLayout, QLineEdit, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QDateTime
from collections import deque


class NrcSelector(QWidget):
    def __init__(self):
      super().__init__()
      self.init_ui()

    def init_ui(self):
        self.main_hbox = QHBoxLayout()
        self.setLayout(self.main_hbox)

        self.nrc_edit = QLineEdit()

        self.combo_box = QComboBox()
        self.combo_box.addItems(('AÑADIR', 'QUITAR'))

        self.main_hbox.addWidget(self.nrc_edit)
        self.main_hbox.addWidget(self.combo_box)


class MainWindow(QWidget):
    def __init__(self):
      super().__init__()

      self.nrc_boxes = deque()
      self.nrc_items = deque()

      self.init_ui()

    def init_ui(self) -> None:
        self.setWindowTitle('Auto-Ramos')

        self.main_vbox = QVBoxLayout()
        self.setLayout(self.main_vbox)

        self.datetimepicker = QDateTimeEdit(self)
        self.datetimepicker.setDateTime(QDateTime.currentDateTime())
        self.datetimepicker.setDisplayFormat("dd/MM/yyyy hh:mm:ss")

        self.main_vbox.addWidget(self.datetimepicker)

        # ASI SE OBTIENE LA FECHA ACTUAL EN FORMATO PYTHON
        # print(self.datetimepicker.dateTime().toPyDateTime())

        self.nrc_list = QListWidget()
        self.main_vbox.addWidget(self.nrc_list)
        self.add_nrc_box()


        self.button_hbox = QHBoxLayout()

        # self.remove_nrc_button = QPushButton('Quitar NRC')
        # self.remove_nrc_button.clicked.connect(self.remove_nrc_box)

        self.add_nrc_button = QPushButton('Añadir NRC')
        self.add_nrc_button.clicked.connect(self.add_nrc_box)
    
        # self.button_hbox.addWidget(self.remove_nrc_button)

        self.button_hbox.addWidget(self.add_nrc_button)
        self.main_vbox.addLayout(self.button_hbox)

        self.start_button = QPushButton('Iniciar')
        self.main_vbox.addWidget(self.start_button)

    def add_nrc_box(self):
        widget = NrcSelector()
        item = QListWidgetItem()

        self.nrc_list.insertItem(self.nrc_list.count(), item)
        self.nrc_list.setItemWidget(item, widget)
        item.setSizeHint(widget.sizeHint())

        self.nrc_boxes.append(widget)
        self.nrc_items.append(item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
