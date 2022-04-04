import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from layout_color import CustomColor
# 내가 작성한 모듈의 클래스 참조

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        # 프로그램 상단에 있는 이름

        widget = CustomColor("red")
        # 내가 작성한 모듈의 클래스를 호출해서 widget에 넣기
        self.setCentralWidget(widget)
        # 색상을 setCentralWidget에 적용

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()