import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from MainWindow import Ui_MainWindow


class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            status, text = self.todos[index.row()]
            return text

    def rowCount(self, index):
        return len(self.todos)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel()
        self.todoView.setModel(self.model)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
