# -*- coding: utf-8 -*-

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from personal_data.resources import *

class Ui_Dialog_feature_detail(QDialog):
    def __init__(self, name, num, feature):
        super().__init__()

        self.name = name
        self.num = num
        self.feature = feature
        if self.feature == "relative":
            self.title = "psd"
        if self.feature == "plv":
            self.title = "fc"
        if self.feature == "network":
            self.title = "ni"

        self.resize(927, 736)
        self.setMaximumSize(927, 736)
        self.setMinimumSize(927, 736)
        self.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 291, 61))
        self.label.setStyleSheet(u"font: 90 28pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 60, 911, 671))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 30))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_15)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 150))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 55))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.frame_8)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 10, 291, 41))
        self.label_16.setStyleSheet(u"font: 90 20pt \"\ub9d1\uc740 \uace0\ub515\";")

        self.verticalLayout.addWidget(self.frame_8)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(170, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.label_19 = QLabel(self.frame_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 75, 100, 15))
        self.label_19.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_20 = QLabel(self.frame_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(110, 75, 56, 15))
        self.label_20.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_21 = QLabel(self.frame_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 135, 100, 15))
        self.label_21.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_22 = QLabel(self.frame_6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 200, 100, 15))
        self.label_22.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_23 = QLabel(self.frame_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 260, 100, 15))
        self.label_23.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_24 = QLabel(self.frame_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 325, 100, 15))
        self.label_24.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_25 = QLabel(self.frame_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(110, 135, 56, 15))
        self.label_25.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_26 = QLabel(self.frame_6)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(110, 200, 56, 15))
        self.label_26.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_27 = QLabel(self.frame_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(110, 260, 56, 15))
        self.label_27.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_28 = QLabel(self.frame_6)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(110, 325, 56, 15))
        self.label_28.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_17)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(70, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.label_18 = QLabel(self.frame_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 75, 56, 15))
        self.label_29 = QLabel(self.frame_7)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(0, 135, 56, 15))
        self.label_30 = QLabel(self.frame_7)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(0, 200, 56, 15))
        self.label_31 = QLabel(self.frame_7)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(0, 260, 56, 15))
        self.label_32 = QLabel(self.frame_7)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(0, 325, 56, 15))

        self.horizontalLayout_3.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

        freq = ['Delta', 'Theta', 'LowAlpha', 'HighAlpha', 'LowBeta', 'HighBeta', 'Gamma']
        text_array = [self.label_9, self.label_10, self.label_11, self.label_12, self.label_13, self.label_14, self.label_15]
        png_array = [self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7, self.label_8]

        for i in range(7):
            text_array[i].setText(freq[i])
            png_array[i].setStyleSheet(u"image:url({}/{}_{}/{}_{}.png)"
                                            .format(root_con, self.num, self.name, self.feature, freq[i]))

        self.label_17.setStyleSheet(u"image:url({}/{}_{}/feature_detail_{})"
                                    .format(root_con, self.num, self.name, self.title))

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"{} Senser Detail".format(self.title.upper()), None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"Feature Position Plot", None))

        ch_list = [self.label_19, self.label_21, self.label_22, self.label_23, self.label_24]
        psd_ch = ["Delta Fp2", "Low Beta P3", "Gamma Fp1", "Low Alpha T7", "Theta C4"]
        fc_ch = ["Low Alpha Fp2-C3", "Gamma O1-Fp2", "Low Alpha P4-O2", "Delta T7-C4", "Theta F3-O2"]
        ni_ch = ["Gamma F4", "Gamma T8", "Delta C4", "Low Beta P8", "High Beta F3"]
        if self.title == "psd":
            for i in range(len(ch_list)):
                ch_list[i].setText(QCoreApplication.translate("Dialog", u"{}".format(psd_ch[i]), None))
        if self.title == "fc":
            for i in range(len(ch_list)):
                ch_list[i].setText(QCoreApplication.translate("Dialog", u"{}".format(fc_ch[i]), None))
        else:
            for i in range(len(ch_list)):
                ch_list[i].setText(QCoreApplication.translate("Dialog", u"{}".format(ni_ch[i]), None))

        mdd_list = [self.label_20, self.label_25, self.label_26, self.label_27, self.label_28]
        hc_list = [self.label_18, self.label_29, self.label_30, self.label_31, self.label_32]
        for i in range(len(mdd_list)):
            mdd_list[i].setText(QCoreApplication.translate("Dialog", u"MDD", None))
            hc_list[i].setText(QCoreApplication.translate("Dialog", u"HC", None))