from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.actionreset = QAction(MainWindow)
        self.actionreset.setObjectName(u"actionreset")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 621, 411))
        self.homeLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.homeLayout.setObjectName(u"homeLayout")
        self.homeLayout.setContentsMargins(0, 0, 0, 0)
        self.init_Layout = QHBoxLayout()
        self.init_Layout.setObjectName(u"init_Layout")
        self.iu_Layout = QVBoxLayout()
        self.iu_Layout.setObjectName(u"iu_Layout")
        self.iu_Label = QLabel(self.verticalLayoutWidget)
        self.iu_Label.setObjectName(u"iu_Label")

        self.iu_Layout.addWidget(self.iu_Label)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.iu_Layout.addWidget(self.pushButton)


        self.init_Layout.addLayout(self.iu_Layout)

        self.sc_Layout = QVBoxLayout()
        self.sc_Layout.setObjectName(u"sc_Layout")
        self.sc_Label = QLabel(self.verticalLayoutWidget)
        self.sc_Label.setObjectName(u"sc_Label")

        self.sc_Layout.addWidget(self.sc_Label)

        self.sc_Button = QPushButton(self.verticalLayoutWidget)
        self.sc_Button.setObjectName(u"sc_Button")

        self.sc_Layout.addWidget(self.sc_Button)


        self.init_Layout.addLayout(self.sc_Layout)


        self.homeLayout.addLayout(self.init_Layout)

        self.recognition_Layout = QHBoxLayout()
        self.recognition_Layout.setObjectName(u"recognition_Layout")
        self.ir_Layout = QVBoxLayout()
        self.ir_Layout.setObjectName(u"ir_Layout")
        self.ir_Label = QLabel(self.verticalLayoutWidget)
        self.ir_Label.setObjectName(u"ir_Label")

        self.ir_Layout.addWidget(self.ir_Label)

        self.ir_Button = QPushButton(self.verticalLayoutWidget)
        self.ir_Button.setObjectName(u"ir_Button")

        self.ir_Layout.addWidget(self.ir_Button)


        self.recognition_Layout.addLayout(self.ir_Layout)

        self.isr_Layout = QVBoxLayout()
        self.isr_Layout.setObjectName(u"isr_Layout")
        self.isr_Label = QLabel(self.verticalLayoutWidget)
        self.isr_Label.setObjectName(u"isr_Label")

        self.isr_Layout.addWidget(self.isr_Label)

        self.isr_Button = QPushButton(self.verticalLayoutWidget)
        self.isr_Button.setObjectName(u"isr_Button")

        self.isr_Layout.addWidget(self.isr_Button)


        self.recognition_Layout.addLayout(self.isr_Layout)


        self.homeLayout.addLayout(self.recognition_Layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 24))
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
        self.menureset.setTitle(QCoreApplication.translate("MainWindow", u"Reset", None))
    # retranslateUi
