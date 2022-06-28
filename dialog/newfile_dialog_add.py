# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *

import os
import json
from dialog.loadingBar import Worker, Ui_Dialog_loading
import personal_data.resources as personal_res


class Ui_Dialog_add(QDialog):
    def __init__(self, dataList):
        super().__init__()
        self.dataList = dataList

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
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_title)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_5 = QLabel(self.frame_title)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font:20pt;")

        self.verticalLayout_12.addWidget(self.label_5)


        self.verticalLayout.addWidget(self.frame_title)

        self.frame_4 = QFrame(self.container)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.comboBox)

        self.frame_19 = QFrame(self.frame_4)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_19)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.lineEdit_6 = QLineEdit(self.frame_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_7.addWidget(self.lineEdit_6)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.clicked.connect(self.search_data)

        self.horizontalLayout_7.addWidget(self.pushButton_2)

        self.verticalLayout.addWidget(self.frame_4)

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
        self.dateEdit = QDateEdit(self.frame_9)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate.currentDate())

        self.horizontalLayout_4.addWidget(self.dateEdit)

        self.verticalLayout_5.addWidget(self.frame_9)

        self.horizontalLayout_3.addWidget(self.frame_5)

        self.verticalLayout.addWidget(self.frame_2)

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

        self.frame_below = QFrame(self.container)
        self.frame_below.setObjectName(u"frame_below")
        self.frame_below.setMaximumSize(QSize(16777215, 40))
        self.frame_below.setFrameShape(QFrame.StyledPanel)
        self.frame_below.setFrameShadow(QFrame.Raised)

        # self.horizontalLayout_8 = QHBoxLayout(self.frame_below)
        # self.horizontalLayout_8.setSpacing(0)
        # self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        # self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        # self.progressBar = QProgressBar(self.frame_below)
        # self.progressBar.setObjectName(u"progressBar")
        # self.progressBar.setMinimumSize(QSize(0, 30))
        # self.progressBar.setMaximumSize(QSize(16777215, 30))
        # self.progressBar.setStyleSheet(u"QProgressBar{\n"
        #                                "	border-style: none;\n"
        #                                "	border-radius: 10px;\n"
        #                                "	text-align: center;\n"
        #                                "	background-color: rgb(235, 235, 235);\n"
        #                                "	margin-left: 20px;\n"
        #                                "	margin-right: 20px;\n"
        #                                "}\n"
        #                                "QProgressBar::chunk{\n"
        #                                "	border-radius: 10px;\n"
        #                                "	background-color: qlineargradient(spread:pad, x1:0, y1:0.472, x2:1, y2:0.472, stop:0 rgba(166, 166, 166, 255), stop:1 rgba(229, 254, 255, 255));\n"
        #                                "}\n"
        #                                "")
        # self.progressBar.setValue(24)
        #
        # self.horizontalLayout_8.addWidget(self.progressBar)

        self.verticalLayout.addWidget(self.frame_below)

        self.buttonBox = QDialogButtonBox(self.container)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.horizontalLayout.addWidget(self.container)


        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.safe_code)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("", u"\ub370\uc774\ud130, \uac1c\uc778\uc815\ubcf4\uc785\ub825", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\ud655\uc7a5\uc790 \uc120\ud0dd", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u".cnt", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u".cdt", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u".mat", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u".mff", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Dialog", u"\uc120\ud0dd", None))
        self.pushButton.setText(QCoreApplication.translate("", u"\uc5c5\ub85c\ub4dc", None))
        self.pushButton_2.setText(QCoreApplication.translate("", u"search", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\ud658\uc790 \uac80\uc0c9:", None))
        self.label_3.setText(QCoreApplication.translate("", u"\uc774\ub984", None))
        self.label_7.setText(QCoreApplication.translate("", u"\ub098\uc774", None))
        self.label_4.setText(QCoreApplication.translate("", u"\uc131\ubcc4", None))
        self.radioButton_3.setText(QCoreApplication.translate("", u"\ub0a8\uc131", None))
        self.radioButton_4.setText(QCoreApplication.translate("", u"\uc5ec\uc131", None))
        self.label.setText(QCoreApplication.translate("", u"\ub4f1\ub85d\ubc88\ud638", None))
        self.label_2.setText(QCoreApplication.translate("", u"\uac80\uc0ac\uc77c\uc2dc", None))
    # retranslateUi

    def search_data(self):
        value = self.lineEdit_6.text()

        detect_val = False
        for s in self.dataList:
            s_split = s.split('_')
            if s_split[0] == value or s_split[1] == value:
                detect_val = s
                break

        if not detect_val:
            print("no result")
            # QmessageBox
            information = "환자 데이터의 ID나 이름을 잘 확인해보세요!"
            msgBox = QMessageBox()
            msgBox.setWindowTitle("NO DATA")
            msgBox.setText("해당 데이터 없음.")
            msgBox.setInformativeText(information)
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setDefaultButton(QMessageBox.Ok)
            result = msgBox.exec()

        else:
            with open(os.path.join(personal_res.root, '{}/info.json'.format(detect_val)), 'r', encoding='utf-8') as f:
                info_json_path = json.load(f)
            self.lineEdit_3.setText(info_json_path['name'])
            self.lineEdit_5.setText(info_json_path['birth'])
            self.lineEdit_2.setText(info_json_path['num'])
            dateList = info_json_path['date'].split("-")
            self.dateEdit.setDate(QDate(int(dateList[0]), int(dateList[1]), int(dateList[2])))
            if info_json_path['sex'] == '남성':
                self.radioButton_3.setChecked(True)
            else:
                self.radioButton_4.setChecked(True)

    # 정보 저장
    def info(self):
        file = self.lineEdit.text()
        name = self.lineEdit_3.text()
        birth = self.lineEdit_5.text()
        num = self.lineEdit_2.text()
        date = self.dateEdit.text()
        if self.radioButton_3.isChecked():
            sex = '남성'
        elif self.radioButton_4.isChecked():
            sex = '여성'
        else:
            sex = 0

        return file, name, birth, num, date, sex

    def safe_code(self):
        file, name, birth, num, date, sex = self.info()
        if file and name and birth and num and date and sex:
            self.accept()
        else:
            # QmessageBox
            information = "모든 데이터를 입력하세요!"
            msgBox = QMessageBox()
            msgBox.setWindowTitle("ERROR")
            msgBox.setText("데이터 입력")
            msgBox.setInformativeText(information)
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setDefaultButton(QMessageBox.Ok)
            result = msgBox.exec()

    # 파일 탐색기 열기
    def open_file(self):  # 열기(O)
        file_format = "Data Files (*{});; All Files(*.*)".format(self.comboBox.currentText())
        file_name = QFileDialog.getOpenFileName(self,self.tr("Open Data files"), "./", self.tr(file_format))
        print(file_name)
        self.lineEdit.setText(file_name[0])


