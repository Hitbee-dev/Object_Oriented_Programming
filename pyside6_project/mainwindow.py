# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EasyOCR_UIggBbqx.ui'
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
    QTransform, QPixmap)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1030, 840)
        self.actionreset = QAction(MainWindow)
        self.actionreset.setObjectName(u"actionreset")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 1011, 771))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ip_groupBox = QGroupBox(self.verticalLayoutWidget)
        self.ip_groupBox.setObjectName(u"ip_groupBox")
        font = QFont()
        font.setPointSize(13)
        self.ip_groupBox.setFont(font)
        self.verticalLayoutWidget_3 = QWidget(self.ip_groupBox)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 20, 1011, 361))
        self.ip_VLayout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.ip_VLayout.setObjectName(u"ip_VLayout")
        self.ip_VLayout.setContentsMargins(0, 0, 0, 0)
        self.ip_Layout1 = QHBoxLayout()
        self.ip_Layout1.setObjectName(u"ip_Layout1")
        self.upload_Layout = QVBoxLayout()
        self.upload_Layout.setObjectName(u"upload_Layout")
        self.upload_Label = QLabel(self.verticalLayoutWidget_3)
        self.upload_Label.setObjectName(u"upload_Label")

        self.upload_Layout.addWidget(self.upload_Label)

        self.upload_Button = QPushButton(self.verticalLayoutWidget_3)
        self.upload_Button.setObjectName(u"upload_Button")
        self.upload_Layout.addWidget(self.upload_Button)

        self.ip_Layout1.addLayout(self.upload_Layout)
        self.upload_Button.clicked.connect(self.upload_button_click_event)
        
        self.grayscale_Layout = QVBoxLayout()
        self.grayscale_Layout.setObjectName(u"grayscale_Layout")
        self.grayscale_Label = QLabel(self.verticalLayoutWidget_3)
        self.grayscale_Label.setObjectName(u"grayscale_Label")

        self.grayscale_Layout.addWidget(self.grayscale_Label)

        self.grayscale_Button = QPushButton(self.verticalLayoutWidget_3)
        self.grayscale_Button.setObjectName(u"grayscale_Button")

        self.grayscale_Layout.addWidget(self.grayscale_Button)


        self.ip_Layout1.addLayout(self.grayscale_Layout)

        self.blur_Layout = QVBoxLayout()
        self.blur_Layout.setObjectName(u"blur_Layout")
        self.blur_Label = QLabel(self.verticalLayoutWidget_3)
        self.blur_Label.setObjectName(u"blur_Label")

        self.blur_Layout.addWidget(self.blur_Label)

        self.blur_Button = QPushButton(self.verticalLayoutWidget_3)
        self.blur_Button.setObjectName(u"blur_Button")

        self.blur_Layout.addWidget(self.blur_Button)


        self.ip_Layout1.addLayout(self.blur_Layout)


        self.ip_VLayout.addLayout(self.ip_Layout1)

        self.ip_Layout2 = QHBoxLayout()
        self.ip_Layout2.setObjectName(u"ip_Layout2")
        self.edged_Layout = QVBoxLayout()
        self.edged_Layout.setObjectName(u"edged_Layout")
        self.edged_Label = QLabel(self.verticalLayoutWidget_3)
        self.edged_Label.setObjectName(u"edged_Label")

        self.edged_Layout.addWidget(self.edged_Label)

        self.edged_Button = QPushButton(self.verticalLayoutWidget_3)
        self.edged_Button.setObjectName(u"edged_Button")

        self.edged_Layout.addWidget(self.edged_Button)


        self.ip_Layout2.addLayout(self.edged_Layout)

        self.outline_Layout = QVBoxLayout()
        self.outline_Layout.setObjectName(u"outline_Layout")
        self.outline_Label = QLabel(self.verticalLayoutWidget_3)
        self.outline_Label.setObjectName(u"outline_Label")

        self.outline_Layout.addWidget(self.outline_Label)

        self.outline_Button = QPushButton(self.verticalLayoutWidget_3)
        self.outline_Button.setObjectName(u"outline_Button")

        self.outline_Layout.addWidget(self.outline_Button)


        self.ip_Layout2.addLayout(self.outline_Layout)

        self.tilt_Layout = QVBoxLayout()
        self.tilt_Layout.setObjectName(u"tilt_Layout")
        self.tilt_Label = QLabel(self.verticalLayoutWidget_3)
        self.tilt_Label.setObjectName(u"tilt_Label")

        self.tilt_Layout.addWidget(self.tilt_Label)

        self.tilt_Button = QPushButton(self.verticalLayoutWidget_3)
        self.tilt_Button.setObjectName(u"tilt_Button")

        self.tilt_Layout.addWidget(self.tilt_Button)


        self.ip_Layout2.addLayout(self.tilt_Layout)


        self.ip_VLayout.addLayout(self.ip_Layout2)


        self.verticalLayout.addWidget(self.ip_groupBox)

        self.ir_groupBox = QGroupBox(self.verticalLayoutWidget)
        self.ir_groupBox.setObjectName(u"ir_groupBox")
        self.ir_groupBox.setFont(font)
        self.verticalLayoutWidget_2 = QWidget(self.ir_groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 20, 1011, 181))
        self.ir_VLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.ir_VLayout.setObjectName(u"ir_VLayout")
        self.ir_VLayout.setContentsMargins(0, 0, 0, 0)
        self.ir_Layout = QHBoxLayout()
        self.ir_Layout.setObjectName(u"ir_Layout")
        self.dr_Layout = QVBoxLayout()
        self.dr_Layout.setObjectName(u"dr_Layout")
        self.dr_Label = QLabel(self.verticalLayoutWidget_2)
        self.dr_Label.setObjectName(u"dr_Label")

        self.dr_Layout.addWidget(self.dr_Label)

        self.dr_Button = QPushButton(self.verticalLayoutWidget_2)
        self.dr_Button.setObjectName(u"dr_Button")

        self.dr_Layout.addWidget(self.dr_Button)


        self.ir_Layout.addLayout(self.dr_Layout)

        self.dsr_Layout = QVBoxLayout()
        self.dsr_Layout.setObjectName(u"dsr_Layout")
        self.dsr_Label = QLabel(self.verticalLayoutWidget_2)
        self.dsr_Label.setObjectName(u"dsr_Label")

        self.dsr_Layout.addWidget(self.dsr_Label)

        self.dsr_Button = QPushButton(self.verticalLayoutWidget_2)
        self.dsr_Button.setObjectName(u"dsr_Button")

        self.dsr_Layout.addWidget(self.dsr_Button)


        self.ir_Layout.addLayout(self.dsr_Layout)

        self.result_Layout = QVBoxLayout()
        self.result_Layout.setObjectName(u"result_Layout")
        self.result_Label = QLabel(self.verticalLayoutWidget_2)
        self.result_Label.setObjectName(u"result_Label")

        self.result_Layout.addWidget(self.result_Label)

        self.result_Button = QPushButton(self.verticalLayoutWidget_2)
        self.result_Button.setObjectName(u"result_Button")

        self.result_Layout.addWidget(self.result_Button)


        self.ir_Layout.addLayout(self.result_Layout)


        self.ir_VLayout.addLayout(self.ir_Layout)

        self.tabWidget = QTabWidget(self.ir_groupBox)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 200, 1011, 181))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(False)
        self.tabWidget.setFont(font1)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.create_tab = QWidget()
        self.create_tab.setObjectName(u"create_tab")
        self.create_scrollArea = QScrollArea(self.create_tab)
        self.create_scrollArea.setObjectName(u"create_scrollArea")
        self.create_scrollArea.setGeometry(QRect(10, 10, 841, 141))
        self.create_scrollArea.setWidgetResizable(True)
        self.create_scrollAreaWidgetContents = QWidget()
        self.create_scrollAreaWidgetContents.setObjectName(u"create_scrollAreaWidgetContents")
        self.create_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 839, 139))
        self.create_scrollArea.setWidget(self.create_scrollAreaWidgetContents)
        self.create_Button = QPushButton(self.create_tab)
        self.create_Button.setObjectName(u"create_Button")
        self.create_Button.setGeometry(QRect(860, 10, 141, 41))
        self.create_Button.setFont(font1)
        self.create_Button.setAutoDefault(False)
        self.save_Button = QPushButton(self.create_tab)
        self.save_Button.setObjectName(u"save_Button")
        self.save_Button.setGeometry(QRect(860, 60, 141, 41))
        self.save_Button.setFont(font1)
        self.save_Button.setAutoDefault(False)
        self.go_Button = QPushButton(self.create_tab)
        self.go_Button.setObjectName(u"go_Button")
        self.go_Button.setGeometry(QRect(860, 110, 141, 41))
        self.go_Button.setFont(font1)
        self.go_Button.setAutoDefault(False)
        self.tabWidget.addTab(self.create_tab, "")
        self.result_tab = QWidget()
        self.result_tab.setObjectName(u"result_tab")
        self.result_scrollArea = QScrollArea(self.result_tab)
        self.result_scrollArea.setObjectName(u"result_scrollArea")
        self.result_scrollArea.setGeometry(QRect(10, 10, 841, 141))
        self.result_scrollArea.setWidgetResizable(True)
        self.result_scrollAreaWidgetContents = QWidget()
        self.result_scrollAreaWidgetContents.setObjectName(u"result_scrollAreaWidgetContents")
        self.result_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 839, 139))
        self.result_scrollArea.setWidget(self.result_scrollAreaWidgetContents)
        self.edit_Button = QPushButton(self.result_tab)
        self.edit_Button.setObjectName(u"edit_Button")
        self.edit_Button.setGeometry(QRect(860, 10, 141, 41))
        self.edit_Button.setFont(font1)
        self.edit_Button.setAutoDefault(False)
        self.done_Button = QPushButton(self.result_tab)
        self.done_Button.setObjectName(u"done_Button")
        self.done_Button.setGeometry(QRect(860, 60, 141, 41))
        self.done_Button.setFont(font1)
        self.done_Button.setAutoDefault(False)
        self.score_label = QLabel(self.result_tab)
        self.score_label.setObjectName(u"score_label")
        self.score_label.setGeometry(QRect(860, 100, 141, 51))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        self.score_label.setFont(font2)
        self.score_label.setFrameShadow(QFrame.Plain)
        self.score_label.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.result_tab, "")

        self.verticalLayout.addWidget(self.ir_groupBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1030, 24))
        self.menureset = QMenu(self.menubar)
        self.menureset.setObjectName(u"menureset")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menureset.menuAction())
        self.menureset.addAction(self.actionreset)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def upload_button_click_event(self):
        print("Check")
        self.upload_Label.setPixmap(QPixmap(r"/Users/chankim/IndividualProject/Object_Oriented_Programming/pyside6_project/images/1. Upload.jpg"))
        self.upload_Label.setScaledContents(True)
    # function

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionreset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.ip_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Image Preprocessing", None))
        self.upload_Label.setText("")
        self.upload_Button.setText(QCoreApplication.translate("MainWindow", u"1. Upload", None))
        self.grayscale_Label.setText("")
        self.grayscale_Button.setText(QCoreApplication.translate("MainWindow", u"2. GrayScale", None))
        self.blur_Label.setText("")
        self.blur_Button.setText(QCoreApplication.translate("MainWindow", u"3. Blur", None))
        self.edged_Label.setText("")
        self.edged_Button.setText(QCoreApplication.translate("MainWindow", u"4. Edged", None))
        self.outline_Label.setText("")
        self.outline_Button.setText(QCoreApplication.translate("MainWindow", u"5. Outline", None))
        self.tilt_Label.setText("")
        self.tilt_Button.setText(QCoreApplication.translate("MainWindow", u"6. Tilt Correction", None))
        self.ir_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Image Recognition", None))
        self.dr_Label.setText("")
        self.dr_Button.setText(QCoreApplication.translate("MainWindow", u"7. Digit Recognition", None))
        self.dsr_Label.setText("")
        self.dsr_Button.setText(QCoreApplication.translate("MainWindow", u"8. Digit Segmentation Recognition", None))
        self.result_Label.setText("")
        self.result_Button.setText(QCoreApplication.translate("MainWindow", u"9. Result", None))
        self.create_Button.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.save_Button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.go_Button.setText(QCoreApplication.translate("MainWindow", u"Go!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.create_tab), QCoreApplication.translate("MainWindow", u"Create", None))
        self.edit_Button.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.done_Button.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.score_label.setText(QCoreApplication.translate("MainWindow", u"SCORE = 40 / 50 [80]", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.result_tab), QCoreApplication.translate("MainWindow", u"Result", None))
        self.menureset.setTitle(QCoreApplication.translate("MainWindow", u"Reset", None))
    # retranslateUi

