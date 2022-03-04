# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QSizePolicy, QWidget, QLineEdit, QFileDialog, QPushButton)

class Ui_Dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.resize(495, 335)
        self.setMinimumSize(QSize(200, 200))
        self.setModal(True)
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.lineEdit=QLineEdit(self)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100,70,113,21))

        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(300, 80, 100, 32))
        self.pushButton.clicked.connect(self.open_file) #파일 탐색기 열기

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    # retranslateUi

    # 정보 저장
    def info(self):
        x = self.lineEdit.text()

        return x

    #파일 탐색기 열기
    def open_file(self):  # 열기(O)
        file_name = QFileDialog.getOpenFileName(self)
        print(file_name)
        if file_name[0]:
            with open(file_name[0], encoding='UTF-8') as f:
                text = f.read()
            self.plainTextEdit.setPlainText(text)

        #TODO: 파일 받아오기 (경로)

