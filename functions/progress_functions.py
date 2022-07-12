from main import *
import sys

# GLOBALS
counter = [0,0,0]
jumper = [10,10,10]

class progress_functions:
    def __init__(self, tabframe, y_pred_proba_mdd, tr):
        super().__init__()

        self._tabFrame = tabframe
        self.y_pred_proba_mdd = y_pred_proba_mdd
        self.tr = tr
        self.progressBarValue(0)
        # self.progressBarValue2(0)
        # self.progressBarValue3(0)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress) #여기에 파라매터 넣으면 안돌아감
        self.timer.start(15)
        # self.timer2 = QtCore.QTimer()
        # self.timer2.timeout.connect(self.progress2)
        # self.timer2.start(15)
        # self.timer3 = QtCore.QTimer()
        # self.timer3.timeout.connect(self.progress3)
        # self.timer3.start(15)

    def progress(self):
        global counter
        global jumper
        value = counter[0]

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

        if counter[0] > float(self.y_pred_proba_mdd):
            self.timer.stop()
            counter[0] = 0
            jumper[0] = 10

        counter[0] += 0.5

    # def progress2(self):
    #     global counter
    #     global jumper
    #     value = counter[1]
    #
    #     if value >= float(self.tr): value = float(self.tr)
    #     self.progressBarValue2(value)
    #
    #     if counter[1] > float(self.tr):
    #         self.timer2.stop()
    #         counter[1] = 0
    #         jumper[1] = 10
    #
    #     counter[1] += 0.5
    #
    # def progress3(self):
    #     global counter
    #     global jumper
    #     value = counter[2]
    #
    #     if value >= float(self.gr): value = float(self.gr)
    #     self.progressBarValue3(value)
    #
    #     if counter[2] > float(self.gr):
    #         self.timer3.stop()
    #         counter[2] = 0
    #         jumper[2] = 10
    #
    #     counter[2] += 0.5

    def progressBarValue(self, value):
        styleSheet_1 = """
                    QFrame{
                        border-radius: 150px;
                        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(255, 90, 0, 255));
                    }
                    """

        progress = (100 - value) / 100.0

        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        self._tabFrame.circularProgress.setStyleSheet(styleSheet_1.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2))

    # def progressBarValue2(self, value):
    #     styleSheet_2 = """
    #                 QFrame{
    #                     border-radius: 100px;
    #                     background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(255, 15, 0, 1));
    #                 }
    #                 """
    #
    #     progress = (100 - value) / 100.0
    #
    #     stop_1 = str(progress - 0.001)
    #     stop_2 = str(progress)
    #
    #     self._tabFrame.circularProgress_tr.setStyleSheet(
    #         styleSheet_2.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2))
    #
    # def progressBarValue3(self, value):
    #     styleSheet_2 = """
    #                 QFrame{
    #                     border-radius: 100px;
    #                     background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(255, 15, 0, 1));
    #                 }
    #                 """
    #
    #     progress = (100 - value) / 100.0
    #
    #     stop_1 = str(progress - 0.001)
    #     stop_2 = str(progress)
    #
    #     self._tabFrame.circularProgress_gr.setStyleSheet(
    #         styleSheet_2.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2))
