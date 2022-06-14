# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'psdPowerHzilbFDP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from personal_data.resources import *


class Ui_Dialog_power(QDialog):
    def __init__(self, name, num):
        super().__init__()

        self.name = name
        self.num = num

        self.page_idx = 0

        # self.setWindowTitle("PSD Hz")
        self.resize(620, 860)
        self.setMinimumSize(QSize(620, 860))
        self.setMaximumSize(QSize(620, 860))
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setStyleSheet("background-color: rgb(255,255,255)")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 75 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setStyleSheet("background-color: rgb(255,255,255)")
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page)

        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_4 = QVBoxLayout(self.page_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.page_2)

        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_40 = QVBoxLayout(self.page_3)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.page_3)

        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_41 = QVBoxLayout(self.page_4)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.page_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.label_6)

        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 60))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setStyleSheet("background-color: rgb(255,255,255)")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 75 14pt \"\ub9d1\uc740 \uace0\ub515\";")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(400, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_4)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
        # setupUi

        self.label_2.setStyleSheet(u"image:url({}/{}_{}/frequency/frequency_abs_1.png)"
                                   .format(root_con, self.num, self.name))
        self.label_3.setStyleSheet(u"image:url({}/{}_{}/frequency/frequency_abs_2.png)"
                                   .format(root_con, self.num, self.name))
        self.label_5.setStyleSheet(u"image:url({}/{}_{}/frequency/frequency_rel_1.png)"
                                   .format(root_con, self.num, self.name))
        self.label_6.setStyleSheet(u"image:url({}/{}_{}/frequency/frequency_rel_2.png)"
                                   .format(root_con, self.num, self.name))

        self.pushButton.clicked.connect(lambda: self.next_btn())
        self.pushButton_2.clicked.connect(lambda: self.pre_btn())

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"PSD Absolute Power", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"1/4", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\ub2e4\uc74c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\uc774\uc804", None))
    # retranslateUi

    def pre_btn(self):
        self.page_idx -= 1
        if self.page_idx <= 0:
            self.page_idx = 0
        self.stackedWidget.setCurrentIndex(self.page_idx)
        self.label_4.setText("{}/4".format(self.page_idx + 1))
        if self.page_idx <= 1:
            self.label.setText("PSD Absolute Power")
        else:
            self.label.setText("PSD Relative Power")

    def next_btn(self):
        self.page_idx += 1
        if self.page_idx >= 4:
            self.page_idx = 3
        self.stackedWidget.setCurrentIndex(self.page_idx)
        self.label_4.setText("{}/4".format(self.page_idx + 1))
        if self.page_idx <= 1:
            self.label.setText("PSD Absolute Power")
        else:
            self.label.setText("PSD Relative Power")

