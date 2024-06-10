from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPropertyAnimation
from main import *


class UIFunctions(MainWindow):
    def __init__(self):
        super().__init__()
        self.animation = None

    def togglemenu(self, maxwidth, enable):
        if enable:
            width = self.ui.frame_left_menu.width()
            maxextend = maxwidth
            standard = 100
            if width == 100:
                widthextended = maxextend
                self.ui.btn_page_1.setText("Лінійна регресія")
                self.ui.btn_page_2.setText("Множинна лінійна \n регресія")
                self.ui.btn_page3.setText("Регресія \n K- найближчих сусідів")
                self.ui.btn_page_4.setText("Класифікація \n K-найближчих сусідів")
                self.ui.btn_page_5.setText("Логістична регресія")
                self.ui.btn_page_6.setText("Перехресна перевірка \n з виключенням по одному")
                self.ui.btn_page_7.setText("k-кратна перехресна \n перевірка")
                self.ui.btn_page_8.setText("Поліномінальна регресія")
                self.ui.btn_page_9.setText("Кубічний сплайн")
                self.ui.btn_page_10.setText("Природний кубічний \n сплайн")
                self.ui.btn_page_11.setText("Рідж-регресія")
                self.ui.btn_page_12.setText("Лассо")
                self.ui.btn_page_13.setText("Регресійні дерева")
                self.ui.btn_page_14.setText("Дерева класифікацій")
                self.ui.btn_page_15.setText("Лінійний \n дискримінантний аналіз")
                self.ui.btn_page_16.setText("Квадратичний \n дискримінантний аналіз")
                font = QtGui.QFont()
                font.setFamily("Georgia")
                font.setPointSize(10)
                self.ui.btn_page_1.setFont(font)
                self.ui.btn_page_2.setFont(font)
                self.ui.btn_page3.setFont(font)
                self.ui.btn_page_4.setFont(font)
                self.ui.btn_page_5.setFont(font)
                self.ui.btn_page_6.setFont(font)
                self.ui.btn_page_7.setFont(font)
                self.ui.btn_page_8.setFont(font)
                self.ui.btn_page_9.setFont(font)
                self.ui.btn_page_10.setFont(font)
                self.ui.btn_page_11.setFont(font)
                self.ui.btn_page_12.setFont(font)
                self.ui.btn_page_13.setFont(font)
                self.ui.btn_page_14.setFont(font)
                self.ui.btn_page_15.setFont(font)
                self.ui.btn_page_16.setFont(font)

            else:
                widthextended = standard
                self.ui.btn_page_1.setText("")
                self.ui.btn_page_2.setText("")
                self.ui.btn_page3.setText("")
                self.ui.btn_page_4.setText("")
                self.ui.btn_page_5.setText("")
                self.ui.btn_page_6.setText("")
                self.ui.btn_page_7.setText("")
                self.ui.btn_page_8.setText("")
                self.ui.btn_page_9.setText("")
                self.ui.btn_page_10.setText("")
                self.ui.btn_page_11.setText("")
                self.ui.btn_page_12.setText("")
                self.ui.btn_page_13.setText("")
                self.ui.btn_page_14.setText("")
                self.ui.btn_page_15.setText("")
                self.ui.btn_page_16.setText("")
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthextended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
