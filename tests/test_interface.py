# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plotFrame = QFrame(self.centralwidget)
        self.plotFrame.setObjectName(u"plotFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.plotFrame.sizePolicy().hasHeightForWidth())
        self.plotFrame.setSizePolicy(sizePolicy)
        self.plotFrame.setStyleSheet(u"background-color: gray")
        self.plotFrame.setFrameShape(QFrame.Shape.Box)
        self.plotFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.plotFrame.setLineWidth(2)
        self.plotFrame.setMidLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.plotFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.plotWidget = PlotWidget(self.plotFrame)
        self.plotWidget.setObjectName(u"plotWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy1)
        self.plotWidget.setStyleSheet(u"background-color: b")

        self.horizontalLayout.addWidget(self.plotWidget)


        self.verticalLayout.addWidget(self.plotFrame)

        self.optionsFrame = QFrame(self.centralwidget)
        self.optionsFrame.setObjectName(u"optionsFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.optionsFrame.sizePolicy().hasHeightForWidth())
        self.optionsFrame.setSizePolicy(sizePolicy2)
        self.optionsFrame.setStyleSheet(u"background-color: gray")
        self.optionsFrame.setFrameShape(QFrame.Shape.Box)
        self.optionsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.optionsFrame.setLineWidth(2)
        self.optionsFrame.setMidLineWidth(1)
        self.horizontalLayout_2 = QHBoxLayout(self.optionsFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.optionsWidget = QWidget(self.optionsFrame)
        self.optionsWidget.setObjectName(u"optionsWidget")
        self.optionsWidget.setStyleSheet(u"background-color: b")
        self.horizontalLayout_3 = QHBoxLayout(self.optionsWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.comboBox = QComboBox(self.optionsWidget)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(3)
        sizePolicy3.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy3)
        self.comboBox.setMinimumSize(QSize(350, 25))
        self.comboBox.setStyleSheet(u"background-color: gray; color: black;")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.widget = QWidget(self.optionsWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: gray")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_5 = QCheckBox(self.widget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setStyleSheet(u"background-color:b")

        self.gridLayout.addWidget(self.checkBox_5, 0, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.widget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setStyleSheet(u"background-color:b")

        self.gridLayout.addWidget(self.checkBox_3, 0, 1, 1, 1)

        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"background-color:b")

        self.gridLayout.addWidget(self.checkBox, 0, 2, 1, 1)

        self.checkBox_6 = QCheckBox(self.widget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setStyleSheet(u"background-color:b")

        self.gridLayout.addWidget(self.checkBox_6, 1, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.widget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setStyleSheet(u"background-color:b")

        self.gridLayout.addWidget(self.checkBox_4, 1, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.widget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"background-color:b")

        self.gridLayout.addWidget(self.checkBox_2, 1, 2, 1, 1)


        self.horizontalLayout_3.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.optionsWidget)


        self.verticalLayout.addWidget(self.optionsFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.comboBox.setPlaceholderText("")
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
    # retranslateUi

