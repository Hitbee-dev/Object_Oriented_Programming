from PySide6.QtWidgets import *
from work.view.tool import Tool

class Window(QMainWindow):

    tool: Tool  # 툴바 입니다.

    def __init__(self):
        super(Window, self).__init__()

        self.tool = Tool()
        self.addToolBar(self.tool)
        self.show()