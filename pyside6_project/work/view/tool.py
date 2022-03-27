from PySide6.QtWidgets import *
from PySide6.QtGui import QAction, QIcon

class Tool(QToolBar):

    helpAction: QAction # 도움 액션

    def __init__(self):
        super(Tool, self).__init__()
        print('Tool: init')

        self.helpAction = QAction(QIcon(None), 'help', self)
        self.helpAction.triggered.connect(self.help_action_click)
        self.addAction(self.helpAction)

    def help_action_click(self):
        print('Tool: help_action_click')