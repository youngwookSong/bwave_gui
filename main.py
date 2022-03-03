import sys
import os
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6 import QtUiTools, QtGui
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, Qt, QEvent)

#imort gui file
from ui_main import Ui_MainWindow

#import gui functions
from ui_funtions import *

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dragPos = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.control()
        self.ui.logo.setPixmap(QPixmap("image/sooncheon_fc_mean.PNG"))
        # self.ui.logo.setScaledContents(True)

        #move window with title bar
        def moveWindow(event):
            if UIFunctions.returnStatus(self) == 1:
                UIFunctions.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.title_bar.mouseMoveEvent = moveWindow
        UIFunctions.uiDefinitions(self)

        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def control(self):
        self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        self.ui.btn_home.clicked.connect(lambda: UIFunctions.set_page(self, self.ui.home))
        self.ui.btn_anal.clicked.connect(lambda: UIFunctions.set_page(self, self.ui.anal))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainView()
    sys.exit(app.exec())