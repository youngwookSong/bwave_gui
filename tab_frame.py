from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *

class Ui_tabFrame(QFrame):
    def __init__(self, current_tab, file, name, birth, num, date, sex, y_pred, y_pred_proba):
        super().__init__()
        self.current_tab = current_tab
        self.file = file
        self.name = name
        self.birth = birth
        self.num = num
        self.date = date
        self.sex = sex
        self.y_pred = y_pred
        self.y_pred_proba = y_pred_proba

        self.verticalLayout_10 = QVBoxLayout(self.current_tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_12 = QFrame(self.current_tab)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 70))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setSpacing(4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_13)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label = QLabel(self.frame_13)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label)

        self.horizontalLayout_7.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_14)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_2 = QLabel(self.frame_14)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_2)

        self.horizontalLayout_7.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_15)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_3 = QLabel(self.frame_15)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_3)

        self.horizontalLayout_7.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_12)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_16)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_4 = QLabel(self.frame_16)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_4)

        self.horizontalLayout_7.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_12)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_17)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_5 = QLabel(self.frame_17)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_5)

        self.horizontalLayout_7.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_12)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_18)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_6 = QLabel(self.frame_18)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_6)

        self.horizontalLayout_7.addWidget(self.frame_18)

        self.verticalLayout_10.addWidget(self.frame_12)

        self.frame_6 = QFrame(self.current_tab)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_8)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_8)


        self.horizontalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_9)

        self.verticalLayout_10.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.current_tab)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_11)

        self.verticalLayout_10.addWidget(self.frame_7)

        self.retranslateUi(self)

    def retranslateUi(self, MainWindow):

        self.label.setText(QCoreApplication.translate("MainWindow", self.file, None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", self.name, None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", self.birth, None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", self.num, None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", self.date, None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", self.sex, None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", self.y_pred, None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", self.y_pred_proba, None))

        # retranslateUi

        # self.label.setText((QCoreApplication.translate("MainWindow", self.file, None)))
        # self.label_2.setText((QCoreApplication.translate("MainWindow", self.name, None)))