import sys

from PySide6.QtWidgets import QApplication
from work.window import Window

# __name__ == "__main__"을 사용하는 이유
# main.py에 있는 모든 프로세스를 실행시키는 것이 아니라
# 다른곳에서 참조할 때 함수만 실행할 수 있도록 하는 것
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window: Window = Window()
    sys.exit(app.exec())
