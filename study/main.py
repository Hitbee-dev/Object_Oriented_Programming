from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Title Name
        self.setWindowTitle("TEST")

        # Window Size조정(FixedSize넣으면 자동조절 안됨)
        self.setFixedSize(500, 400)

        # Button 선언 및 실행
        self.button = QPushButton("Push!")
        self.button.setFixedSize(100, 50)
        self.setCentralWidget(self.button)

        self.button.clicked.connect(self.button_click_event)

    def button_click_event(self):
        print("PUSH!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()