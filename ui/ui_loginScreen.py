# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginScreenWNilED.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6 import QtGui, QtCore
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        self.btn_cmm = 20
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(1350, 900)
        MainWindow.setMinimumSize(QSize(1350, 900))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.setSpacing(0)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.drop_frame = QFrame(self.centralwidget)
        self.drop_frame.setObjectName(u"drop_frame")
        self.drop_frame.setStyleSheet(u"border-radius:0px;\n"
"background-color: rgb(255, 255, 255);")
        self.drop_frame.setFrameShape(QFrame.StyledPanel)
        self.drop_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.drop_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.drop_frame)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.content)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.content_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.content_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 40))
        self.title_bar.setMaximumSize(QSize(16777215, 40))
        self.title_bar.setStyleSheet(u"background-color: rgb(230, 230, 230);title")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 0))
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_title)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(15, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        # font.setFamilies([u"Franklin Gothic Heavy"])
        font.setPointSize(12)
        self.label_title.setFont(font)

        self.verticalLayout_6.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMinimumSize(QSize(120, 0))
        self.frame_btns.setMaximumSize(QSize(120, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.btn_min = QPushButton(self.frame_btns)
        self.btn_min.setObjectName(u"btn_min")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_min.sizePolicy().hasHeightForWidth())
        self.btn_min.setSizePolicy(sizePolicy)
        # self.btn_min.setMinimumSize(QSize(40, 30))
        # self.btn_min.setMaximumSize(QSize(40, 30))
        self.btn_min.setIcon(QtGui.QIcon("./icon/mini.png"))
        self.btn_min.setIconSize(QtCore.QSize(self.btn_cmm, self.btn_cmm))
        self.btn_min.setStyleSheet(u"QPushButton {\n"
                                   "	border:none;\n"
                                   "	border-radius: 3px;\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "	\n"
                                   "	background-color: rgba(85, 255, 127, 150);\n"
                                   "}")

        self.horizontalLayout_3.addWidget(self.btn_min)

        self.btn_max = QPushButton(self.frame_btns)
        self.btn_max.setObjectName(u"btn_max")
        self.btn_max.setSizePolicy(sizePolicy)
        # self.btn_max.setMinimumSize(QSize(40, 20))
        # self.btn_max.setMaximumSize(QSize(40, 20))
        self.btn_max.setIcon(QtGui.QIcon("./icon/maxi.png"))
        self.btn_max.setIconSize(QtCore.QSize(self.btn_cmm, self.btn_cmm))
        self.btn_max.setStyleSheet(u"QPushButton {\n"
                                   "	border:none;\n"
                                   "	border-radius: 3px;\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "	\n"
                                   "	background-color: rgba(255, 170, 0, 150);\n"
                                   "}")

        self.horizontalLayout_3.addWidget(self.btn_max)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setSizePolicy(sizePolicy)
        # self.btn_close.setMinimumSize(QSize(40, 20))
        # self.btn_close.setMaximumSize(QSize(40, 20))
        self.btn_close.setIcon(QtGui.QIcon("./icon/close.png"))
        self.btn_close.setIconSize(QtCore.QSize(self.btn_cmm, self.btn_cmm))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
                                     "	border:none;\n"
                                     "	border-radius: 3px;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "	\n"
                                     "	background-color: rgba(255,0, 0, 150);\n"
                                     "}")

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.frame = QFrame(self.content_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(55, 55, 56);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 80))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 200))
        self.frame_3.setMinimumSize(QSize(0, 200))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 800 90pt;\n"
                                 "color: rgb(255,255,255);")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.label.setMargin(0)

        self.horizontalLayout_6.addWidget(self.label)

        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(160, 16777215))
        self.label_2.setStyleSheet(u"font: 60pt;\n"
                                   "color: rgb(255,255,255);")
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_2.setMargin(8)

        self.horizontalLayout_6.addWidget(self.label_2)


        self.horizontalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_9)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setMinimumSize(QSize(0, 350))
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(250, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_11.setMinimumSize(QSize(700, 350))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy1)

        self.verticalLayout_3 = QVBoxLayout(self.frame_11)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 120))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_13)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 17pt;\n"
                                   "color: rgb(255,255,255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.verticalLayout_3.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_15)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 30, -1, 30)
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.frame_17)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(160, 16777215))
        self.label_4.setStyleSheet(u"font: 18pt;\n"
                                   "color: rgb(255,255,255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.IDInput = QLineEdit(self.frame_17)
        self.IDInput.setObjectName(u"IDInput")
        self.IDInput.setMinimumSize(QSize(230, 0))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.IDInput.sizePolicy().hasHeightForWidth())
        self.IDInput.setSizePolicy(sizePolicy1)
        # self.IDInput.setStyleSheet(u"background-color: rgb(208, 206, 210);")
        self.IDInput.setStyleSheet(u"border: 2px solid;\n"
                                         "height: 30px;\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "font-size: 20px;\n"
                                         "color: rgb(0,0,0);\n"
                                         "border-radius: 7px;\n")

        self.horizontalLayout_8.addWidget(self.IDInput)


        self.verticalLayout_7.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.frame_18)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(160, 16777215))
        self.label_5.setStyleSheet(u"font: 18pt;\n"
                                   "color: rgb(255,255,255);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_5)

        self.passwordInput = QLineEdit(self.frame_18)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setMinimumSize(QSize(230, 0))
        sizePolicy1.setHeightForWidth(self.passwordInput.sizePolicy().hasHeightForWidth())
        self.passwordInput.setSizePolicy(sizePolicy1)
        # self.passwordInput.setStyleSheet(u"background-color: rgb(208, 206, 210);")
        self.passwordInput.setStyleSheet(u"border: 2px solid;\n"
                                    "height: 30px;\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "font-size: 20px;\n"
                                    "color: rgb(0,0,0);\n"
                                    "border-radius: 7px;\n")
        self.passwordInput.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_9.addWidget(self.passwordInput)


        self.verticalLayout_7.addWidget(self.frame_18)


        self.horizontalLayout_7.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(250, 16777215))
        self.frame_16.setMinimumSize(QSize(250, 0))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(50, 50, 50, 50)
        self.btn_login = QPushButton(self.frame_16)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy2)
        self.btn_login.setStyleSheet(u"background-color: rgb(132, 172, 255);\n"
                                     "font-size: 20px;\n"
                                     "border-radius: 7px;")

        self.horizontalLayout_10.addWidget(self.btn_login)


        self.horizontalLayout_7.addWidget(self.frame_16)


        self.verticalLayout_3.addWidget(self.frame_14)


        self.horizontalLayout_5.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(250, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_12)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 100))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_19 = QFrame(self.frame_6)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_6)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(250, 16777215))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_20)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.littleLogo = QLabel(self.frame_20)
        self.littleLogo.setObjectName(u"littleLogo")
        self.littleLogo.setAlignment(Qt.AlignCenter)
        # self.littleLogo.setStyleSheet(u"image:url(./icon/bwave_logo_2.png)")

        self.verticalLayout_8.addWidget(self.littleLogo)


        self.horizontalLayout_11.addWidget(self.frame_20)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.content_frame)


        self.verticalLayout_5.addWidget(self.content)


        self.layout.addWidget(self.drop_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Maumgyeol - Depression    ver. 1.0.0", None))
#if QT_CONFIG(tooltip)
#         self.btn_min.setToolTip(QCoreApplication.translate("MainWindow", u"\ucd5c\uc18c\ud654", None))
# #endif // QT_CONFIG(tooltip)
#         self.btn_min.setText(QCoreApplication.translate("MainWindow", u"\ucd5c\uc18c", None))
# #if QT_CONFIG(tooltip)
#         self.btn_max.setToolTip(QCoreApplication.translate("MainWindow", u"\ucd5c\ub300\ud654", None))
# #endif // QT_CONFIG(tooltip)
#         self.btn_max.setText(QCoreApplication.translate("MainWindow", u"\ucd5c\ub300", None))
# #if QT_CONFIG(tooltip)
#         self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"\ub2eb\uae30", None))
# #endif // QT_CONFIG(tooltip)
#         self.btn_close.setText(QCoreApplication.translate("MainWindow", u"\ub2eb\uae30", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Maumgyeol", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pro", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"An EEG Analysis Platform\n"
"AI Diagnostics Software - Depression", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.littleLogo.setText(QCoreApplication.translate("MainWindow", u"", None))
    # retranslateUi

