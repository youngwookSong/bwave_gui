from main import *
import sys
import style

# GLOBALS
counter = [0] * 8
jumper = [10] * 8

class progress_functions:
    def __init__(self, tabframe, y_pred_proba_mdd, tr, psd_sen, fc_sen, ni_sen, psd_sou, fc_sou, ni_sou):
        super().__init__()

        self._tabFrame = tabframe
        self.y_pred_proba_mdd = y_pred_proba_mdd
        self.tr = tr
        self.psd_sen = round(psd_sen * 100, 1)
        self.fc_sen = round(fc_sen * 100, 1)
        self.ni_sen = round(ni_sen * 100, 1)
        self.psd_sou = round(psd_sou * 100, 1)
        self.fc_sou = round(fc_sou * 100, 1)
        self.ni_sou = round(ni_sou * 100, 1)

        # max 확률 색깔 다르게 하기
        self.style_base = style.progress_circle_style_base
        self.style_max = progress_circle_style_maxProba

        self.maxProba = max(self.psd_sen, self.fc_sen, self.ni_sen, self.psd_sou, self.fc_sou, self.ni_sou)

        self.progressBarValue(0)
        self.progressBarValue2(0)
        self.progressBarValue3(0)
        self.progressBarValue4(0)
        self.progressBarValue5(0)
        self.progressBarValue6(0)
        self.progressBarValue7(0)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress) #여기에 파라매터 넣으면 안돌아감
        self.timer.start(15)

        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.progress2)
        self.timer2.start(15)

        self.timer3 = QtCore.QTimer()
        self.timer3.timeout.connect(self.progress3)
        self.timer3.start(15)

        self.timer4 = QtCore.QTimer()
        self.timer4.timeout.connect(self.progress4)
        self.timer4.start(15)

        self.timer5 = QtCore.QTimer()
        self.timer5.timeout.connect(self.progress5)
        self.timer5.start(15)

        self.timer6 = QtCore.QTimer()
        self.timer6.timeout.connect(self.progress6)
        self.timer6.start(15)

        self.timer7 = QtCore.QTimer()
        self.timer7.timeout.connect(self.progress7)
        self.timer7.start(15)

    def progress(self):
        global counter
        global jumper
        value = counter[1]

        # 텍스트도 계속 바뀌게 할라면 아래 주석 풀기, ui가서 labelPercentage밑에있는거도 html로 바꿔야됨됨
        # htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""
        #
        # # REPLACE VALUE
        # newHtml = htmlText.replace("{VALUE}", str(jumper))
        #
        # if (value > jumper):
        #     # APPLY NEW PERCENTAGE TEXT
        #     self._tabFrame.labelPercentage.setText(newHtml)
        #     jumper += 10

        if value >= float(self.y_pred_proba_mdd): value = float(self.y_pred_proba_mdd)
        self.progressBarValue(value)

        if counter[1] > float(self.y_pred_proba_mdd):
            self.timer.stop()
            counter[1] = 0
            jumper[1] = 10

        counter[1] += 0.5

    def progress2(self):
        global counter
        global jumper
        value = counter[2]

        if value >= float(self.psd_sen): value = float(self.psd_sen)
        self.progressBarValue2(value)

        if counter[2] > float(self.psd_sen):
            self.timer2.stop()
            counter[2] = 0
            jumper[2] = 10

        counter[2] += 0.5

    def progress3(self):
        global counter
        global jumper
        value = counter[3]

        if value >= float(self.fc_sen): value = float(self.fc_sen)
        self.progressBarValue3(value)

        if counter[3] > float(self.fc_sen):
            self.timer3.stop()
            counter[3] = 0
            jumper[3] = 10

        counter[3] += 0.5

    def progress4(self):
        global counter
        global jumper
        value = counter[4]

        if value >= float(self.ni_sen): value = float(self.ni_sen)
        self.progressBarValue4(value)

        if counter[4] > float(self.ni_sen):
            self.timer4.stop()
            counter[4] = 0
            jumper[4] = 10

        counter[4] += 0.5

    def progress5(self):
        global counter
        global jumper
        value = counter[5]

        if value >= float(self.psd_sou): value = float(self.psd_sou)
        self.progressBarValue5(value)

        if counter[5] > float(self.psd_sou):
            self.timer5.stop()
            counter[5] = 0
            jumper[5] = 10

        counter[5] += 0.5

    def progress6(self):
        global counter
        global jumper
        value = counter[6]

        if value >= float(self.fc_sou): value = float(self.fc_sou)
        self.progressBarValue6(value)

        if counter[6] > float(self.fc_sou):
            self.timer6.stop()
            counter[6] = 0
            jumper[6] = 10

        counter[6] += 0.5

    def progress7(self):
        global counter
        global jumper
        value = counter[7]

        if value >= float(self.ni_sou): value = float(self.ni_sou)
        self.progressBarValue7(value)

        if counter[7] > float(self.ni_sou):
            self.timer7.stop()
            counter[7] = 0
            jumper[7] = 10

        counter[7] += 0.5

    # MDD
    def progressBarValue(self, value):
        styleSheet_1 = """
                    QFrame{
                        border-radius: 150px;
                        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(255, 15, 0, 0.8));
                    }
                    """

        progress = (100 - value) / 100.0

        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        self._tabFrame.circularProgress.setStyleSheet(styleSheet_1.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2))

    # sensor PSD
    def progressBarValue2(self, value):
        if self.psd_sen == self.maxProba:
            styleSheet_2 = self.style_max
        else:
            styleSheet_2 = self.style_base

        progress = (100 - value) / 100.0

        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        self._tabFrame.circularProgress_psd_sen.setStyleSheet(
            styleSheet_2.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2))

    # sensor FC
    def progressBarValue3(self, value):
        if self.fc_sen == self.maxProba:
            styleSheet_3 = self.style_max
        else:
            styleSheet_3 = self.style_base

        progress = (100 - value) / 100.0

        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        self._tabFrame.circularProgress_fc_sen.setStyleSheet(
            styleSheet_3.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2))

    # sensor NI
    def progressBarValue4(self, value):
        if self.ni_sen == self.maxProba:
            styleSheet_4 = self.style_max
        else:
            styleSheet_4 = self.style_base

        progress = (100 - value) / 100.0

        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        self._tabFrame.circularProgress_ni_sen.setStyleSheet(
            styleSheet_4.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2))

    # source PSD
    def progressBarValue5(self, value):
        if self.psd_sou == self.maxProba:
            styleSheet_5 = self.style_max
        else:
            styleSheet_5= self.style_base

        progress = (100 - value) / 100.0

        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        self._tabFrame.circularProgress_psd_sou.setStyleSheet(
            styleSheet_5.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2))

    # source FC
    def progressBarValue6(self, value):
        if self.fc_sou == self.maxProba:
            styleSheet_6 = self.style_max
        else:
            styleSheet_6 = self.style_base

        progress = (100 - value) / 100.0

        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        self._tabFrame.circularProgress_fc_sou.setStyleSheet(
            styleSheet_6.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2))

    # source NI
    def progressBarValue7(self, value):
        if self.ni_sou == self.maxProba:
            styleSheet_7 = self.style_max
        else:
            styleSheet_7 = self.style_base

        progress = (100 - value) / 100.0

        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        self._tabFrame.circularProgress_ni_sou.setStyleSheet(
            styleSheet_7.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2))
