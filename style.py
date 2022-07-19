## style sheet

btn_style = (u"QPushButton{\n"
            "	color: rgb(255, 255, 255);\n"
            "	\n"
            "	background-color: rgb(77, 90, 140);\n"
            "	border:0px solid;\n"
            "	border-radius:4px;\n"
            "   font-size: 14px;\n"
            "   font-style: bold;\n"
            "}\n"
            "QPushButton:hover{\n"
            "	\n"
            "	background-color: rgba(77, 90, 140, 0.5);\n"
            "}"
)

tab_btn_style = (u"QPushButton{\n"
            "	background-color: rgb(215, 221, 224);\n"
            "	border:0px solid;\n"
            "	border-radius:4px;\n"
            "   font-size: 12px;\n"
            "   font-style: bold;\n"
            "}\n"
            "QPushButton:hover{\n"
            "	\n"
            "	background-color: rgba(215, 221, 224, 0.5);\n"
            "}"
)

tab_btn_style_bot = (u"QPushButton:hover{\n"
            "	\n"
            "	color: rgb(27, 64, 247);\n"
            "}"
)


more_btn_style = (u"QPushButton{\n"
            "	color: rgb(0, 0, 0);\n"
            "	border:0px solid;\n"
            "	border-radius:4px;\n"
            "   font-size: 14px;\n"
            "   font-style: bold;\n"
            "   text-decoration: underline;\n"
            "}\n"
            "QPushButton:hover{\n"
            "color: rgb(5, 92, 232);\n"
            "}"
)

style = (u"QPushButton{\n"
        "	font: 75 14pt \"\ub9d1\uc740 \uace0\ub515\";\n"
        "	\n"
        "	border:0px solid;\n"
        "   text-align: left;\n"
        "   padding-left: 10px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "	\n"
        "	background-color: rgb(153, 153, 153);\n"
        "}"
)

close_style = (u"QPushButton{\n"
        "	font: 75 14pt \"\ub9d1\uc740 \uace0\ub515\";\n"
        "	\n"
        "	border:0px solid;\n"
        "   text-align: center;\n"
        "}\n"
        "QPushButton:hover{\n"
        "	\n"
        "	background-color: rgb(153, 153, 153);\n"
        "}"
)


active_style = (u"QPushButton{\n"
            "	font: 75 14pt \"\ub9d1\uc740 \uace0\ub515\";\n"
            "	color: rgb(255, 255, 255);\n"
            "	\n"
            "	background-color: rgb(153, 153, 153);\n"
            "	border:0px solid;\n"
            "   text-align: left;\n"
            "   padding-left: 10px;\n"
            "}"
)

active_close_style = (u"QPushButton{\n"
            "	font: 75 14pt \"\ub9d1\uc740 \uace0\ub515\";\n"
            "	color: rgb(255, 255, 255);\n"
            "	\n"
            "	background-color: rgb(153, 153, 153);\n"
            "	border:0px solid;\n"
            "   text-align: center;\n"
            "}"
)

main_btn_style = (u"QPushButton{\n"
        "	font: 75 18pt \"\ub9d1\uc740 \uace0\ub515\";\n"
        "	color: rgb(255, 255, 255);\n"
        "	\n"
        "	background-color: rgb(129, 129, 129);\n"
        "	border:0px solid;\n"
        "   padding: 10px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "	\n"
        "	background-color: rgb(152, 255, 140);\n"
        "}"
)

progress_circle_style_base = """
                    QFrame{
                        border-radius: 60px;
                        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(255, 90, 0, 1));
                    }
                    """

progress_circle_style_maxProba = """
                    QFrame{
                        border-radius: 60px;
                        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(15, 130, 255, 0.8));
                    }
                    """

