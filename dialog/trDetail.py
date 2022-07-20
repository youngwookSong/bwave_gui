# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trDetailfmHBJY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Dialog_trDetail(QDialog):
    def __init__(self, name, num):
        super().__init__()

        self.name = name
        self.num = num

        self.resize(1150, 750)
        self.setMaximumSize(1150, 750)
        self.setMinimumSize(1150, 750)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 30, 91, 41))

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"tr-detail", None))
    # retranslateUi

