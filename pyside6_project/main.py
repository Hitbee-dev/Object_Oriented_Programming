import sys

from PySide6.QtWidgets import QApplication
from work.window import Window
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    app = QApplication(sys.argv)
    window: Window = Window()
    sys.exit(app.exec())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
