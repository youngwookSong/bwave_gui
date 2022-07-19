from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *

import personal_data.resources as personal_res
from dialog.psdPowerHz import Ui_Dialog_power
from dialog.source_plot import Ui_Dialog_source
from dialog.trDetail import Ui_Dialog_trDetail

from style import *
from personal_data.resources import *
from model_Test.directory import ROOT_DIR_con

import json
import os
import mne


class Ui_tabFrame_pre(QFrame):
    def __init__(self, current_tab, file, name, birth, num, date, sex, y_pred, y_pred_proba_mdd, y_pred_proba_hc,
                 best_model, tr, psd_sen, fc_sen, ni_sen, psd_sou, fc_sou, ni_sou):
        super().__init__()
        self.current_tab = current_tab
        self.file = file
        self.name = name
        self.birth = birth
        self.num = num
        self.date = date
        self.sex = sex
        self.y_pred = y_pred
        self.y_pred_proba_mdd = y_pred_proba_mdd
        self.y_pred_proba_hc = y_pred_proba_hc
        self.best_model = best_model
        self.tr = tr
        self.psd_sen = psd_sen
        self.fc_sen = fc_sen
        self.ni_sen = ni_sen
        self.psd_sou = psd_sou
        self.fc_sou = fc_sou
        self.ni_sou = ni_sou

        # 6개 원 그래프를 위한 변수
        self.circularProgressCoordinate = [5, 20, 120, 120]
        self.circularBgCoordinate = [5, 20, 120, 120]
        self.containerCoordinate = [20, 35, 90, 90]
        self.labelTitleCoordinate = [2, 0, 61, 35]
        self.labelPercentageCoordinate = [20, 40, 61, 50]

        self.data = None

        self.verticalLayout_6 = QVBoxLayout(self.current_tab)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.tab_pages = QStackedWidget(self.current_tab)
        self.tab_pages.setObjectName(u"tab_pages")
        self.tab_pages.setStyleSheet(u"background-color: rgb(255,255,255);")

        self.tabFrame_pre = QWidget()
        self.tabFrame_pre.setObjectName(u"tabFrame_pre")
        self.verticalLayout_tabpre = QVBoxLayout(self.tabFrame_pre)
        self.verticalLayout_tabpre.setSpacing(0)
        self.verticalLayout_tabpre.setObjectName(u"verticalLayout_tabpre")
        self.verticalLayout_tabpre.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.tabFrame_pre)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy3)
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.frame_38)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_28 = QLabel(self.frame_43)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_28.setStyleSheet(u"font-style: bold;")

        self.horizontalLayout_25.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_43)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_25.addWidget(self.label_29)

        self.horizontalLayout_20.addWidget(self.frame_43)

        self.frame_42 = QFrame(self.frame_38)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_26 = QLabel(self.frame_42)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_26.setStyleSheet(u"font-style: bold;")

        self.horizontalLayout_24.addWidget(self.label_26)

        self.label_27 = QLabel(self.frame_42)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_24.addWidget(self.label_27)

        self.horizontalLayout_20.addWidget(self.frame_42)

        self.frame_41 = QFrame(self.frame_38)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_24 = QLabel(self.frame_41)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_24.setStyleSheet(u"font-style: bold;")

        self.horizontalLayout_23.addWidget(self.label_24)

        self.label_25 = QLabel(self.frame_41)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_23.addWidget(self.label_25)

        self.horizontalLayout_20.addWidget(self.frame_41)

        self.frame_45 = QFrame(self.frame_38)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_22 = QLabel(self.frame_45)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_22.setStyleSheet(u"font-style: bold;")

        self.horizontalLayout_22.addWidget(self.label_22)

        self.label_23 = QLabel(self.frame_45)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_22.addWidget(self.label_23)

        self.horizontalLayout_20.addWidget(self.frame_45)

        self.frame_40 = QFrame(self.frame_38)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_20 = QLabel(self.frame_40)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_20.setStyleSheet(u"font-style: bold;")

        self.horizontalLayout_21.addWidget(self.label_20)

        self.label_21 = QLabel(self.frame_40)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_21.addWidget(self.label_21)

        self.horizontalLayout_20.addWidget(self.frame_40)

        self.verticalLayout_tabpre.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.tabFrame_pre)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)

        self.frame_46 = QFrame(self.frame_39)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_46)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QFrame(self.frame_46)
        self.frame_48.setObjectName(u"frame_48")
        sizePolicy3.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        self.frame_48.setSizePolicy(sizePolicy3)
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 9, 0, 0)
        self.label_30 = QLabel(self.frame_48)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_30)

        self.label_31 = QLabel(self.frame_48)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_31)

        self.label_32 = QLabel(self.frame_48)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_32)

        self.label_32_h = QLabel(self.frame_48)
        self.label_32_h.setObjectName(u"label_32_h")
        self.label_32_h.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_32_h)

        self.label_33 = QLabel(self.frame_48)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_33)

        self.label_33_h = QLabel(self.frame_48)
        self.label_33_h.setObjectName(u"label_33_h")
        self.label_33_h.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_33_h)

        self.label_34 = QLabel(self.frame_48)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_34)

        self.verticalLayout_22.addWidget(self.frame_48)

        self.frame_50 = QFrame(self.frame_46)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_50)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.frame_50)
        self.label_41.setObjectName(u"label_41")
        sizePolicy3.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy3)
        self.label_41.setStyleSheet(u"margin-left: 10px;")

        self.verticalLayout_24.addWidget(self.label_41)

        self.frame_55 = QFrame(self.frame_50)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.A_delta = QLabel(self.frame_55)
        self.A_delta.setObjectName(u"A_delta")
        self.A_delta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.A_delta)

        self.A_theta = QLabel(self.frame_55)
        self.A_theta.setObjectName(u"A_theta")
        self.A_theta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.A_theta)

        self.A_LowAlpha = QLabel(self.frame_55)
        self.A_LowAlpha.setObjectName(u"A_LowAlpha")
        self.A_LowAlpha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.A_LowAlpha)

        self.A_HighAlpha = QLabel(self.frame_55)
        self.A_HighAlpha.setObjectName(u"A_HighAlpha")
        self.A_HighAlpha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.A_HighAlpha)

        self.A_LowBeta = QLabel(self.frame_55)
        self.A_LowBeta.setObjectName(u"A_LowBeta")
        self.A_LowBeta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.A_LowBeta)

        self.A_HighBeta = QLabel(self.frame_55)
        self.A_HighBeta.setObjectName(u"A_HighBeta")
        self.A_HighBeta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.A_HighBeta)

        self.A_Gamma = QLabel(self.frame_55)
        self.A_Gamma.setObjectName(u"A_Gamma")
        self.A_Gamma.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.A_Gamma)

        self.verticalLayout_24.addWidget(self.frame_55)

        self.verticalLayout_22.addWidget(self.frame_50)

        self.frame_53 = QFrame(self.frame_46)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_53)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.frame_53)
        self.label_59.setObjectName(u"label_59")
        sizePolicy3.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy3)
        self.label_59.setStyleSheet(u"margin-left: 10px;")

        self.verticalLayout_27.addWidget(self.label_59)

        self.frame_58 = QFrame(self.frame_53)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.R_delta = QLabel(self.frame_58)
        self.R_delta.setObjectName(u"R_delta")
        self.R_delta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.R_delta)

        self.R_theta = QLabel(self.frame_58)
        self.R_theta.setObjectName(u"R_theta")
        self.R_theta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.R_theta)

        self.R_Lowalpha = QLabel(self.frame_58)
        self.R_Lowalpha.setObjectName(u"R_Lowalpha")
        self.R_Lowalpha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.R_Lowalpha)

        self.R_Highalpha = QLabel(self.frame_58)
        self.R_Highalpha.setObjectName(u"R_Highalpha")
        self.R_Highalpha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.R_Highalpha)

        self.R_Lowbeta = QLabel(self.frame_58)
        self.R_Lowbeta.setObjectName(u"R_Lowbeta")
        self.R_Lowbeta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.R_Lowbeta)

        self.R_Highbeta = QLabel(self.frame_58)
        self.R_Highbeta.setObjectName(u"R_Highbeta")
        self.R_Highbeta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.R_Highbeta)

        self.R_gamma = QLabel(self.frame_58)
        self.R_gamma.setObjectName(u"R_gamma")
        self.R_gamma.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.R_gamma)

        self.verticalLayout_27.addWidget(self.frame_58)

        self.verticalLayout_22.addWidget(self.frame_53)

        self.frame_52 = QFrame(self.frame_46)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_52)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.frame_52)
        self.label_53.setObjectName(u"label_53")
        sizePolicy3.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy3)
        self.label_53.setStyleSheet(u"margin-left: 10px;")

        self.verticalLayout_26.addWidget(self.label_53)

        self.frame_57 = QFrame(self.frame_52)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.plv_delta = QLabel(self.frame_57)
        self.plv_delta.setObjectName(u"plv_delta")
        self.plv_delta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.plv_delta)

        self.plv_theta = QLabel(self.frame_57)
        self.plv_theta.setObjectName(u"plv_theta")
        self.plv_theta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.plv_theta)

        self.plv_Lowalpha = QLabel(self.frame_57)
        self.plv_Lowalpha.setObjectName(u"plv_Lowalpha")
        self.plv_Lowalpha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.plv_Lowalpha)

        self.plv_Highalpha = QLabel(self.frame_57)
        self.plv_Highalpha.setObjectName(u"plv_Highalpha")
        self.plv_Highalpha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.plv_Highalpha)

        self.plv_Lowbeta = QLabel(self.frame_57)
        self.plv_Lowbeta.setObjectName(u"plv_Lowbeta")
        self.plv_Lowbeta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.plv_Lowbeta)

        self.plv_Highbeta = QLabel(self.frame_57)
        self.plv_Highbeta.setObjectName(u"plv_Highbeta")
        self.plv_Highbeta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.plv_Highbeta)

        self.plv_gamma = QLabel(self.frame_57)
        self.plv_gamma.setObjectName(u"plv_gamma")
        self.plv_gamma.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.plv_gamma)

        self.verticalLayout_26.addWidget(self.frame_57)

        self.verticalLayout_22.addWidget(self.frame_52)

        self.frame_51 = QFrame(self.frame_46)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_51)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.frame_51)
        self.label_47.setObjectName(u"label_47")
        sizePolicy3.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy3)
        self.label_47.setStyleSheet(u"margin-left: 10px;")

        self.verticalLayout_25.addWidget(self.label_47)

        self.frame_56 = QFrame(self.frame_51)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.wp_delta = QLabel(self.frame_56)
        self.wp_delta.setObjectName(u"wp_delta")
        self.wp_delta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.wp_delta)

        self.wp_theta = QLabel(self.frame_56)
        self.wp_theta.setObjectName(u"wp_theta")
        self.wp_theta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.wp_theta)

        self.wp_Lowalpha = QLabel(self.frame_56)
        self.wp_Lowalpha.setObjectName(u"wp_Lowalpha")
        self.wp_Lowalpha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.wp_Lowalpha)

        self.wp_Highalpha = QLabel(self.frame_56)
        self.wp_Highalpha.setObjectName(u"wp_Highalpha")
        self.wp_Highalpha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.wp_Highalpha)

        self.wp_Lowbeta = QLabel(self.frame_56)
        self.wp_Lowbeta.setObjectName(u"wp_Lowbeta")
        self.wp_Lowbeta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.wp_Lowbeta)

        self.wp_Highbeta = QLabel(self.frame_56)
        self.wp_Highbeta.setObjectName(u"wp_Highbeta")
        self.wp_Highbeta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.wp_Highbeta)

        self.wp_gamma = QLabel(self.frame_56)
        self.wp_gamma.setObjectName(u"wp_gamma")
        self.wp_gamma.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.wp_gamma)

        self.verticalLayout_25.addWidget(self.frame_56)

        self.verticalLayout_22.addWidget(self.frame_51)

        self.frame_49 = QFrame(self.frame_46)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_49)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_49)
        self.label_35.setObjectName(u"label_35")
        sizePolicy3.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy3)
        self.label_35.setStyleSheet(u"margin-left: 10px;")

        self.verticalLayout_23.addWidget(self.label_35)

        self.frame_54 = QFrame(self.frame_49)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.n_delta = QLabel(self.frame_54)
        self.n_delta.setObjectName(u"n_delta")
        self.n_delta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.n_delta)

        self.n_theta = QLabel(self.frame_54)
        self.n_theta.setObjectName(u"n_theta")
        self.n_theta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.n_theta)

        self.n_Lowalpha = QLabel(self.frame_54)
        self.n_Lowalpha.setObjectName(u"n_Lowalpha")
        self.n_Lowalpha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.n_Lowalpha)

        self.n_Highalpha = QLabel(self.frame_54)
        self.n_Highalpha.setObjectName(u"n_Highalpha")
        self.n_Highalpha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.n_Highalpha)

        self.n_Lowbeta = QLabel(self.frame_54)
        self.n_Lowbeta.setObjectName(u"n_Lowbeta")
        self.n_Lowbeta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.n_Lowbeta)

        self.n_Highbeta = QLabel(self.frame_54)
        self.n_Highbeta.setObjectName(u"n_Highbeta")
        self.n_Highbeta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.n_Highbeta)

        self.n_gamma = QLabel(self.frame_54)
        self.n_gamma.setObjectName(u"n_gamma")
        self.n_gamma.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.n_gamma)

        self.verticalLayout_23.addWidget(self.frame_54)

        self.verticalLayout_22.addWidget(self.frame_49)

        self.horizontalLayout_26.addWidget(self.frame_46)


        self.verticalLayout_tabpre.addWidget(self.frame_39)

        self.tab_pages.addWidget(self.tabFrame_pre)
        ## ----------------------------------------------두번째 페이지

        self.tabFrame_anal = QWidget()
        self.tabFrame_anal.setObjectName(u"tabFrame_anal")
        self.verticalLayout_10 = QVBoxLayout(self.tabFrame_anal)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.tabFrame_anal)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy3)
        self.frame_12.setMaximumSize(QSize(16777215, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.frame_left_mar = QFrame(self.frame_12)
        self.frame_left_mar.setObjectName(u"frame_left_mar")
        self.frame_left_mar.setFrameShape(QFrame.StyledPanel)
        self.frame_left_mar.setFrameShadow(QFrame.Raised)
        self.frame_left_mar.setMaximumSize(50, 16777215)
        self.horizontalLayout_7.addWidget(self.frame_left_mar)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_45 = QLabel(self.frame_13)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"font: 75 11pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_45.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_35.addWidget(self.label_45)

        self.label = QLabel(self.frame_13)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label.setStyleSheet(u"font: 75 11pt \"\ub9d1\uc740 \uace0\ub515\";")

        self.horizontalLayout_35.addWidget(self.label)

        self.horizontalLayout_7.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_46 = QLabel(self.frame_14)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"font: 75 11pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_46.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_46)

        self.label_2 = QLabel(self.frame_14)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_2.setStyleSheet(u"font: 75 11pt \"\ub9d1\uc740 \uace0\ub515\";")

        self.horizontalLayout_36.addWidget(self.label_2)

        self.horizontalLayout_7.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_48 = QLabel(self.frame_15)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"font: 75 11pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_48.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.label_48)

        self.label_3 = QLabel(self.frame_15)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_3.setStyleSheet(u"font: 75 11pt \"\ub9d1\uc740 \uace0\ub515\";")

        self.horizontalLayout_37.addWidget(self.label_3)

        self.horizontalLayout_7.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_12)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_49 = QLabel(self.frame_16)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"font: 75 11pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_49.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.label_49)

        self.label_4 = QLabel(self.frame_16)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_4.setStyleSheet(u"font: 75 11pt \"\ub9d1\uc740 \uace0\ub515\";")

        self.horizontalLayout_38.addWidget(self.label_4)

        self.horizontalLayout_7.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_12)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_50 = QLabel(self.frame_17)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"font: 75 11pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_50.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.label_50)

        self.label_5 = QLabel(self.frame_17)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_5.setStyleSheet(u"font: 75 11pt \"\ub9d1\uc740 \uace0\ub515\";")

        self.horizontalLayout_39.addWidget(self.label_5)

        self.horizontalLayout_7.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_12)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_51 = QLabel(self.frame_18)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"font: 75 11pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_51.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.label_51)

        self.label_6 = QLabel(self.frame_18)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_6.setStyleSheet(u"font: 75 11pt \"\ub9d1\uc740 \uace0\ub515\";")

        self.horizontalLayout_40.addWidget(self.label_6)

        self.horizontalLayout_7.addWidget(self.frame_18)

        self.frame_right_mar = QFrame(self.frame_12)
        self.frame_right_mar.setObjectName(u"frame_right_mar")
        self.frame_right_mar.setFrameShape(QFrame.StyledPanel)
        self.frame_right_mar.setFrameShadow(QFrame.Raised)
        self.frame_right_mar.setMaximumSize(50, 16777215)
        self.horizontalLayout_7.addWidget(self.frame_right_mar)

        self.verticalLayout_10.addWidget(self.frame_12)

        self.frame_6 = QFrame(self.tabFrame_anal)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(25, 10, 25, 10) # margin 고치기
        self.horizontalLayout_5.setSpacing(0)
        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        # self.frame_9.setStyleSheet(u"#frame_9{border-right: 1px solid;}")
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_9)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_27)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)

        self.frame_31 = QFrame(self.frame_27)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(16777215, 50))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10_31 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_10_31.setSpacing(0)
        self.horizontalLayout_10_31.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10_31.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.frame_31)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_44)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_44)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 63 18pt \"Segoe UI Semibold\";")

        self.verticalLayout_41.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_44)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 63 10pt \"Segoe UI\";")

        self.verticalLayout_41.addWidget(self.label_11)

        self.horizontalLayout_10_31.addWidget(self.frame_44)

        self.frame_47 = QFrame(self.frame_31)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)

        self.line = QFrame(self.frame_47)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 15, 250, 3))
        self.line.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10_31.addWidget(self.frame_47)

        self.verticalLayout_28.addWidget(self.frame_31)

        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)

        self.circularProgressBarBase = QFrame(self.frame_27)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setMinimumSize(0, 330)
        # self.circularProgressBarBase.setGeometry(QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        # self.circularProgressBarBase.setAlignment(Qt.AlignCenter)
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(10, 25, 300, 300))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
                                            "	border-radius: 150px;\n"
                                            "	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
                                            "}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 25, 300, 300))
        self.circularBg.setStyleSheet(u"QFrame{\n"
                                      "	border-radius: 150px;\n"
                                      "	background-color: rgba(255, 90, 0, 0.2);\n"
                                      "}")
        self.circularBg.setFrameShape(QFrame.StyledPanel)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(35, 50, 250, 250))
        self.container.setStyleSheet(u"QFrame{\n"
                                     "	border-radius: 125px;\n"
                                     "	background-color: rgb(255, 255, 255);\n"
                                     "}")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.container)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(32, 35, 193, 130))
        self.widget.setStyleSheet("background-color: none;")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelTitle = QLabel(self.widget)
        self.labelTitle.setObjectName(u"labelTitle")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(20)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet(u"background-color: none;")
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)

        self.labelPercentage = QLabel(self.widget)
        self.labelPercentage.setObjectName(u"labelPercentage")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(42)
        self.labelPercentage.setFont(font1)
        self.labelPercentage.setStyleSheet(u"background-color: none;\n"
                                           "color: rgba(255, 90, 0, 255);\n"
                                           "font-style: bold;\n")
        self.labelPercentage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPercentage, 1, 0, 1, 1)

        self.pushButton_detail = QPushButton(self.container)
        self.pushButton_detail.setObjectName(u"pushButton_detail")
        self.pushButton_detail.setGeometry(QRect(95, 190, 64, 20))
        sizePolicy4.setHeightForWidth(self.pushButton_detail.sizePolicy().hasHeightForWidth())
        self.pushButton_detail.setSizePolicy(sizePolicy4)
        self.pushButton_detail.setIconSize(QSize(16, 16))
        self.pushButton_detail.setAutoDefault(False)
        self.pushButton_detail.setFlat(False)
        self.pushButton_detail.setStyleSheet(tab_btn_style)
        self.pushButton_detail.clicked.connect(lambda: self.open_psd_power())

        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        # SplashScreen.setCentralWidget(self.frame_27)
        self.verticalLayout_28.addWidget(self.circularProgressBarBase)

        ## 오른쪽 글씨
        self.label_62 = QLabel(self.circularProgressBarBase)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(325, 105, 121, 31))
        self.label_62.setStyleSheet(u"font: 10pt \"Segoe UI Symbol\";")
        self.label_62.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_63 = QLabel(self.circularProgressBarBase)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(325, 165, 121, 31))
        self.label_63.setStyleSheet(u"font: 10pt \"Segoe UI Symbol\";")
        self.label_63.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_64 = QLabel(self.circularProgressBarBase)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(325, 45, 121, 31))
        self.label_64.setStyleSheet(u"font: 10pt \"Segoe UI Symbol\";")
        self.label_64.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_9 = QLabel(self.circularProgressBarBase)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(340, 75, 71, 21))
        self.label_9.setStyleSheet(u"font: 63 14pt \"Segoe UI Semibold\";")
        self.label_65 = QLabel(self.circularProgressBarBase)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(340, 135, 71, 21))
        self.label_65.setStyleSheet(u"font: 63 14pt \"Segoe UI Semibold\";")
        self.label_66 = QLabel(self.circularProgressBarBase)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(340, 195, 71, 21))
        self.label_66.setStyleSheet(u"font: 63 14pt \"Segoe UI Semibold\";")

        self.frame_59 = QFrame(self.frame_27)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMaximumSize(QSize(16777215, 50))
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_60 = QFrame(self.frame_59)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_60)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_60)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font: 63 18pt \"Segoe UI Semibold\";")

        self.verticalLayout_42.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_60)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 63 10pt \"Segoe UI\";")

        self.verticalLayout_42.addWidget(self.label_13)

        self.horizontalLayout_6.addWidget(self.frame_60)

        self.frame_100 = QFrame(self.frame_59)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_100)

        self.verticalLayout_28.addWidget(self.frame_59)

        # self.label_36 = QLabel(self.frame_27)
        # self.label_36.setObjectName(u"label_36")
        # self.label_36.setAlignment(Qt.AlignCenter)
        # self.label_36.setMaximumSize(16777215, 300)
        #
        # self.verticalLayout_28.addWidget(self.label_36)

        self.frame_91 = QFrame(self.frame_27)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_91)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_92 = QFrame(self.frame_91)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_94 = QFrame(self.frame_92)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)

        self.circularProgress_psd_sen = QFrame(self.frame_94)  # 색깔 배경
        self.circularProgress_psd_sen.setObjectName(u"circularProgress_psd_sen")
        self.circularProgress_psd_sen.setGeometry(
            QRect(self.circularProgressCoordinate[0], self.circularProgressCoordinate[1],
                  self.circularProgressCoordinate[2], self.circularProgressCoordinate[3]))
        self.circularProgress_psd_sen.setStyleSheet(u"QFrame{\n"
                                                    "border-radius: 60px;\n"
                                                    "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
                                                    "}")
        self.circularProgress_psd_sen.setFrameShape(QFrame.NoFrame)
        self.circularProgress_psd_sen.setFrameShadow(QFrame.Raised)
        self.circularBg_psd_sen = QFrame(self.frame_94)  # 색깔 나머지 배경
        self.circularBg_psd_sen.setObjectName(u"circularBg_psd_sen")
        self.circularBg_psd_sen.setGeometry(
            QRect(self.circularBgCoordinate[0], self.circularBgCoordinate[1], self.circularBgCoordinate[2],
                  self.circularBgCoordinate[3]))
        self.circularBg_psd_sen.setStyleSheet(u"QFrame{\n"
                                              "	border-radius: 60px;\n"
                                              "	background-color: rgba(255, 90, 0, 0.2);\n"
                                              "}")
        self.circularBg_psd_sen.setFrameShape(QFrame.StyledPanel)
        self.circularBg_psd_sen.setFrameShadow(QFrame.Raised)
        self.container_psd_sen = QFrame(self.frame_94)  # 가운데 작은 흰색 원
        self.container_psd_sen.setObjectName(u"container_psd_sen")
        self.container_psd_sen.setGeometry(
            QRect(self.containerCoordinate[0], self.containerCoordinate[1], self.containerCoordinate[2],
                  self.containerCoordinate[3]))
        self.container_psd_sen.setStyleSheet(u"QFrame{\n"
                                             "	border-radius: 45px;\n"
                                             "	background-color: rgb(255, 255, 255);\n"
                                             "}")
        self.container_psd_sen.setFrameShape(QFrame.StyledPanel)
        self.container_psd_sen.setFrameShadow(QFrame.Raised)
        self.widget_psd_sen = QWidget(self.container_psd_sen)
        self.widget_psd_sen.setObjectName(u"widget_psd_sen")
        self.widget_psd_sen.setGeometry(QRect(15, 15, 61, 61))
        self.widget_psd_sen.setStyleSheet("background-color: none;")
        self.labelTitle_psd_sen = QLabel(self.widget_psd_sen)
        self.labelTitle_psd_sen.setObjectName(u"labelTitle_psd_sen")
        self.labelTitle_psd_sen.setGeometry(
            QRect(self.labelTitleCoordinate[0], self.labelTitleCoordinate[1], self.labelTitleCoordinate[2],
                  self.labelTitleCoordinate[3]))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.labelTitle_psd_sen.setFont(font)
        self.labelTitle_psd_sen.setStyleSheet(u"background-color: none;")
        self.labelTitle_psd_sen.setAlignment(Qt.AlignCenter)

        self.labelPercentage_psd_sen = QLabel(self.container_psd_sen)
        self.labelPercentage_psd_sen.setObjectName(u"labelPercentage_psd_sen")
        self.labelPercentage_psd_sen.setGeometry(
            QRect(self.labelPercentageCoordinate[0], self.labelPercentageCoordinate[1],
                  self.labelPercentageCoordinate[2], self.labelPercentageCoordinate[3]))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(18)
        self.labelPercentage_psd_sen.setFont(font1)
        self.labelPercentage_psd_sen.setStyleSheet(u"background-color: none;\n"
                                                   "color: rgba(255, 90, 0, 255);\n"
                                                   "font-style: bold;\n")
        self.labelPercentage_psd_sen.setAlignment(Qt.AlignCenter)

        self.circularBg_psd_sen.raise_()
        self.circularProgress_psd_sen.raise_()
        self.container_psd_sen.raise_()

        # self.label_7 = QLabel(self.frame_94)
        # self.label_7.setObjectName(u"label_7")
        # self.label_7.setGeometry(QRect(10, 10, 30, 100))
        # self.label_7.setStyleSheet(u"color: rgb(34,34,34);")

        self.horizontalLayout_42.addWidget(self.frame_94)

        self.frame_95 = QFrame(self.frame_92)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)

        self.circularProgress_fc_sen = QFrame(self.frame_95)  # 색깔 배경
        self.circularProgress_fc_sen.setObjectName(u"circularProgress_fc_sen")
        self.circularProgress_fc_sen.setGeometry(
            QRect(self.circularProgressCoordinate[0], self.circularProgressCoordinate[1],
                  self.circularProgressCoordinate[2], self.circularProgressCoordinate[3]))
        self.circularProgress_fc_sen.setStyleSheet(u"QFrame{\n"
                                                   "border-radius: 60px;\n"
                                                   "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
                                                   "}")
        self.circularProgress_fc_sen.setFrameShape(QFrame.NoFrame)
        self.circularProgress_fc_sen.setFrameShadow(QFrame.Raised)
        self.circularBg_fc_sen = QFrame(self.frame_95)  # 색깔 나머지 배경
        self.circularBg_fc_sen.setObjectName(u"circularBg_fc_sen")
        self.circularBg_fc_sen.setGeometry(
            QRect(self.circularBgCoordinate[0], self.circularBgCoordinate[1], self.circularBgCoordinate[2],
                  self.circularBgCoordinate[3]))
        self.circularBg_fc_sen.setStyleSheet(u"QFrame{\n"
                                             "	border-radius: 60px;\n"
                                             "	background-color: rgba(255, 90, 0, 0.2);\n"
                                             "}")
        self.circularBg_fc_sen.setFrameShape(QFrame.StyledPanel)
        self.circularBg_fc_sen.setFrameShadow(QFrame.Raised)
        self.container_fc_sen = QFrame(self.frame_95)  # 가운데 작은 흰색 원
        self.container_fc_sen.setObjectName(u"container_fc_sen")
        self.container_fc_sen.setGeometry(
            QRect(self.containerCoordinate[0], self.containerCoordinate[1], self.containerCoordinate[2],
                  self.containerCoordinate[3]))
        self.container_fc_sen.setStyleSheet(u"QFrame{\n"
                                            "	border-radius: 45px;\n"
                                            "	background-color: rgb(255, 255, 255);\n"
                                            "}")
        self.container_fc_sen.setFrameShape(QFrame.StyledPanel)
        self.container_fc_sen.setFrameShadow(QFrame.Raised)
        self.widget_fc_sen = QWidget(self.container_fc_sen)
        self.widget_fc_sen.setObjectName(u"widget_fc_sen")
        self.widget_fc_sen.setGeometry(QRect(15, 15, 61, 61))
        self.widget_fc_sen.setStyleSheet("background-color: none;")
        self.labelTitle_fc_sen = QLabel(self.widget_fc_sen)
        self.labelTitle_fc_sen.setObjectName(u"labelTitle_fc_sen")
        self.labelTitle_fc_sen.setGeometry(
            QRect(self.labelTitleCoordinate[0], self.labelTitleCoordinate[1], self.labelTitleCoordinate[2],
                  self.labelTitleCoordinate[3]))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.labelTitle_fc_sen.setFont(font)
        self.labelTitle_fc_sen.setStyleSheet(u"background-color: none;")
        self.labelTitle_fc_sen.setAlignment(Qt.AlignCenter)

        self.labelPercentage_fc_sen = QLabel(self.container_fc_sen)
        self.labelPercentage_fc_sen.setObjectName(u"labelPercentage_fc_sen")
        self.labelPercentage_fc_sen.setGeometry(
            QRect(self.labelPercentageCoordinate[0], self.labelPercentageCoordinate[1],
                  self.labelPercentageCoordinate[2], self.labelPercentageCoordinate[3]))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(18)
        self.labelPercentage_fc_sen.setFont(font1)
        self.labelPercentage_fc_sen.setStyleSheet(u"background-color: none;\n"
                                                  "color: rgba(255, 90, 0, 255);\n"
                                                  "font-style: bold;\n")
        self.labelPercentage_fc_sen.setAlignment(Qt.AlignCenter)

        self.circularBg_fc_sen.raise_()
        self.circularProgress_fc_sen.raise_()
        self.container_fc_sen.raise_()

        self.horizontalLayout_42.addWidget(self.frame_95)

        self.frame_96 = QFrame(self.frame_92)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)

        self.circularProgress_ni_sen = QFrame(self.frame_96)  # 색깔 배경
        self.circularProgress_ni_sen.setObjectName(u"circularProgress_ni_sen")
        self.circularProgress_ni_sen.setGeometry(
            QRect(self.circularProgressCoordinate[0], self.circularProgressCoordinate[1],
                  self.circularProgressCoordinate[2], self.circularProgressCoordinate[3]))
        self.circularProgress_ni_sen.setStyleSheet(u"QFrame{\n"
                                                   "border-radius: 60px;\n"
                                                   "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
                                                   "}")
        self.circularProgress_ni_sen.setFrameShape(QFrame.NoFrame)
        self.circularProgress_ni_sen.setFrameShadow(QFrame.Raised)
        self.circularBg_ni_sen = QFrame(self.frame_96)  # 색깔 나머지 배경
        self.circularBg_ni_sen.setObjectName(u"circularBg_ni_sen")
        self.circularBg_ni_sen.setGeometry(
            QRect(self.circularBgCoordinate[0], self.circularBgCoordinate[1], self.circularBgCoordinate[2],
                  self.circularBgCoordinate[3]))
        self.circularBg_ni_sen.setStyleSheet(u"QFrame{\n"
                                             "	border-radius: 60px;\n"
                                             "	background-color: rgba(255, 90, 0, 0.2);\n"
                                             "}")
        self.circularBg_ni_sen.setFrameShape(QFrame.StyledPanel)
        self.circularBg_ni_sen.setFrameShadow(QFrame.Raised)
        self.container_ni_sen = QFrame(self.frame_96)  # 가운데 작은 흰색 원
        self.container_ni_sen.setObjectName(u"container_ni_sen")
        self.container_ni_sen.setGeometry(
            QRect(self.containerCoordinate[0], self.containerCoordinate[1], self.containerCoordinate[2],
                  self.containerCoordinate[3]))
        self.container_ni_sen.setStyleSheet(u"QFrame{\n"
                                            "	border-radius: 45px;\n"
                                            "	background-color: rgb(255, 255, 255);\n"
                                            "}")
        self.container_ni_sen.setFrameShape(QFrame.StyledPanel)
        self.container_ni_sen.setFrameShadow(QFrame.Raised)
        self.widget_ni_sen = QWidget(self.container_ni_sen)
        self.widget_ni_sen.setObjectName(u"widget_ni_sen")
        self.widget_ni_sen.setGeometry(QRect(15, 15, 61, 61))
        self.widget_ni_sen.setStyleSheet("background-color: none;")
        self.labelTitle_ni_sen = QLabel(self.widget_ni_sen)
        self.labelTitle_ni_sen.setObjectName(u"labelTitle_ni_sen")
        self.labelTitle_ni_sen.setGeometry(
            QRect(self.labelTitleCoordinate[0], self.labelTitleCoordinate[1], self.labelTitleCoordinate[2],
                  self.labelTitleCoordinate[3]))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.labelTitle_ni_sen.setFont(font)
        self.labelTitle_ni_sen.setStyleSheet(u"background-color: none;")
        self.labelTitle_ni_sen.setAlignment(Qt.AlignCenter)

        self.labelPercentage_ni_sen = QLabel(self.container_ni_sen)
        self.labelPercentage_ni_sen.setObjectName(u"labelPercentage_ni_sen")
        self.labelPercentage_ni_sen.setGeometry(
            QRect(self.labelPercentageCoordinate[0], self.labelPercentageCoordinate[1],
                  self.labelPercentageCoordinate[2], self.labelPercentageCoordinate[3]))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(18)
        self.labelPercentage_ni_sen.setFont(font1)
        self.labelPercentage_ni_sen.setStyleSheet(u"background-color: none;\n"
                                                  "color: rgba(255, 90, 0, 255);\n"
                                                  "font-style: bold;\n")
        self.labelPercentage_ni_sen.setAlignment(Qt.AlignCenter)

        self.circularBg_ni_sen.raise_()
        self.circularProgress_ni_sen.raise_()
        self.container_ni_sen.raise_()

        self.horizontalLayout_42.addWidget(self.frame_96)

        self.verticalLayout_31.addWidget(self.frame_92)

        self.frame_93 = QFrame(self.frame_91)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_93)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_97 = QFrame(self.frame_93)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)

        self.circularProgress_psd_sou = QFrame(self.frame_97)  # 색깔 배경
        self.circularProgress_psd_sou.setObjectName(u"circularProgress_psd_sou")
        self.circularProgress_psd_sou.setGeometry(
            QRect(self.circularProgressCoordinate[0], self.circularProgressCoordinate[1],
                  self.circularProgressCoordinate[2], self.circularProgressCoordinate[3]))
        self.circularProgress_psd_sou.setStyleSheet(u"QFrame{\n"
                                                    "border-radius: 60px;\n"
                                                    "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
                                                    "}")
        self.circularProgress_psd_sou.setFrameShape(QFrame.NoFrame)
        self.circularProgress_psd_sou.setFrameShadow(QFrame.Raised)
        self.circularBg_psd_sou = QFrame(self.frame_97)  # 색깔 나머지 배경
        self.circularBg_psd_sou.setObjectName(u"circularBg_psd_sou")
        self.circularBg_psd_sou.setGeometry(
            QRect(self.circularBgCoordinate[0], self.circularBgCoordinate[1], self.circularBgCoordinate[2],
                  self.circularBgCoordinate[3]))
        self.circularBg_psd_sou.setStyleSheet(u"QFrame{\n"
                                              "	border-radius: 60px;\n"
                                              "	background-color: rgba(255, 90, 0, 0.2);\n"
                                              "}")
        self.circularBg_psd_sou.setFrameShape(QFrame.StyledPanel)
        self.circularBg_psd_sou.setFrameShadow(QFrame.Raised)
        self.container_psd_sou = QFrame(self.frame_97)  # 가운데 작은 흰색 원
        self.container_psd_sou.setObjectName(u"container_psd_sou")
        self.container_psd_sou.setGeometry(
            QRect(self.containerCoordinate[0], self.containerCoordinate[1], self.containerCoordinate[2],
                  self.containerCoordinate[3]))
        self.container_psd_sou.setStyleSheet(u"QFrame{\n"
                                             "	border-radius: 45px;\n"
                                             "	background-color: rgb(255, 255, 255);\n"
                                             "}")
        self.container_psd_sou.setFrameShape(QFrame.StyledPanel)
        self.container_psd_sou.setFrameShadow(QFrame.Raised)
        self.widget_psd_sou = QWidget(self.container_psd_sou)
        self.widget_psd_sou.setObjectName(u"widget_psd_sou")
        self.widget_psd_sou.setGeometry(QRect(15, 15, 61, 61))
        self.widget_psd_sou.setStyleSheet("background-color: none;")
        self.labelTitle_psd_sou = QLabel(self.widget_psd_sou)
        self.labelTitle_psd_sou.setObjectName(u"labelTitle_psd_sou")
        self.labelTitle_psd_sou.setGeometry(
            QRect(self.labelTitleCoordinate[0], self.labelTitleCoordinate[1], self.labelTitleCoordinate[2],
                  self.labelTitleCoordinate[3]))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.labelTitle_psd_sou.setFont(font)
        self.labelTitle_psd_sou.setStyleSheet(u"background-color: none;")
        self.labelTitle_psd_sou.setAlignment(Qt.AlignCenter)

        self.labelPercentage_psd_sou = QLabel(self.container_psd_sou)
        self.labelPercentage_psd_sou.setObjectName(u"labelPercentage_psd_sou")
        self.labelPercentage_psd_sou.setGeometry(
            QRect(self.labelPercentageCoordinate[0], self.labelPercentageCoordinate[1],
                  self.labelPercentageCoordinate[2], self.labelPercentageCoordinate[3]))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(18)
        self.labelPercentage_psd_sou.setFont(font1)
        self.labelPercentage_psd_sou.setStyleSheet(u"background-color: none;\n"
                                                   "color: rgba(255, 90, 0, 255);\n"
                                                   "font-style: bold;\n")
        self.labelPercentage_psd_sou.setAlignment(Qt.AlignCenter)

        self.circularBg_psd_sou.raise_()
        self.circularProgress_psd_sou.raise_()
        self.container_psd_sou.raise_()

        self.horizontalLayout_43.addWidget(self.frame_97)

        self.frame_98 = QFrame(self.frame_93)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)

        self.circularProgress_fc_sou = QFrame(self.frame_98)  # 색깔 배경
        self.circularProgress_fc_sou.setObjectName(u"circularProgress_fc_sou")
        self.circularProgress_fc_sou.setGeometry(
            QRect(self.circularProgressCoordinate[0], self.circularProgressCoordinate[1],
                  self.circularProgressCoordinate[2], self.circularProgressCoordinate[3]))
        self.circularProgress_fc_sou.setStyleSheet(u"QFrame{\n"
                                                   "border-radius: 60px;\n"
                                                   "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
                                                   "}")
        self.circularProgress_fc_sou.setFrameShape(QFrame.NoFrame)
        self.circularProgress_fc_sou.setFrameShadow(QFrame.Raised)
        self.circularBg_fc_sou = QFrame(self.frame_98)  # 색깔 나머지 배경
        self.circularBg_fc_sou.setObjectName(u"circularBg_fc_sou")
        self.circularBg_fc_sou.setGeometry(
            QRect(self.circularBgCoordinate[0], self.circularBgCoordinate[1], self.circularBgCoordinate[2],
                  self.circularBgCoordinate[3]))
        self.circularBg_fc_sou.setStyleSheet(u"QFrame{\n"
                                             "	border-radius: 60px;\n"
                                             "	background-color: rgba(255, 90, 0, 0.2);\n"
                                             "}")
        self.circularBg_fc_sou.setFrameShape(QFrame.StyledPanel)
        self.circularBg_fc_sou.setFrameShadow(QFrame.Raised)
        self.container_fc_sou = QFrame(self.frame_98)  # 가운데 작은 흰색 원
        self.container_fc_sou.setObjectName(u"container_fc_sou")
        self.container_fc_sou.setGeometry(
            QRect(self.containerCoordinate[0], self.containerCoordinate[1], self.containerCoordinate[2],
                  self.containerCoordinate[3]))
        self.container_fc_sou.setStyleSheet(u"QFrame{\n"
                                            "	border-radius: 45px;\n"
                                            "	background-color: rgb(255, 255, 255);\n"
                                            "}")
        self.container_fc_sou.setFrameShape(QFrame.StyledPanel)
        self.container_fc_sou.setFrameShadow(QFrame.Raised)
        self.widget_fc_sou = QWidget(self.container_fc_sou)
        self.widget_fc_sou.setObjectName(u"widget_fc_sou")
        self.widget_fc_sou.setGeometry(QRect(15, 15, 61, 61))
        self.widget_fc_sou.setStyleSheet("background-color: none;")
        self.labelTitle_fc_sou = QLabel(self.widget_fc_sou)
        self.labelTitle_fc_sou.setObjectName(u"labelTitle_fc_sou")
        self.labelTitle_fc_sou.setGeometry(
            QRect(self.labelTitleCoordinate[0], self.labelTitleCoordinate[1], self.labelTitleCoordinate[2],
                  self.labelTitleCoordinate[3]))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.labelTitle_fc_sou.setFont(font)
        self.labelTitle_fc_sou.setStyleSheet(u"background-color: none;")
        self.labelTitle_fc_sou.setAlignment(Qt.AlignCenter)

        self.labelPercentage_fc_sou = QLabel(self.container_fc_sou)
        self.labelPercentage_fc_sou.setObjectName(u"labelPercentage_fc_sou")
        self.labelPercentage_fc_sou.setGeometry(
            QRect(self.labelPercentageCoordinate[0], self.labelPercentageCoordinate[1],
                  self.labelPercentageCoordinate[2], self.labelPercentageCoordinate[3]))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(18)
        self.labelPercentage_fc_sou.setFont(font1)
        self.labelPercentage_fc_sou.setStyleSheet(u"background-color: none;\n"
                                                  "color: rgba(255, 90, 0, 255);\n"
                                                  "font-style: bold;\n")
        self.labelPercentage_fc_sou.setAlignment(Qt.AlignCenter)

        self.circularBg_fc_sou.raise_()
        self.circularProgress_fc_sou.raise_()
        self.container_fc_sou.raise_()

        self.horizontalLayout_43.addWidget(self.frame_98)

        self.frame_99 = QFrame(self.frame_93)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)

        self.circularProgress_ni_sou = QFrame(self.frame_99)  # 색깔 배경
        self.circularProgress_ni_sou.setObjectName(u"circularProgress_ni_sou")
        self.circularProgress_ni_sou.setGeometry(
            QRect(self.circularProgressCoordinate[0], self.circularProgressCoordinate[1],
                  self.circularProgressCoordinate[2], self.circularProgressCoordinate[3]))
        self.circularProgress_ni_sou.setStyleSheet(u"QFrame{\n"
                                                   "border-radius: 60px;\n"
                                                   "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
                                                   "}")
        self.circularProgress_ni_sou.setFrameShape(QFrame.NoFrame)
        self.circularProgress_ni_sou.setFrameShadow(QFrame.Raised)
        self.circularBg_ni_sou = QFrame(self.frame_99)  # 색깔 나머지 배경
        self.circularBg_ni_sou.setObjectName(u"circularBg_ni_sou")
        self.circularBg_ni_sou.setGeometry(
            QRect(self.circularBgCoordinate[0], self.circularBgCoordinate[1], self.circularBgCoordinate[2],
                  self.circularBgCoordinate[3]))
        self.circularBg_ni_sou.setStyleSheet(u"QFrame{\n"
                                             "	border-radius: 60px;\n"
                                             "	background-color: rgba(255, 90, 0, 0.2);\n"
                                             "}")
        self.circularBg_ni_sou.setFrameShape(QFrame.StyledPanel)
        self.circularBg_ni_sou.setFrameShadow(QFrame.Raised)
        self.container_ni_sou = QFrame(self.frame_99)  # 가운데 작은 흰색 원
        self.container_ni_sou.setObjectName(u"container_ni_sou")
        self.container_ni_sou.setGeometry(
            QRect(self.containerCoordinate[0], self.containerCoordinate[1], self.containerCoordinate[2],
                  self.containerCoordinate[3]))
        self.container_ni_sou.setStyleSheet(u"QFrame{\n"
                                            "	border-radius: 45px;\n"
                                            "	background-color: rgb(255, 255, 255);\n"
                                            "}")
        self.container_ni_sou.setFrameShape(QFrame.StyledPanel)
        self.container_ni_sou.setFrameShadow(QFrame.Raised)
        self.widget_ni_sour = QWidget(self.container_ni_sou)
        self.widget_ni_sour.setObjectName(u"widget_ni_sour")
        self.widget_ni_sour.setGeometry(QRect(15, 15, 61, 61))
        self.widget_ni_sour.setStyleSheet("background-color: none;")
        self.labelTitle_ni_sou = QLabel(self.widget_ni_sour)
        self.labelTitle_ni_sou.setObjectName(u"labelTitle_ni_sou")
        self.labelTitle_ni_sou.setGeometry(
            QRect(self.labelTitleCoordinate[0], self.labelTitleCoordinate[1], self.labelTitleCoordinate[2],
                  self.labelTitleCoordinate[3]))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.labelTitle_ni_sou.setFont(font)
        self.labelTitle_ni_sou.setStyleSheet(u"background-color: none;")
        self.labelTitle_ni_sou.setAlignment(Qt.AlignCenter)

        self.labelPercentage_ni_sou = QLabel(self.container_ni_sou)
        self.labelPercentage_ni_sou.setObjectName(u"labelPercentage_ni_sou")
        self.labelPercentage_ni_sou.setGeometry(
            QRect(self.labelPercentageCoordinate[0], self.labelPercentageCoordinate[1],
                  self.labelPercentageCoordinate[2], self.labelPercentageCoordinate[3]))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(18)
        self.labelPercentage_ni_sou.setFont(font1)
        self.labelPercentage_ni_sou.setStyleSheet(u"background-color: none;\n"
                                                  "color: rgba(255, 90, 0, 255);\n"
                                                  "font-style: bold;\n")
        self.labelPercentage_ni_sou.setAlignment(Qt.AlignCenter)

        self.circularBg_ni_sou.raise_()
        self.circularProgress_ni_sou.raise_()
        self.container_ni_sou.raise_()

        self.horizontalLayout_43.addWidget(self.frame_99)

        self.verticalLayout_31.addWidget(self.frame_93)

        self.verticalLayout_28.addWidget(self.frame_91)

        self.horizontalLayout_9.addWidget(self.frame_27)

        self.horizontalLayout_5.addWidget(self.frame_9)

        self.frame_107 = QFrame(self.frame_6)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setMaximumSize(QSize(40, 16777215))
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)

        self.line_2 = QFrame(self.frame_107)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(15, 20, 3, 385))
        self.line_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.frame_107)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_8)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_103 = QFrame(self.frame_8)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setMaximumSize(QSize(16777215, 50))
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_103)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_104 = QFrame(self.frame_103)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_104)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_104)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 63 18pt \"Segoe UI Semibold\";")

        self.verticalLayout_43.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_104)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 63 10pt \"Segoe UI\";")

        self.verticalLayout_43.addWidget(self.label_15)

        self.horizontalLayout_10.addWidget(self.frame_104)

        self.frame_105 = QFrame(self.frame_103)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.line_3 = QFrame(self.frame_105)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(30, 20, 118, 3))
        self.line_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.frame_105)

        self.verticalLayout_11.addWidget(self.frame_103)

        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_7)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.frame_7)
        self.label_37.setObjectName(u"label_37")
        sizePolicy3.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy3)
        self.label_37.setStyleSheet(u"font: 75 14pt \"Arial\";\n"
                                    "background-color: rgb(231, 231, 231);")
        self.label_37.setAlignment(Qt.AlignLeft)

        self.verticalLayout_45.addWidget(self.label_37)

        self.frame_28 = QFrame(self.frame_7)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_64 = QFrame(self.frame_28)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_64)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.frame_64)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_40)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)

        self.frame_70 = QFrame(self.frame_64)
        self.frame_70.setObjectName(u"frame_70")
        sizePolicy.setHeightForWidth(self.frame_70.sizePolicy().hasHeightForWidth())
        self.frame_70.setSizePolicy(sizePolicy)
        self.frame_70.setMaximumSize(QSize(16777215, 40))
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.label_74 = QLabel(self.frame_70)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(0, 0, 100, 16))
        sizePolicy4.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy4)
        self.label_74.setAlignment(Qt.AlignRight)
        self.pushButton_7 = QPushButton(self.frame_70)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(120, 8, 64, 20))
        sizePolicy4.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy4)
        self.pushButton_7.setIconSize(QSize(16, 16))
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setStyleSheet(tab_btn_style)
        self.pushButton_7.clicked.connect(lambda: self.open_psd_power())
        self.label_42 = QLabel(self.frame_70)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(0, 15, 100, 16))
        sizePolicy4.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy4)
        self.label_42.setAlignment(Qt.AlignRight)

        self.verticalLayout_15.addWidget(self.frame_70)

        self.horizontalLayout_34.addWidget(self.frame_64)

        self.frame_65 = QFrame(self.frame_28)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_65)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.frame_65)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_43)

        self.frame_71 = QFrame(self.frame_65)
        self.frame_71.setObjectName(u"frame_71")
        sizePolicy.setHeightForWidth(self.frame_71.sizePolicy().hasHeightForWidth())
        self.frame_71.setSizePolicy(sizePolicy)
        self.frame_71.setMaximumSize(QSize(16777215, 40))
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.label_75 = QLabel(self.frame_71)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(0, 0, 100, 16))
        sizePolicy4.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy4)
        self.label_75.setAlignment(Qt.AlignRight)

        self.pushButton_8 = QPushButton(self.frame_71)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(120, 8, 64, 20))
        sizePolicy4.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy4)
        self.pushButton_8.setIconSize(QSize(16, 16))
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setStyleSheet(tab_btn_style)
        self.pushButton_8.clicked.connect(lambda: self.open_source_plot())
        self.label_44 = QLabel(self.frame_71)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(0, 15, 100, 16))
        sizePolicy4.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy4)
        self.label_44.setAlignment(Qt.AlignRight)

        self.verticalLayout_16.addWidget(self.frame_71)

        self.horizontalLayout_34.addWidget(self.frame_65)

        self.verticalLayout_45.addWidget(self.frame_28)

        self.verticalLayout_11.addWidget(self.frame_7)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_10)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.frame_10)
        self.label_58.setObjectName(u"label_58")
        sizePolicy3.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy3)
        self.label_58.setStyleSheet(u"font: 75 14pt \"Arial\";\n"
                                    "background-color: rgb(231, 231, 231);")
        self.label_58.setAlignment(Qt.AlignLeft)

        self.verticalLayout_46.addWidget(self.label_58)

        self.frame_26 = QFrame(self.frame_10)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_26)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_30)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_30)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_38)

        self.frame_68 = QFrame(self.frame_30)
        self.frame_68.setObjectName(u"frame_68")
        sizePolicy.setHeightForWidth(self.frame_68.sizePolicy().hasHeightForWidth())
        self.frame_68.setSizePolicy(sizePolicy)
        self.frame_68.setMaximumSize(QSize(16777215, 40))
        self.frame_68.setStyleSheet(u"")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.label_72 = QLabel(self.frame_68)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(0, 0, 100, 16))
        sizePolicy4.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy4)
        self.label_72.setAlignment(Qt.AlignRight)
        self.pushButton_5 = QPushButton(self.frame_68)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(120, 8, 64, 20))
        sizePolicy4.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy4)
        self.pushButton_5.setIconSize(QSize(16, 16))
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setStyleSheet(tab_btn_style)
        self.pushButton_5.clicked.connect(lambda: self.open_tr_detail())
        self.label_70 = QLabel(self.frame_68)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(0, 15, 100, 16))
        sizePolicy4.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy4)
        self.label_70.setAlignment(Qt.AlignRight)

        self.verticalLayout_13.addWidget(self.frame_68)

        self.horizontalLayout_66.addWidget(self.frame_30)

        self.frame_63 = QFrame(self.frame_26)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_63)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.frame_63)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_39)

        self.frame_69 = QFrame(self.frame_63)
        self.frame_69.setObjectName(u"frame_69")
        sizePolicy.setHeightForWidth(self.frame_69.sizePolicy().hasHeightForWidth())
        self.frame_69.setSizePolicy(sizePolicy)
        self.frame_69.setMaximumSize(QSize(16777215, 40))
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.label_73 = QLabel(self.frame_69)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(0, 0, 100, 16))
        sizePolicy4.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy4)
        self.label_73.setAlignment(Qt.AlignRight)

        self.pushButton_6 = QPushButton(self.frame_69)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(120, 8, 64, 20))
        sizePolicy4.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy4)
        self.pushButton_6.setIconSize(QSize(16, 16))
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setStyleSheet(tab_btn_style)
        self.pushButton_6.clicked.connect(lambda: self.open_source_plot())
        self.label_71 = QLabel(self.frame_69)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(0, 15, 100, 16))
        sizePolicy4.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy4)
        self.label_71.setAlignment(Qt.AlignRight)

        self.verticalLayout_14.addWidget(self.frame_69)

        self.horizontalLayout_66.addWidget(self.frame_63)

        self.verticalLayout_46.addWidget(self.frame_26)

        self.verticalLayout_11.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_11)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_60 = QLabel(self.frame_11)
        self.label_60.setObjectName(u"label_60")
        sizePolicy3.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy3)
        self.label_60.setStyleSheet(u"font: 75 14pt \"Arial\";\n"
                                    "background-color: rgb(231, 231, 231);")
        self.label_60.setAlignment(Qt.AlignLeft)

        self.verticalLayout_47.addWidget(self.label_60)

        self.frame_29 = QFrame(self.frame_11)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.frame_66 = QFrame(self.frame_29)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_66)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.frame_66)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_52)

        self.frame_72 = QFrame(self.frame_66)
        self.frame_72.setObjectName(u"frame_72")
        sizePolicy.setHeightForWidth(self.frame_72.sizePolicy().hasHeightForWidth())
        self.frame_72.setSizePolicy(sizePolicy)
        self.frame_72.setMaximumSize(QSize(16777215, 40))
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.label_76 = QLabel(self.frame_72)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(0, 0, 100, 16))
        sizePolicy4.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy4)
        self.label_76.setAlignment(Qt.AlignRight)

        self.pushButton_9 = QPushButton(self.frame_72)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(120, 8, 64, 20))
        sizePolicy4.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy4)
        self.pushButton_9.setIconSize(QSize(16, 16))
        self.pushButton_9.setAutoDefault(False)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setStyleSheet(tab_btn_style)
        self.pushButton_9.clicked.connect(lambda: self.open_tr_detail())
        self.label_67 = QLabel(self.frame_72)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(0, 15, 100, 16))
        sizePolicy4.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy4)
        self.label_67.setAlignment(Qt.AlignRight)

        self.verticalLayout_18.addWidget(self.frame_72)

        self.horizontalLayout_65.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.frame_29)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_67)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_68 = QLabel(self.frame_67)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_68)

        self.frame_73 = QFrame(self.frame_67)
        self.frame_73.setObjectName(u"frame_73")
        sizePolicy.setHeightForWidth(self.frame_73.sizePolicy().hasHeightForWidth())
        self.frame_73.setSizePolicy(sizePolicy)
        self.frame_73.setMaximumSize(QSize(16777215, 40))
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.label_77 = QLabel(self.frame_73)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(0, 0, 100, 16))
        sizePolicy4.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy4)
        self.label_77.setAlignment(Qt.AlignRight)
        self.pushButton_10 = QPushButton(self.frame_73)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(120, 8, 64, 20))
        sizePolicy4.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy4)
        self.pushButton_10.setIconSize(QSize(16, 16))
        self.pushButton_10.setAutoDefault(False)
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setStyleSheet(tab_btn_style)
        self.pushButton_10.clicked.connect(lambda: self.open_source_plot())
        self.label_69 = QLabel(self.frame_73)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(0, 15, 100, 16))
        sizePolicy4.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy4)
        self.label_69.setAlignment(Qt.AlignRight)

        self.verticalLayout_20.addWidget(self.frame_73)

        self.horizontalLayout_65.addWidget(self.frame_67)

        self.verticalLayout_47.addWidget(self.frame_29)

        self.verticalLayout_11.addWidget(self.frame_11)

        self.horizontalLayout_5.addWidget(self.frame_8)

        self.verticalLayout_10.addWidget(self.frame_6)

        self.frame_61 = QFrame(self.tabFrame_anal)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(0, 0))
        self.frame_61.setMaximumSize(QSize(16777215, 20))
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)

        self.pushButton_4 = QPushButton(self.frame_61)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 0, 40, 23))
        self.pushButton_4.setDisabled(False)
        self.pushButton_4.clicked.connect(lambda: self.tab_pages.setCurrentIndex(0))
        self.pushButton_11 = QPushButton(self.frame_61)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(45, 0, 40, 23))
        self.pushButton_11.setDisabled(False)
        self.pushButton_11.clicked.connect(lambda: self.tab_pages.setCurrentIndex(2))

        self.verticalLayout_10.addWidget(self.frame_61)

        self.tab_pages.addWidget(self.tabFrame_anal)

        ## ----------------------------------------------------세번째 페이지

        self.tabFrame_anal_2 = QWidget()
        self.tabFrame_anal_2.setObjectName(u"tabFrame_anal_2")
        self.verticalLayout_29 = QVBoxLayout(self.tabFrame_anal_2)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_74 = QFrame(self.tabFrame_anal_2)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)

        # self.circularProgress_tr = QFrame(self.frame_74)  # 색깔 배경
        # self.circularProgress_tr.setObjectName(u"circularProgress_tr")
        # self.circularProgress_tr.setGeometry(QRect(15, 15, 130, 130))
        # self.circularProgress_tr.setStyleSheet(u"QFrame{\n"
        #                                        "border-radius: 65px;\n"
        #                                        "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
        #                                        "}")
        # self.circularProgress_tr.setFrameShape(QFrame.NoFrame)
        # self.circularProgress_tr.setFrameShadow(QFrame.Raised)
        # self.circularBg_tr = QFrame(self.frame_74)  # 색깔 나머지 배경
        # self.circularBg_tr.setObjectName(u"circularBg_tr")
        # self.circularBg_tr.setGeometry(QRect(15, 15, 130, 130))
        # self.circularBg_tr.setStyleSheet(u"QFrame{\n"
        #                                  "	border-radius: 65px;\n"
        #                                  "	background-color: rgba(255, 90, 0, 0.2);\n"
        #                                  "}")
        # self.circularBg_tr.setFrameShape(QFrame.StyledPanel)
        # self.circularBg_tr.setFrameShadow(QFrame.Raised)
        # self.container_tr = QFrame(self.frame_74)  # 가운데 작은 흰색 원
        # self.container_tr.setObjectName(u"container_tr")
        # self.container_tr.setGeometry(QRect(35, 35, 90, 90))
        # self.container_tr.setStyleSheet(u"QFrame{\n"
        #                                 "	border-radius: 45px;\n"
        #                                 "	background-color: rgb(255, 255, 255);\n"
        #                                 "}")
        # self.container_tr.setFrameShape(QFrame.StyledPanel)
        # self.container_tr.setFrameShadow(QFrame.Raised)
        # self.widget_tr = QWidget(self.container_tr)
        # self.widget_tr.setObjectName(u"widget_tr")
        # self.widget_tr.setGeometry(QRect(15, 15, 61, 61))
        # self.widget_tr.setStyleSheet("background-color: none;")
        # self.labelTitle_tr = QLabel(self.widget_tr)
        # self.labelTitle_tr.setObjectName(u"labelTitle_tr")
        # self.labelTitle_tr.setGeometry(QRect(0, 0, 61, 20))
        # font = QFont()
        # font.setFamily(u"Segoe UI")
        # font.setPointSize(12)
        # self.labelTitle_tr.setFont(font)
        # self.labelTitle_tr.setStyleSheet(u"background-color: none;")
        # self.labelTitle_tr.setAlignment(Qt.AlignCenter)
        #
        # self.labelPercentage_tr = QLabel(self.widget_tr)
        # self.labelPercentage_tr.setObjectName(u"labelPercentage_tr")
        # self.labelPercentage_tr.setGeometry(QRect(0, 10, 61, 50))
        # font1 = QFont()
        # font1.setFamily(u"Roboto")
        # font1.setPointSize(20)
        # self.labelPercentage_tr.setFont(font1)
        # self.labelPercentage_tr.setStyleSheet(u"background-color: none;\n"
        #                                       "color: rgba(255, 90, 0, 255);\n"
        #                                       "font-style: bold;\n")
        # self.labelPercentage_tr.setAlignment(Qt.AlignCenter)
        #
        #
        # self.circularBg_tr.raise_()
        # self.circularProgress_tr.raise_()
        # self.container_tr.raise_()

        self.verticalLayout_29.addWidget(self.frame_74)

        self.frame_75 = QFrame(self.tabFrame_anal_2)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.frame_78 = QFrame(self.frame_75)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)

        self.pushButton_12 = QPushButton(self.frame_78)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(40, 160, 75, 23))
        self.pushButton_12.setDisabled(False)
        self.pushButton_12.clicked.connect(lambda: self.tab_pages.setCurrentIndex(1))

        self.horizontalLayout_50.addWidget(self.frame_78)

        self.frame_79 = QFrame(self.frame_75)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_79)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_76 = QFrame(self.frame_79)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_78 = QLabel(self.frame_76)
        self.label_78.setObjectName(u"label_78")

        self.horizontalLayout_51.addWidget(self.label_78)

        self.verticalLayout_30.addWidget(self.frame_76)

        self.frame_77 = QFrame(self.frame_79)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_79 = QLabel(self.frame_77)
        self.label_79.setObjectName(u"label_79")

        self.horizontalLayout_52.addWidget(self.label_79)

        self.verticalLayout_30.addWidget(self.frame_77)

        self.frame_80 = QFrame(self.frame_79)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_80 = QLabel(self.frame_80)
        self.label_80.setObjectName(u"label_80")

        self.horizontalLayout_53.addWidget(self.label_80)

        self.verticalLayout_30.addWidget(self.frame_80)

        self.horizontalLayout_50.addWidget(self.frame_79)

        self.verticalLayout_29.addWidget(self.frame_75)

        self.tab_pages.addWidget(self.tabFrame_anal_2)


        ## --------------------------------------------네번째
        self.verticalLayout_6.addWidget(self.tab_pages)

        self.tab_pages.setCurrentIndex(0)

        self.retranslateUi(self)

        ## pre화면 plot
        freq = ['Delta', 'Theta', 'LowAlpha', 'HighAlpha', 'LowBeta', 'HighBeta', 'Gamma']
        absolute_array = [self.A_delta, self.A_theta, self.A_LowAlpha, self.A_HighAlpha, self.A_LowBeta, self.A_HighBeta, self.A_Gamma]
        relative_array = [self.R_delta, self.R_theta, self.R_Lowalpha, self.R_Highalpha, self.R_Lowbeta, self.R_Highbeta, self.R_gamma]
        plv_array = [self.plv_delta, self.plv_theta, self.plv_Lowalpha, self.plv_Highalpha, self.plv_Lowbeta, self.plv_Highbeta, self.plv_gamma]
        wpli_array = [self.wp_delta, self.wp_theta, self.wp_Lowalpha, self.wp_Highalpha, self.wp_Lowbeta, self.wp_Highbeta, self.wp_gamma]
        network_array = [self.n_delta, self.n_theta, self.n_Lowalpha, self.n_Highalpha, self.n_Lowbeta, self.n_Highbeta, self.n_gamma]

        for i in range(7):
            absolute_array[i].setStyleSheet(u"image:url({}/{}_{}/absolute_{}.png)"
                                            .format(root_con, self.num, self.name, freq[i]))
            relative_array[i].setStyleSheet(u"image:url({}/{}_{}/relative_{}.png)"
                                            .format(root_con, self.num, self.name, freq[i]))
            plv_array[i].setStyleSheet(u"image:url({}/{}_{}/plv_{}.png)"
                                            .format(root_con, self.num, self.name, freq[i]))
            wpli_array[i].setStyleSheet(u"image:url({}/{}_{}/plv_{}.png)"
                                       .format(root_con, self.num, self.name, freq[i]))
            network_array[i].setStyleSheet(u"image:url({}/{}_{}/network_{}.png)"
                                        .format(root_con, self.num, self.name, freq[i]))

        ## 분석 화면 plot
        self.label_38.setStyleSheet(u"image:url({}/{}_{}/plv_Theta.png)".format(root_con, self.num, self.name))
        self.label_40.setStyleSheet(u"image:url({}/{}_{}/absolute_Theta.png)".format(root_con, self.num, self.name))
        self.label_52.setStyleSheet(u"image:url({}/{}_{}/network_Theta.png)".format(root_con, self.num, self.name))
        self.label_39.setStyleSheet(u"image:url({}/plot_image/source_2.jpg)".format(ROOT_DIR_con))
        self.label_43.setStyleSheet(u"image:url({}/plot_image/source_1.png)".format(ROOT_DIR_con))
        self.label_68.setStyleSheet(u"image:url({}/plot_image/source_3.png)".format(ROOT_DIR_con))

        # self.label_36.setStyleSheet(u"image:url({}/{}_{}/mode_prob.png)".format(root_con, self.num, self.name))

        self.label_78.setStyleSheet(u"image:url({}/{}_{}/position_plot_0.png)".format(root_con, self.num, self.name))
        self.label_79.setStyleSheet(u"image:url({}/{}_{}/position_plot_1.png)".format(root_con, self.num, self.name))
        self.label_80.setStyleSheet(u"image:url({}/{}_{}/position_plot_2.png)".format(root_con, self.num, self.name))

        ## 가장 유의미한 지표
        # label_list = [self.label_12, self.label_7, self.label_8, self.label_10, self.label_13, self.label_14, self.label_15]
        # with open('{}/{}_{}/info.json'.format(root_con, self.num, self.name), 'r', encoding='utf-8') as f:
        #     self.data = json.load(f)
        # if self.data['best_model'] == 'psd':
        #     for i in range(7):
        #         label_list[i].setStyleSheet((u"image:url({}/{}_{}/absolute_{}.png)"
        #                                     .format(root_con, self.num, self.name, freq[i])))
        #     # self.label_70.setText(QCoreApplication.translate("MainWindow", u"Fp1_θ", None))
        #     # self.label_71.setText(QCoreApplication.translate("MainWindow", u"O2_low_α", None))
        #     # self.label_72.setText(QCoreApplication.translate("MainWindow", u"P8_θ", None))
        # if self.data['best_model'] == 'fc':
        #     for i in range(7):
        #         label_list[i].setStyleSheet((u"image:url({}/{}_{}/plv_{}.png)"
        #                                     .format(root_con, self.num, self.name, freq[i])))
        #     # self.label_70.setText(QCoreApplication.translate("MainWindow", u"F7-C4_δ", None))
        #     # self.label_71.setText(QCoreApplication.translate("MainWindow", u"P4-T7_δ", None))
        #     # self.label_72.setText(QCoreApplication.translate("MainWindow", u"O2-Pz_θ", None))
        # if self.data['best_model'] == 'ni':
        #     for i in range(7):
        #         label_list[i].setStyleSheet((u"image:url({}/{}_{}/network_{}.png)"
        #                                     .format(root_con, self.num, self.name, freq[i])))
        #     # self.label_70.setText(QCoreApplication.translate("MainWindow", u"Fp2-F4_θ", None))
        #     # self.label_71.setText(QCoreApplication.translate("MainWindow", u"T7-C3_δ", None))
        #     # self.label_72.setText(QCoreApplication.translate("MainWindow", u"F7-P3_θ", None))

        # self.label_11.setText(QCoreApplication.translate("MainWindow", u"{} - Most Influential Feature".format(self.data['best_model'].upper()), None))
        # self.label_52.setText(QCoreApplication.translate("MainWindow", u"Most Influential Feature : {}".format(self.data['best_model'].upper()), None))

    def retranslateUi(self, MainWindow):
        ## --------------------------------pre 페이지
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Patient ID:", None))
        self.label_28.setStyleSheet(u"font-style: bold;")
        self.label_29.setText(QCoreApplication.translate("MainWindow", self.num, None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_26.setStyleSheet(u"font-style: bold;")
        self.label_27.setText(QCoreApplication.translate("MainWindow", self.name, None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.label_24.setStyleSheet(u"font-style: bold;")
        self.label_25.setText(QCoreApplication.translate("MainWindow", self.birth, None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Sex:", None))
        self.label_22.setStyleSheet(u"font-style: bold;")
        self.label_23.setText(QCoreApplication.translate("MainWindow", self.sex, None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_20.setStyleSheet(u"font-style: bold;")
        self.label_21.setText(QCoreApplication.translate("MainWindow", self.date, None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Delta (1~4Hz)", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Theta (4~8Hz)", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Low-Alpha (8~10Hz)", None))
        self.label_32_h.setText(QCoreApplication.translate("MainWindow", u"High-Alpha (10~12Hz)", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Low-Beta (12~22Hz)", None))
        self.label_33_h.setText(QCoreApplication.translate("MainWindow", u"High-Beta (22~30Hz)", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Gamma (30~55Hz)", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Absolute Power", None))
        self.A_delta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.A_theta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.A_LowAlpha.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.A_HighAlpha.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.A_LowBeta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.A_HighBeta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.A_Gamma.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Relative Power", None))
        self.R_delta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.R_theta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.R_Lowalpha.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.R_Highalpha.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.R_Lowbeta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.R_Highbeta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.R_gamma.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Functional Connectivity - PLV", None))
        self.plv_delta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.plv_theta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.plv_Lowalpha.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.plv_Highalpha.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.plv_Lowbeta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.plv_Highbeta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.plv_gamma.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Functional Connectivity - WPLI", None))
        self.wp_delta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.wp_theta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.wp_Lowalpha.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.wp_Highalpha.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.wp_Lowbeta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.wp_Highbeta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.wp_gamma.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Network (clustering coeffience)", None))
        self.n_delta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.n_theta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.n_Lowalpha.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.n_Highalpha.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.n_Lowbeta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.n_Highbeta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.n_gamma.setText(QCoreApplication.translate("MainWindow", u"", None))

        ## --------------------------------분석 페이지
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Patient ID:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", self.num, None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", self.name, None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", self.birth, None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Sex:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", self.sex, None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", self.date, None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"File:", None))
        file_split = self.file.split('/')
        self.label_6.setText(QCoreApplication.translate("MainWindow", file_split[-1], None))

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"back", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"next", None))

        self.labelTitle.setText(QCoreApplication.translate("MainWindow",
                                                           u"MDD\nprobabilty",
                                                           None))

        self.labelPercentage.setText(QCoreApplication.translate("MainWindow",
                                                                u"{}%".format(round(float(self.y_pred_proba_mdd), 1)),
                                                                None))

        self.label_62.setText(QCoreApplication.translate("MainWindow", u"\u25a0  MDD Probability", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"\u25a0  HC Probability", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"\u25a0  AI Predict", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"{}", None).format(self.y_pred))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"{}%", None).format(self.y_pred_proba_mdd))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"{}%", None).format(self.y_pred_proba_hc))
        # self.label_68.setText(QCoreApplication.translate("MainWindow", u"{}", None).format(self.best_model.upper()))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"", None))

        self.label_70.setText(QCoreApplication.translate("MainWindow", u"FC-sensor", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Fp1 - Delta", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"PSD-sensor", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"NI-sensor", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"FC-source", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"PSD-source", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"NI-source", None))

        pushButton_list = [self.pushButton_detail, self.pushButton_5, self.pushButton_6, self.pushButton_7,
                           self.pushButton_8, self.pushButton_9, self.pushButton_10]
        for button in pushButton_list:
            button.setText(QCoreApplication.translate("MainWindow", u"Detail", None))

        self.label_73.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))

        self.label_37.setText(QCoreApplication.translate("MainWindow", u" PSD(Power Spectral Density)", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u" FC(Functional Connectivity)", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u" NI(Network Indices)", None))


        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Prediction of MDD %", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Mean of 6 Model Probability", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Predictive Probability by Model", None))
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", u"Best model is Source Functional Connectivity", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Influential Features", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Sensor & Source Level Feature Indices", None))

        ## ------------------------------ 세번쨰 페이지지
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"back", None))

        self.labelTitle_psd_sen.setText(QCoreApplication.translate("MainWindow", u"sensor\n" "PSD", None))
        self.labelPercentage_psd_sen.setText(
            QCoreApplication.translate("MainWindow", u"{}% ".format(round(self.psd_sen * 100)), None))
        self.labelTitle_fc_sen.setText(QCoreApplication.translate("MainWindow", u"sensor\n" "FC", None))
        self.labelPercentage_fc_sen.setText(
            QCoreApplication.translate("MainWindow", u"{}%".format(round(self.fc_sen * 100)), None))
        self.labelTitle_ni_sen.setText(QCoreApplication.translate("MainWindow", u"sensor\n" "NI", None))
        self.labelPercentage_ni_sen.setText(
            QCoreApplication.translate("MainWindow", u"{}%".format(round(self.ni_sen * 100)), None))
        self.labelTitle_psd_sou.setText(QCoreApplication.translate("MainWindow", u"source\n" "PSD", None))
        self.labelPercentage_psd_sou.setText(
            QCoreApplication.translate("MainWindow", u"{}%".format(round(self.psd_sou * 100)), None))
        self.labelTitle_fc_sou.setText(QCoreApplication.translate("MainWindow", u"source\n" "FC", None))
        self.labelPercentage_fc_sou.setText(
            QCoreApplication.translate("MainWindow", u"{}%".format(round(self.fc_sou * 100)), None))
        self.labelTitle_ni_sou.setText(QCoreApplication.translate("MainWindow", u"source\n" "NI", None))
        self.labelPercentage_ni_sou.setText(
            QCoreApplication.translate("MainWindow", u"{}%".format(round(self.ni_sou * 100)), None))

        # self.label_7.setText(QCoreApplication.translate(u"S\nE\nN\nS\nE\nR", None))

    # retranslateUi
    def open_tr_detail(self):
        self._tr_detail_dialog = Ui_Dialog_trDetail()
        self._tr_detail_dialog.setWindowTitle("TR Detail")
        self._tr_detail_dialog.show()

    def open_psd_power(self):
        self._psd_dialog = Ui_Dialog_power(self.name, self.num)
        self._psd_dialog.setWindowTitle("PSD Hz Topomap")
        self._psd_dialog.show()

    def open_source_plot(self):
        self._source_plot = Ui_Dialog_source()
        self._source_plot.setWindowTitle("Source Plot")
        self._source_plot.show()
        # sample_data_folder = mne.datasets.sample.data_path()
        # subjects_dir = os.path.join(sample_data_folder, 'subjects')
        # Brain = mne.viz.get_brain_class()
        # brain = Brain('sample', hemi='lh', surf='pial',
        #               subjects_dir=subjects_dir, size=(800, 600))
        # brain.add_annotation('aparc.a2009s', borders=False)
