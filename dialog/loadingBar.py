# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadingBarsbaosQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Dialog_loading(QDialog):
    def __init__(self):
        super().__init__()

        self.resize(730, 350)
        self.setMinimumSize(QSize(730, 350))
        self.setMaximumSize(QSize(730, 350))
        self.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(self)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 250, 216);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 30))
        self.frame_2.setMaximumSize(QSize(16777215, 30))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font.setPointSize(30)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_title)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font1.setPointSize(15)
        self.label_2.setFont(font1)
        self.label_2.setLocale(QLocale(QLocale.Kpelle, QLocale.Liberia))
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 20))
        self.frame_4.setMaximumSize(QSize(16777215, 20))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_4)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 30))
        self.progressBar.setMaximumSize(QSize(16777215, 30))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"	background-color: rgb(235, 235, 235);\n"
"	margin-left: 20px;\n"
"	margin-right: 20px;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.472, x2:1, y2:0.472, stop:0 rgba(166, 166, 166, 255), stop:1 rgba(229, 254, 255, 255));\n"
"}\n"
"")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font2.setPointSize(12)
        self.label_3.setFont(font2)
        self.label_3.setLocale(QLocale(QLocale.Kpelle, QLocale.Liberia))
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label_3)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_title.setText(QCoreApplication.translate("Dialog", u"<strong>\uc0c8\ub85c\uc6b4 \ub370\uc774\ud130 \ubd84\uc11d \uc911..", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\uc9c4\ud589 \ud604\ud669...", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"loading...", None))
    # retranslateUi

