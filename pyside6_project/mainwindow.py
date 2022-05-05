# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EasyOCR_UIlVluXK.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1633, 1273)
        self.actionreset = QAction(MainWindow)
        self.actionreset.setObjectName(u"actionreset")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 1611, 1141))
        self.homeLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.homeLayout.setObjectName(u"homeLayout")
        self.homeLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 20, 1611, 551))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pretreatment1_Layout = QHBoxLayout()
        self.pretreatment1_Layout.setObjectName(u"pretreatment1_Layout")
        self.iu_Layout = QVBoxLayout()
        self.iu_Layout.setObjectName(u"iu_Layout")
        self.iu_Label = QLabel(self.verticalLayoutWidget_2)
        self.iu_Label.setObjectName(u"iu_Label")

        self.iu_Layout.addWidget(self.iu_Label)

        self.iu_Button = QPushButton(self.verticalLayoutWidget_2)
        self.iu_Button.setObjectName(u"iu_Button")

        self.iu_Layout.addWidget(self.iu_Button)


        self.pretreatment1_Layout.addLayout(self.iu_Layout)

        self.ig_Layout = QVBoxLayout()
        self.ig_Layout.setObjectName(u"ig_Layout")
        self.ig_Label = QLabel(self.verticalLayoutWidget_2)
        self.ig_Label.setObjectName(u"ig_Label")

        self.ig_Layout.addWidget(self.ig_Label)

        self.ig_Button = QPushButton(self.verticalLayoutWidget_2)
        self.ig_Button.setObjectName(u"ig_Button")

        self.ig_Layout.addWidget(self.ig_Button)


        self.pretreatment1_Layout.addLayout(self.ig_Layout)

        self.ib_Layout = QVBoxLayout()
        self.ib_Layout.setObjectName(u"ib_Layout")
        self.ib_Label = QLabel(self.verticalLayoutWidget_2)
        self.ib_Label.setObjectName(u"ib_Label")

        self.ib_Layout.addWidget(self.ib_Label)

        self.ib_Button = QPushButton(self.verticalLayoutWidget_2)
        self.ib_Button.setObjectName(u"ib_Button")

        self.ib_Layout.addWidget(self.ib_Button)


        self.pretreatment1_Layout.addLayout(self.ib_Layout)


        self.verticalLayout.addLayout(self.pretreatment1_Layout)

        self.pretreatment2_Layout = QHBoxLayout()
        self.pretreatment2_Layout.setObjectName(u"pretreatment2_Layout")
        self.ie_Layout = QVBoxLayout()
        self.ie_Layout.setObjectName(u"ie_Layout")
        self.ie_Label = QLabel(self.verticalLayoutWidget_2)
        self.ie_Label.setObjectName(u"ie_Label")

        self.ie_Layout.addWidget(self.ie_Label)

        self.ie_Button = QPushButton(self.verticalLayoutWidget_2)
        self.ie_Button.setObjectName(u"ie_Button")

        self.ie_Layout.addWidget(self.ie_Button)


        self.pretreatment2_Layout.addLayout(self.ie_Layout)

        self.io_Layout = QVBoxLayout()
        self.io_Layout.setObjectName(u"io_Layout")
        self.io_Label = QLabel(self.verticalLayoutWidget_2)
        self.io_Label.setObjectName(u"io_Label")

        self.io_Layout.addWidget(self.io_Label)

        self.io_Button = QPushButton(self.verticalLayoutWidget_2)
        self.io_Button.setObjectName(u"io_Button")

        self.io_Layout.addWidget(self.io_Button)


        self.pretreatment2_Layout.addLayout(self.io_Layout)

        self.itc_Layout = QVBoxLayout()
        self.itc_Layout.setObjectName(u"itc_Layout")
        self.itc_Label = QLabel(self.verticalLayoutWidget_2)
        self.itc_Label.setObjectName(u"itc_Label")

        self.itc_Layout.addWidget(self.itc_Label)

        self.itc_Button = QPushButton(self.verticalLayoutWidget_2)
        self.itc_Button.setObjectName(u"itc_Button")

        self.itc_Layout.addWidget(self.itc_Button)


        self.pretreatment2_Layout.addLayout(self.itc_Layout)


        self.verticalLayout.addLayout(self.pretreatment2_Layout)


        self.homeLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 30, 1609, 281))
        self.result1_Layout = QHBoxLayout(self.widget)
        self.result1_Layout.setObjectName(u"result1_Layout")
        self.result1_Layout.setContentsMargins(0, 0, 0, 0)
        self.dir_Layout = QVBoxLayout()
        self.dir_Layout.setObjectName(u"dir_Layout")
        self.dir_Label = QLabel(self.widget)
        self.dir_Label.setObjectName(u"dir_Label")

        self.dir_Layout.addWidget(self.dir_Label)

        self.dir_Button = QPushButton(self.widget)
        self.dir_Button.setObjectName(u"dir_Button")

        self.dir_Layout.addWidget(self.dir_Button)


        self.result1_Layout.addLayout(self.dir_Layout)

        self.disr_Layout = QVBoxLayout()
        self.disr_Layout.setObjectName(u"disr_Layout")
        self.disr_Label = QLabel(self.widget)
        self.disr_Label.setObjectName(u"disr_Label")

        self.disr_Layout.addWidget(self.disr_Label)

        self.disr_Button = QPushButton(self.widget)
        self.disr_Button.setObjectName(u"disr_Button")

        self.disr_Layout.addWidget(self.disr_Button)


        self.result1_Layout.addLayout(self.disr_Layout)

        self.ar_Layout = QVBoxLayout()
        self.ar_Layout.setObjectName(u"ar_Layout")
        self.ar_Label = QLabel(self.widget)
        self.ar_Label.setObjectName(u"ar_Label")

        self.ar_Layout.addWidget(self.ar_Label)

        self.ar_Button = QPushButton(self.widget)
        self.ar_Button.setObjectName(u"ar_Button")

        self.ar_Layout.addWidget(self.ar_Button)


        self.result1_Layout.addLayout(self.ar_Layout)

        self.tabWidget = QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 320, 1609, 241))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.di_tab = QWidget()
        self.di_tab.setObjectName(u"di_tab")
        self.scrollArea = QScrollArea(self.di_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 1361, 201))
        self.scrollArea.setWidgetResizable(True)
        self.input_problem = QWidget()
        self.input_problem.setObjectName(u"input_problem")
        self.input_problem.setGeometry(QRect(0, 0, 1359, 199))
        self.scrollArea.setWidget(self.input_problem)
        self.go_Button = QPushButton(self.di_tab)
        self.go_Button.setObjectName(u"go_Button")
        self.go_Button.setGeometry(QRect(1380, 160, 221, 51))
        self.idx_Button = QPushButton(self.di_tab)
        self.idx_Button.setObjectName(u"idx_Button")
        self.idx_Button.setGeometry(QRect(1380, 10, 221, 51))
        self.reset_Button = QPushButton(self.di_tab)
        self.reset_Button.setObjectName(u"reset_Button")
        self.reset_Button.setGeometry(QRect(1380, 60, 221, 51))
        self.save_Button = QPushButton(self.di_tab)
        self.save_Button.setObjectName(u"save_Button")
        self.save_Button.setGeometry(QRect(1380, 110, 221, 51))
        self.tabWidget.addTab(self.di_tab, "")
        self.result_tab = QWidget()
        self.result_tab.setObjectName(u"result_tab")
        self.scrollArea_2 = QScrollArea(self.result_tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(10, 10, 1361, 201))
        self.scrollArea_2.setWidgetResizable(True)
        self.result_problem = QWidget()
        self.result_problem.setObjectName(u"result_problem")
        self.result_problem.setGeometry(QRect(0, 0, 1359, 199))
        self.scrollArea_2.setWidget(self.result_problem)
        self.edit_Button = QPushButton(self.result_tab)
        self.edit_Button.setObjectName(u"edit_Button")
        self.edit_Button.setGeometry(QRect(1380, 10, 221, 51))
        self.screenshot_Button = QPushButton(self.result_tab)
        self.screenshot_Button.setObjectName(u"screenshot_Button")
        self.screenshot_Button.setGeometry(QRect(1380, 110, 221, 51))
        self.score_label = QLabel(self.result_tab)
        self.score_label.setObjectName(u"score_label")
        self.score_label.setGeometry(QRect(1380, 170, 221, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setKerning(True)
        self.score_label.setFont(font)
        self.score_label.setAlignment(Qt.AlignCenter)
        self.done_Button = QPushButton(self.result_tab)
        self.done_Button.setObjectName(u"done_Button")
        self.done_Button.setGeometry(QRect(1380, 60, 221, 51))
        self.tabWidget.addTab(self.result_tab, "")

        self.homeLayout.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1633, 24))
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

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionreset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Image preprocessing", None))
        self.iu_Label.setText("")
        self.iu_Button.setText(QCoreApplication.translate("MainWindow", u"1. Image Upload", None))
        self.ig_Label.setText("")
        self.ig_Button.setText(QCoreApplication.translate("MainWindow", u"2. Image GrayScale", None))
        self.ib_Label.setText("")
        self.ib_Button.setText(QCoreApplication.translate("MainWindow", u"3. Image Blur", None))
        self.ie_Label.setText("")
        self.ie_Button.setText(QCoreApplication.translate("MainWindow", u"4. Image Edged", None))
        self.io_Label.setText("")
        self.io_Button.setText(QCoreApplication.translate("MainWindow", u"5. Image Outline", None))
        self.itc_Label.setText("")
        self.itc_Button.setText(QCoreApplication.translate("MainWindow", u"6. Image Tilt Correction", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Image Recognition", None))
        self.dir_Label.setText("")
        self.dir_Button.setText(QCoreApplication.translate("MainWindow", u"7. Digit Image Recognition", None))
        self.disr_Label.setText("")
        self.disr_Button.setText(QCoreApplication.translate("MainWindow", u"8. Digit Image Segmentation Recognition", None))
        self.ar_Label.setText("")
        self.ar_Button.setText(QCoreApplication.translate("MainWindow", u"9. Answer Recognition", None))
        self.go_Button.setText(QCoreApplication.translate("MainWindow", u"Go!", None))
        self.idx_Button.setText(QCoreApplication.translate("MainWindow", u"Index", None))
        self.reset_Button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.save_Button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.di_tab), QCoreApplication.translate("MainWindow", u"Data Input", None))
        self.edit_Button.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.screenshot_Button.setText(QCoreApplication.translate("MainWindow", u"ScreenShot", None))
        self.score_label.setText(QCoreApplication.translate("MainWindow", u"SCORE: 40 / 50 [80]", None))
        self.done_Button.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.result_tab), QCoreApplication.translate("MainWindow", u"Result", None))
        self.menureset.setTitle(QCoreApplication.translate("MainWindow", u"Reset", None))
    # retranslateUi

