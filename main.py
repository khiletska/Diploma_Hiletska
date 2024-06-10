from Interface.UIFunctions import *
from Interface.ui_main import UiMainWindow
import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = UiMainWindow()
        self.ui.set_up_ui(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.data)
        self.ui.Btn_home.clicked.connect(lambda: UIFunctions.togglemenu(self, 250, True))
        self.ui.btn_data.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.data))
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_page3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.btn_page_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.ui.btn_page_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5))
        self.ui.btn_page_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_6))
        self.ui.btn_page_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_7))
        self.ui.btn_page_8.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_8))
        self.ui.btn_page_9.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_9))
        self.ui.btn_page_10.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_10))
        self.ui.btn_page_11.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_11))
        self.ui.btn_page_12.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_12))
        self.ui.btn_page_13.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_13))
        self.ui.btn_page_14.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_14))
        self.ui.btn_page_15.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_15))
        self.ui.btn_page_16.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_16))
        self.show()

    def closeEvent(self, event):
        if self.ui.generate_data_window:  # Закриваємо вікно з даними, якщо воно відкрите
            self.ui.generate_data_window.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
