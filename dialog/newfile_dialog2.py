# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *


class Ui_Dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.resize(450, 500)
        self.setMinimumSize(QSize(450, 500))
        self.setMaximumSize(QSize(450, 500))
        self.setModal(True)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.container = QFrame(self)
        self.container.setObjectName(u"container")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_title = QFrame(self.container)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMaximumSize(QSize(16777215, 40))
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_title)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_5 = QLabel(self.frame_title)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_12.addWidget(self.label_5)


        self.verticalLayout.addWidget(self.frame_title)

        self.frame_1 = QFrame(self.container)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.frame_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self.open_file)  # 파일 탐색기 열기

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.lineEdit = QLineEdit(self.frame_1)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout.addWidget(self.frame_1)

        self.frame_3 = QFrame(self.container)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_8.addWidget(self.label_3)


        self.verticalLayout_7.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lineEdit_3 = QLineEdit(self.frame_12)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaxLength(20)
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setDragEnabled(True)
        self.lineEdit_3.setClearButtonEnabled(False)

        self.verticalLayout_9.addWidget(self.lineEdit_3)


        self.verticalLayout_7.addWidget(self.frame_12)


        self.horizontalLayout_5.addWidget(self.frame_10)

        self.frame_16 = QFrame(self.frame_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_16)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_18)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_7 = QLabel(self.frame_18)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_15.addWidget(self.label_7)


        self.verticalLayout_13.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_17)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.lineEdit_5 = QLineEdit(self.frame_17)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_14.addWidget(self.lineEdit_5)


        self.verticalLayout_13.addWidget(self.frame_17)


        self.horizontalLayout_5.addWidget(self.frame_16)

        self.frame_13 = QFrame(self.frame_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_11.addWidget(self.label_4)


        self.verticalLayout_10.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radioButton_3 = QRadioButton(self.frame_15)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_6.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.frame_15)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_6.addWidget(self.radioButton_4)

        self.verticalLayout_10.addWidget(self.frame_15)


        self.horizontalLayout_5.addWidget(self.frame_13)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lineEdit_2 = QLineEdit(self.frame_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaxLength(50)

        self.verticalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_4 = QLineEdit(self.frame_9)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_4.addWidget(self.lineEdit_4)


        self.verticalLayout_5.addWidget(self.frame_9)


        self.horizontalLayout_3.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_below = QFrame(self.container)
        self.frame_below.setObjectName(u"frame_below")
        self.frame_below.setMaximumSize(QSize(16777215, 40))
        self.frame_below.setFrameShape(QFrame.StyledPanel)
        self.frame_below.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_below)

        self.buttonBox = QDialogButtonBox(self.container)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.horizontalLayout.addWidget(self.container)


        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("", u"\ub370\uc774\ud130, \uac1c\uc778\uc815\ubcf4\uc785\ub825", None))
        self.pushButton.setText(QCoreApplication.translate("", u"\uc5c5\ub85c\ub4dc", None))
        self.label_3.setText(QCoreApplication.translate("", u"\uc774\ub984", None))
        self.label_7.setText(QCoreApplication.translate("", u"\uc0dd\ub144\uc6d4\uc77c", None))
        self.label_4.setText(QCoreApplication.translate("", u"\uc131\ubcc4", None))
        self.radioButton_3.setText(QCoreApplication.translate("", u"\ub0a8\uc131", None))
        self.radioButton_4.setText(QCoreApplication.translate("", u"\uc5ec\uc131", None))
        self.label.setText(QCoreApplication.translate("", u"\ub4f1\ub85d\ubc88\ud638", None))
        self.label_2.setText(QCoreApplication.translate("", u"\uac80\uc0ac\uc77c\uc2dc", None))
    # retranslateUi

    # 정보 저장
    def info(self):
        file = self.lineEdit.text()
        name = self.lineEdit_3.text()
        birth = self.lineEdit_5.text()
        num = self.lineEdit_2.text()
        date = self.lineEdit_4.text()
        if self.radioButton_3.isChecked():
            sex = '남성'
        if self.radioButton_4.isChecked():
            sex = '여성'

        return file, name, birth, num, date, sex

    # 파일 탐색기 열기
    def open_file(self):  # 열기(O)
        file_name = QFileDialog.getOpenFileName(self)
        print(file_name)
        self.lineEdit.setText(file_name[0])
        # if file_name[0]:
        #     with open(file_name[0], encoding='UTF-8') as f:
        #         text = f.read()
        #     # self.plainTextEdit.setPlainText(text)

        # TODO: 파일 받아오기 (경로)

