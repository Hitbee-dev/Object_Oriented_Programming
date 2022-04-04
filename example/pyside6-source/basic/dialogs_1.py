import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)

        dlg = QDialog(self)
        # QDialog에서 self를 선언해 주지 않으면 완전히 새로운 창에서 Dialog를 띄우고,
        # self를 선언해 주면 실행중인 창 안에서 Dialog를 띄운다.
        dlg.setWindowTitle("?")
        dlg.exec()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
