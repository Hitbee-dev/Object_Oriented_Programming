from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget

class CustomColor(QWidget): # QWidget 상속
    def __init__(self, color):
        super().__init__()
        # 상속받은 QWidget의 init을 가져옴
        self.setAutoFillBackground(True)
        # background의 Color를 변경
    
        palette = self.palette()
        # palette 변수에 QWidgets에 있는 palette를 참조
        palette.setColor(QPalette.Window, QColor(color))
        # palette의 색을 받아와서 적용
        self.setPalette(palette)
        # palette 설정