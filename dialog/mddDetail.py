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

from personal_data.resources import *


class Ui_Dialog_mdd_Detail(QDialog):
    def __init__(self, name, num):
        super().__init__()

        self.name = name
        self.num = num

        self.resize(610, 800)
        self.setMaximumSize(610, 800)
        self.setMinimumSize(610, 800)
        self.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 301, 61))
        self.label.setStyleSheet(u"font: 90 28pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 501, 31))
        self.label_2.setStyleSheet(u"font: 90 24pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 110, 611, 681))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 121, 31))
        self.label_3.setStyleSheet(u"font: 90 16pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(95, 45, 56, 12))
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 60, 170, 170))
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(280, 45, 56, 12))
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(220, 60, 170, 170))
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(455, 45, 65, 12))
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(400, 60, 170, 170))
        self.label_9.setAlignment(Qt.AlignCenter)
        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(140, 27, 400, 3))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(440, 45, 95, 12))
        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(400, 60, 170, 170))
        self.label_18.setAlignment(Qt.AlignCenter)
        self.line_3 = QFrame(self.frame_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(110, 27, 430, 3))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(265, 45, 90, 12))
        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 10, 121, 31))
        self.label_20.setStyleSheet(u"font: 90 16pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(90, 45, 90, 12))
        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(220, 60, 170, 170))
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(40, 60, 170, 170))
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.line_4 = QFrame(self.frame_4)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(110, 27, 430, 3))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.label_24 = QLabel(self.frame_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(400, 60, 170, 170))
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_25 = QLabel(self.frame_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(220, 60, 170, 170))
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_26 = QLabel(self.frame_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(460, 45, 56, 12))
        self.label_27 = QLabel(self.frame_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(96, 45, 65, 12))
        self.label_28 = QLabel(self.frame_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 10, 121, 31))
        self.label_28.setStyleSheet(u"font: 90 16pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_29 = QLabel(self.frame_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(280, 45, 56, 12))
        self.label_30 = QLabel(self.frame_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(40, 60, 170, 170))
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame_4)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
        # setupUi

        ## PSD
        self.label_5.setStyleSheet(u"image:url({}/{}_{}/psd_detail_0.png)".format(root_con, self.num, self.name))
        self.label_7.setStyleSheet(u"image:url({}/{}_{}/psd_detail_1.png)".format(root_con, self.num, self.name))
        self.label_9.setStyleSheet(u"image:url({}/{}_{}/psd_detail_2.png)".format(root_con, self.num, self.name))

        ## FC
        self.label_23.setStyleSheet(u"image:url({}/{}_{}/plv_detail_0.png)".format(root_con, self.num, self.name))
        self.label_22.setStyleSheet(u"image:url({}/{}_{}/plv_detail_1.png)".format(root_con, self.num, self.name))
        self.label_18.setStyleSheet(u"image:url({}/{}_{}/plv_detail_2.png)".format(root_con, self.num, self.name))

        ## NI
        self.label_30.setStyleSheet(u"image:url({}/{}_{}/ni_detail_0.png)".format(root_con, self.num, self.name))
        self.label_25.setStyleSheet(u"image:url({}/{}_{}/ni_detail_1.png)".format(root_con, self.num, self.name))
        self.label_24.setStyleSheet(u"image:url({}/{}_{}/ni_detail_2.png)".format(root_con, self.num, self.name))

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Probability Detail", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Most Influential 3 Features", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"PSD-Senser", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Theta Fp1", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Theta Pz", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Gamma Fp1", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Low Beta Fp1-O2", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Gamma FZ-P3", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"FC-Senser", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"Delta C2-T8", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"Theta F7", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"Gamma Pz", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"NI-Senser", None))
        self.label_29.setText(QCoreApplication.translate("Dialog", u"Theta Fp2", None))
    # retranslateUi


