from main import *

GLOBAL_STATE = 0

class UIFunctions(MainView): #ui_main.py의 클래스를 상속
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

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        # self.sizegrip = QSizeGrip(self.ui.frame_grip)
        # self.sizegrip.setStyleSheet(
        #     "QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        # self.sizegrip.setToolTip("Resize Window")

    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus(self):
        return GLOBAL_STATE

    def toggleMenu(self, maxWidth, enable):
        if enable:
            #get width
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            #set max width
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            #animation
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def set_page(self, page):
        self.ui.pages.setCurrentWidget(page)
