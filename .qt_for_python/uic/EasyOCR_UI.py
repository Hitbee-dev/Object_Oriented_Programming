# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EasyOCR_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(641, 1109)
        self.actionreset = QAction(MainWindow)
        self.actionreset.setObjectName(u"actionreset")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 619, 641))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 617, 639))
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 601, 61))
        self.init_Layout = QHBoxLayout(self.widget)
        self.init_Layout.setObjectName(u"init_Layout")
        self.init_Layout.setContentsMargins(0, 0, 0, 0)
        self.iu_Layout = QVBoxLayout()
        self.iu_Layout.setObjectName(u"iu_Layout")
        self.iu_Label = QLabel(self.widget)
        self.iu_Label.setObjectName(u"iu_Label")

        self.iu_Layout.addWidget(self.iu_Label)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.iu_Layout.addWidget(self.pushButton)


        self.init_Layout.addLayout(self.iu_Layout)

        self.sc_Layout = QVBoxLayout()
        self.sc_Layout.setObjectName(u"sc_Layout")
        self.sc_Label = QLabel(self.widget)
        self.sc_Label.setObjectName(u"sc_Label")

        self.sc_Layout.addWidget(self.sc_Label)

        self.sc_Button = QPushButton(self.widget)
        self.sc_Button.setObjectName(u"sc_Button")

        self.sc_Layout.addWidget(self.sc_Button)


        self.init_Layout.addLayout(self.sc_Layout)

        self.widget1 = QWidget(self.scrollAreaWidgetContents)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 80, 601, 61))
        self.recognition_Layout = QHBoxLayout(self.widget1)
        self.recognition_Layout.setObjectName(u"recognition_Layout")
        self.recognition_Layout.setContentsMargins(0, 0, 0, 0)
        self.ir_Layout = QVBoxLayout()
        self.ir_Layout.setObjectName(u"ir_Layout")
        self.ir_Label = QLabel(self.widget1)
        self.ir_Label.setObjectName(u"ir_Label")

        self.ir_Layout.addWidget(self.ir_Label)

        self.ir_Button = QPushButton(self.widget1)
        self.ir_Button.setObjectName(u"ir_Button")

        self.ir_Layout.addWidget(self.ir_Button)


        self.recognition_Layout.addLayout(self.ir_Layout)

        self.isr_Layout = QVBoxLayout()
        self.isr_Layout.setObjectName(u"isr_Layout")
        self.isr_Label = QLabel(self.widget1)
        self.isr_Label.setObjectName(u"isr_Label")

        self.isr_Layout.addWidget(self.isr_Label)

        self.isr_Button = QPushButton(self.widget1)
        self.isr_Button.setObjectName(u"isr_Button")

        self.isr_Layout.addWidget(self.isr_Button)


        self.recognition_Layout.addLayout(self.isr_Layout)

        self.layoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 680, 601, 61))
        self.init_Layout_6 = QHBoxLayout(self.layoutWidget)
        self.init_Layout_6.setObjectName(u"init_Layout_6")
        self.init_Layout_6.setContentsMargins(0, 0, 0, 0)
        self.iu_Layout_6 = QVBoxLayout()
        self.iu_Layout_6.setObjectName(u"iu_Layout_6")
        self.iu_Label_6 = QLabel(self.layoutWidget)
        self.iu_Label_6.setObjectName(u"iu_Label_6")

        self.iu_Layout_6.addWidget(self.iu_Label_6)

        self.pushButton_9 = QPushButton(self.layoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.iu_Layout_6.addWidget(self.pushButton_9)


        self.init_Layout_6.addLayout(self.iu_Layout_6)

        self.sc_Layout_6 = QVBoxLayout()
        self.sc_Layout_6.setObjectName(u"sc_Layout_6")
        self.sc_Label_6 = QLabel(self.layoutWidget)
        self.sc_Label_6.setObjectName(u"sc_Label_6")

        self.sc_Layout_6.addWidget(self.sc_Label_6)

        self.sc_Button_6 = QPushButton(self.layoutWidget)
        self.sc_Button_6.setObjectName(u"sc_Button_6")

        self.sc_Layout_6.addWidget(self.sc_Button_6)


        self.init_Layout_6.addLayout(self.sc_Layout_6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 641, 24))
        self.menureset = QMenu(self.menubar)
        self.menureset.setObjectName(u"menureset")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menureset.menuAction())
        self.menureset.addAction(self.actionreset)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionreset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.iu_Label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"1. Image Upload", None))
        self.sc_Label.setText("")
        self.sc_Button.setText(QCoreApplication.translate("MainWindow", u"2. Image Slope correction", None))
        self.ir_Label.setText("")
        self.ir_Button.setText(QCoreApplication.translate("MainWindow", u"3. Image Recognition", None))
        self.isr_Label.setText("")
        self.isr_Button.setText(QCoreApplication.translate("MainWindow", u"4. Image Segmentation Recognition", None))
        self.iu_Label_6.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"1. Image Upload", None))
        self.sc_Label_6.setText("")
        self.sc_Button_6.setText(QCoreApplication.translate("MainWindow", u"2. Image Slope correction", None))
        self.menureset.setTitle(QCoreApplication.translate("MainWindow", u"Reset", None))
    # retranslateUi

