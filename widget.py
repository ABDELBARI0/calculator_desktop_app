# This Python file uses the following encoding: utf-8
import sys

from PySide6 import QtWidgets

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QtWidgets,Ui_Widget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        #connection of boutoms
        self.pushButton_1.clicked.connect(self.degit_pressed)



    def degit_pressed(self):
        print("test")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
