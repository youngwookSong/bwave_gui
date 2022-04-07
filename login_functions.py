from main import *
GLOBAL_STATE = 0

class UIFunctions_2(LoginView):
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # if maximized
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            # self.ui.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
            # self.ui.drop_frame.setStyleSheet("border-radius: 0px;")
            self.ui.btn_max.setToolTip("Restore")

        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            # self.ui.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
            # self.ui.drop_frame.setStyleSheet("border-radius: 10px;")
            self.ui.btn_max.setToolTip("Maximize")


    def uiDefinitions(self):
        #remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # MAXIMIZE / RESTORE
        self.ui.btn_max.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # MINIMIZE
        self.ui.btn_min.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW 나중에 구현해야욈
        # self.sizegrip = QSizeGrip(self.ui.frame_grip)
        # self.sizegrip.setStyleSheet(
        #     "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        # self.sizegrip.setToolTip("Resize Window")

    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus(self):
        return GLOBAL_STATE