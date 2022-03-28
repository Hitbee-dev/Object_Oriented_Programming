from PySide6.QtWidgets import *
from PySide6.QtGui import QAction, QIcon

class Tool(QToolBar):

    fileAction: QAction  # File
    editAction: QAction  # Edit
    viewAction: QAction  # View
    navigateAction: QAction  # Navigate
    codeAction: QAction  # Code
    refactorAction: QAction  # Refactor
    runAction: QAction  # Run
    toolsAction: QAction  # Tools
    gitAction: QAction  # Git
    windowAction: QAction  # Window
    helpAction: QAction  # Help

    def __init__(self):
        super(Tool, self).__init__()
        print('Tool: init')

        self.fileAction = QAction(QIcon(None), 'File', self)
        self.editAction = QAction(QIcon(None), 'Edit', self)
        self.viewAction = QAction(QIcon(None), 'View', self)
        self.navigateAction = QAction(QIcon(None), 'Navigate', self)
        self.codeAction = QAction(QIcon(None), 'Code', self)
        self.refactorAction = QAction(QIcon(None), 'Refactor', self)
        self.runAction = QAction(QIcon(None), 'Run', self)
        self.toolsAction = QAction(QIcon(None), 'Tools', self)
        self.gitAction = QAction(QIcon(None), 'Git', self)
        self.windowAction = QAction(QIcon(None), 'Window', self)
        self.helpAction = QAction(QIcon(None), 'Help', self)

        self.fileAction.triggered.connect(self.file_action)
        self.editAction.triggered.connect(self.edit_action)
        self.viewAction.triggered.connect(self.view_action)
        self.navigateAction.triggered.connect(self.navigate_action)
        self.codeAction.triggered.connect(self.code_action)
        self.refactorAction.triggered.connect(self.refactor_action)
        self.runAction.triggered.connect(self.run_action)
        self.toolsAction.triggered.connect(self.tools_action)
        self.gitAction.triggered.connect(self.git_action)
        self.windowAction.triggered.connect(self.window_action)
        self.helpAction.triggered.connect(self.help_action)

        self.fileAction
        self.editAction
        self.viewAction
        self.navigateAction
        self.codeAction
        self.refactorAction
        self.runAction
        self.toolsAction
        self.gitAction
        self.windowAction
        self.helpAction

        self.addAction(self.fileAction)
        self.addAction(self.editAction)
        self.addAction(self.viewAction)
        self.addAction(self.navigateAction)
        self.addAction(self.codeAction)
        self.addAction(self.refactorAction)
        self.addAction(self.runAction)
        self.addAction(self.toolsAction)
        self.addAction(self.gitAction)
        self.addAction(self.windowAction)
        self.addAction(self.helpAction)

    def file_action(self):
        print('Tool: file_action')

    def edit_action(self):
        print('Tool: edit_action')

    def view_action(self):
        print('Tool: view_action')

    def navigate_action(self):
        print('Tool: navigate_action')

    def code_action(self):
        print('Tool: code_action')

    def refactor_action(self):
        print('Tool: refactor_action')

    def run_action(self):
        print('Tool: run_action')

    def tools_action(self):
        print('Tool: tools_action')

    def git_action(self):
        print('Tool: git_action')

    def window_action(self):
        print('Tool: window_action')

    def help_action(self):
        print('Tool: help_action')