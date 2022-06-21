from main import *
import sys

# GLOBALS
counter = 0
jumper = 10

class progress_functions:
    def __init__(self, tabframe, y_pred_proba_mdd, y_pred, tr, gr):
        super().__init__()

        self._tabFrame = tabframe
        self.y_pred_proba_mdd = y_pred_proba_mdd
        self.y_pred = y_pred
        self.tr = tr
        self.gr = gr
        self.progressBarValue(0)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.progress) #여기에 파라매터 넣으면 안돌아감
        # TIMER IN MILLISECONDS
        self.timer.start(15)

    def progress(self):
        global counter
        global jumper
        value = counter

        # 텍스트도 계속 바뀌게 할라면 아래 주석 풀기, ui가서 labelPercentage밑에있는거도 html로 바꿔야됨됨
       # # HTML TEXT PERCENTAGE
        # htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""
        #
        # # REPLACE VALUE
        # newHtml = htmlText.replace("{VALUE}", str(jumper))
        #
        # if (value > jumper):
        #     # APPLY NEW PERCENTAGE TEXT
        #     self._tabFrame.labelPercentage.setText(newHtml)
        #     jumper += 10

        # SET VALUE TO PROGRESS BAR
        if value >= float(self.y_pred_proba_mdd): value = float(self.y_pred_proba_mdd)
        self.progressBarValue(value)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > float(self.y_pred_proba_mdd):
            # STOP TIMER
            self.timer.stop()
            counter = 0
            jumper = 10

        # INCREASE COUNTER
        counter += 0.5

    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet_1 = """
                    QFrame{
                        border-radius: 150px;
                        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(255, 90, 0, 255));
                    }
                    """

        styleSheet_2 = """
                    QFrame{
                        border-radius: 100px;
                        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(255, 90, 0, 255));
                    }
                    """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET

        # APPLY STYLESHEET WITH NEW VALUES
        self._tabFrame.circularProgress.setStyleSheet(styleSheet_1.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2))
        self._tabFrame.circularProgress_tr.setStyleSheet(styleSheet_2.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2))
        self._tabFrame.circularProgress_gr.setStyleSheet(
            styleSheet_2.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2))