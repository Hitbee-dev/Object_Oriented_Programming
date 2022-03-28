import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton  # <1>


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # <2>

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        self.setCentralWidget(button)  # <3>

        # self.setFixedSize(width, height)를 하게 되면 창의 크기가 고정되며 수정이 불가능하다.
        # self.setFixedSize(400, 500)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
