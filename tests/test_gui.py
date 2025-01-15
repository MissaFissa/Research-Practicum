"""A gui for a graphing application.
"""
import sys
from pathlib import Path
import numpy as np
import pyqtgraph as pg
import pandas as pd
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl, Slot, QTimer)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform, QShortcut)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox,
                               QFileDialog, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QLineEdit, QMainWindow, QMenuBar,
                               QPushButton, QSizePolicy, QSpinBox, QStatusBar,
                               QStyle, QToolBar, QVBoxLayout, QWidget, QSlider)

from data_gathering import DataGathering
from test_interface import Ui_MainWindow

pg.setConfigOption("foreground", "w")
pg.setConfigOptions(antialias = True)

cwd = Path.cwd()

class UserInterface(QMainWindow):

    def __init__(self):

        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)




        self.data = DataGathering()

        # self.data.

        self.plot_data = self.ui.comboBox.currentText()
        

    # def updatePlot(self):




def main():

    app = QApplication(sys.argv)
    ui = UserInterface()
    # ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":

    main()