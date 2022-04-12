from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *

class Ui_tabFrame_pre(QFrame):
    def __init__(self, current_tab, file, name, birth, num, date, sex):
        super().__init__()
        self.current_tab = current_tab
        self.file = file
        self.name = name
        self.birth = birth
        self.num = num
        self.date = date
        self.sex = sex
        # self.y_pred = y_pred
        # self.y_pred_proba = y_pred_proba

        self.verticalLayout_6 = QVBoxLayout(self.current_tab)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.current_tab)
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

        self.verticalLayout_6.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.current_tab)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.frame_39)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMaximumSize(QSize(100, 16777215))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_26.addWidget(self.frame_44)

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

        self.label_33 = QLabel(self.frame_48)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_33)

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

        self.A_Alpha = QLabel(self.frame_55)
        self.A_Alpha.setObjectName(u"A_Alpha")
        self.A_Alpha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.A_Alpha)

        self.A_Beta = QLabel(self.frame_55)
        self.A_Beta.setObjectName(u"A_Beta")
        self.A_Beta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.A_Beta)

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

        self.R_alpha = QLabel(self.frame_58)
        self.R_alpha.setObjectName(u"R_alpha")
        self.R_alpha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.R_alpha)

        self.R_beta = QLabel(self.frame_58)
        self.R_beta.setObjectName(u"R_beta")
        self.R_beta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.R_beta)

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

        self.plv_alpha = QLabel(self.frame_57)
        self.plv_alpha.setObjectName(u"plv_alpha")
        self.plv_alpha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.plv_alpha)

        self.plv_beta = QLabel(self.frame_57)
        self.plv_beta.setObjectName(u"plv_beta")
        self.plv_beta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.plv_beta)

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

        self.wp_alpha = QLabel(self.frame_56)
        self.wp_alpha.setObjectName(u"wp_alpha")
        self.wp_alpha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.wp_alpha)

        self.wp_beta = QLabel(self.frame_56)
        self.wp_beta.setObjectName(u"wp_beta")
        self.wp_beta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.wp_beta)

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

        self.n_alpha = QLabel(self.frame_54)
        self.n_alpha.setObjectName(u"n_alpha")
        self.n_alpha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.n_alpha)

        self.n_beta = QLabel(self.frame_54)
        self.n_beta.setObjectName(u"n_beta")
        self.n_beta.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.n_beta)

        self.n_gamma = QLabel(self.frame_54)
        self.n_gamma.setObjectName(u"n_gamma")
        self.n_gamma.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.n_gamma)

        self.verticalLayout_23.addWidget(self.frame_54)

        self.verticalLayout_22.addWidget(self.frame_49)

        self.horizontalLayout_26.addWidget(self.frame_46)

        self.frame_47 = QFrame(self.frame_39)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMaximumSize(QSize(100, 16777215))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)

        self.verticalLayout_28 = QVBoxLayout(self.frame_47)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_61 = QFrame(self.frame_47)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMaximumSize(QSize(16777215, 50))
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)

        self.verticalLayout_28.addWidget(self.frame_61)

        self.frame_60 = QFrame(self.frame_47)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMaximumSize(QSize(16777215, 200))
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_60)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_36 = QLabel(self.frame_60)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_29.addWidget(self.label_36)

        self.verticalLayout_28.addWidget(self.frame_60)

        self.frame_59 = QFrame(self.frame_47)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)

        self.verticalLayout_28.addWidget(self.frame_59)

        self.horizontalLayout_26.addWidget(self.frame_47)

        self.verticalLayout_6.addWidget(self.frame_39)

        self.retranslateUi(self)

        ## plot
        freq = ["Delta", "Theta", "Alpha", "Beta", "Gamma"]
        absolute_array = [self.A_delta, self.A_theta, self.A_Alpha, self.A_Beta, self.A_Gamma]
        relative_array = [self.R_delta, self.R_theta, self.R_alpha, self.R_beta, self.R_gamma]
        plv_array = [self.plv_delta, self.plv_theta, self.plv_alpha, self.plv_beta, self.plv_gamma]
        wpli_array = [self.wp_delta, self.wp_theta, self.wp_alpha, self.wp_beta, self.wp_gamma]
        network_array = [self.n_delta, self.n_theta, self.n_alpha, self.n_beta, self.n_gamma]

        for i in range(5):
            absolute_array[i].setStyleSheet(u"image:url(./personal_data/{}_{}/absolute_{}.png)"
                                            .format(self.num, self.name, freq[i]))
            relative_array[i].setStyleSheet(u"image:url(./personal_data/{}_{}/relative_{}.png)"
                                            .format(self.num, self.name, freq[i]))
            plv_array[i].setStyleSheet(u"image:url(./personal_data/{}_{}/plv_{}.png)"
                                            .format(self.num, self.name, freq[i]))
            wpli_array[i].setStyleSheet(u"image:url(./personal_data/{}_{}/plv_{}.png)"
                                       .format(self.num, self.name, freq[i]))
            network_array[i].setStyleSheet(u"image:url(./personal_data/{}_{}/network_{}.png)"
                                        .format(self.num, self.name, freq[i]))

        # self.label_36.setStyleSheet(u"image:url(./icon/plot.png)")

    def retranslateUi(self, MainWindow):
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Patient ID:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", self.num, None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", self.name, None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", self.birth, None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Sex:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", self.sex, None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", self.date, None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Delta", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Theta", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Alpha", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Beta", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Gamma", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Absolute Power", None))
        self.A_delta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.A_theta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.A_Alpha.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.A_Beta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.A_Gamma.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Relative Power", None))
        self.R_delta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.R_theta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.R_alpha.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.R_beta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.R_gamma.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Functional Connectivity - PLV", None))
        self.plv_delta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.plv_theta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.plv_alpha.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.plv_beta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.plv_gamma.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Functional Connectivity - WPLI", None))
        self.wp_delta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.wp_theta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.wp_alpha.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.wp_beta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.wp_gamma.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.n_delta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.n_theta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.n_alpha.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.n_beta.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.n_gamma.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_36.setText("")

    # retranslateUi
