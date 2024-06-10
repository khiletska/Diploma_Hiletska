from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from Interface.PageBinomialDistribution import PageBinomialDistribution
from Interface.PageExponentialDistribution import PageExponentialDistribution
from Interface.PageNormalDistribution import PageNormalDistribution
from Interface.PagePoissonDistribution import PagePoissonDistribution
from Interface.PageUniformDistribution import PageUniformDistribution
import random
import numpy as np
import pandas as pd

from Interface.TableWidget import TableWidget


class GenerateWindow(QMainWindow):
    closed = pyqtSignal()  # Сигнал, який відправляється при закритті вікна
    data_transferred = pyqtSignal(pd.DataFrame)  # Сигнал для передачі даних

    def __init__(self):
        QMainWindow.__init__(self)
        self.setObjectName("GenerateWindow")
        self.resize(1063, 800)
        self.setMinimumSize(QtCore.QSize(50, 50))
        self.setStyleSheet("background-color:  rgb(255, 255, 255);")
        self.centralWidget = QtWidgets.QWidget(self, flags=QtCore.Qt.Widget)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Content = QtWidgets.QFrame(self.centralWidget, flags=QtCore.Qt.Widget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content, flags=QtCore.Qt.Widget)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(200, 196, 74)")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu, flags=QtCore.Qt.Widget)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        stl_btn = "QPushButton {\n" \
                  "    color: rgb(255, 255, 255);\n" \
                  "    background-color: rgb(200, 196, 74);\n" \
                  "    border: 2px solid;\n" \
                  "}\n" \
                  "QPushButton:hover {\n" \
                  "    background-color:rgb(211, 207, 78);\n" \
                  "}"
        self.btn_page_1 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_1.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_page_1.setStyleSheet(stl_btn)
        self.btn_page_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Katrusia\\курсова\\Interface\\interface-arrows-button-right-duoble.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_page_1.setIcon(icon1)
        self.btn_page_1.setObjectName("btn_page_1")
        self.verticalLayout_4.addWidget(self.btn_page_1)
        self.btn_page_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_2.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_page_2.setStyleSheet(stl_btn)
        self.btn_page_2.setText("")
        self.btn_page_2.setIcon(icon1)
        self.btn_page_2.setObjectName("btn_page_2")
        self.verticalLayout_4.addWidget(self.btn_page_2)
        self.btn_page3 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page3.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_page3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btn_page3.setStyleSheet(stl_btn)
        self.btn_page3.setText("")
        self.btn_page3.setIcon(icon1)
        self.btn_page3.setObjectName("btn_page3")
        self.verticalLayout_4.addWidget(self.btn_page3)
        self.btn_page_4 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_4.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_page_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btn_page_4.setStyleSheet(stl_btn)
        self.btn_page_4.setText("")
        self.btn_page_4.setIcon(icon1)
        self.btn_page_4.setObjectName("btn_page_4")
        self.verticalLayout_4.addWidget(self.btn_page_4)
        self.btn_page_5 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_5.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_page_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btn_page_5.setStyleSheet(stl_btn)
        self.btn_page_5.setText("")
        self.btn_page_5.setIcon(icon1)
        self.btn_page_5.setObjectName("btn_page_5")
        self.verticalLayout_4.addWidget(self.btn_page_5)

        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.btn_page_1.setFont(font)
        self.btn_page_2.setFont(font)
        self.btn_page3.setFont(font)
        self.btn_page_4.setFont(font)
        self.btn_page_5.setFont(font)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu, alignment=QtCore.Qt.AlignLeft)
        self.frame_pages = QtWidgets.QFrame(self.Content, flags=QtCore.Qt.Widget)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")

        self.normal_distribution = PageNormalDistribution(stl_btn, font)
        self.normal_distribution.generate_btn.clicked.connect(self.click_generate_normal)
        self.normal_distribution.save_btn.clicked.connect(self.click_save_normal)
        self.normal_distribution.analise_btn.clicked.connect(self.transfer_data_normal)
        self.stackedWidget.addWidget(self.normal_distribution)

        self.uniform_distribution = PageUniformDistribution(stl_btn, font)
        self.uniform_distribution.generate_btn.clicked.connect(self.click_generate_uniform)
        self.uniform_distribution.save_btn.clicked.connect(self.click_save_uniform)
        self.uniform_distribution.analise_btn.clicked.connect(self.transfer_data_uniform)
        self.stackedWidget.addWidget(self.uniform_distribution)

        self.exponential_distribution = PageExponentialDistribution(stl_btn, font)
        self.exponential_distribution.generate_btn.clicked.connect(self.click_generate_exponential)
        self.exponential_distribution.save_btn.clicked.connect(self.click_save_exponential)
        self.exponential_distribution.analise_btn.clicked.connect(self.transfer_data_exponential)
        self.stackedWidget.addWidget(self.exponential_distribution)

        self.poisson_distribution = PagePoissonDistribution(stl_btn, font)
        self.poisson_distribution.generate_btn.clicked.connect(self.click_generate_poisson)
        self.poisson_distribution.save_btn.clicked.connect(self.click_save_exponential)
        self.poisson_distribution.analise_btn.clicked.connect(self.transfer_data_exponential)
        self.stackedWidget.addWidget(self.poisson_distribution)

        self.binomial_distribution = PageBinomialDistribution(stl_btn, font)
        self.binomial_distribution.generate_btn.clicked.connect(self.click_generate_binomial)
        self.binomial_distribution.save_btn.clicked.connect(self.click_save_binomial)
        self.binomial_distribution.analise_btn.clicked.connect(self.transfer_data_binomial)
        self.stackedWidget.addWidget(self.binomial_distribution)

        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        self.setCentralWidget(self.centralWidget)

        self.setWindowTitle("Розподіли даних")
        self.btn_page_1.setText("Нормальний розподіл")
        self.btn_page_2.setText("Рівномірний розподіл")
        self.btn_page3.setText("Експоненційний розподіл")
        self.btn_page_4.setText("Розподіл Пуассона")
        self.btn_page_5.setText("Біноміальний розподіл")
        self.normal_distribution.n_label.setText("Кількість елементів")
        self.normal_distribution.mu_x_label.setText("Математичне сподівання (середнє значення) для X ")
        self.normal_distribution.mu_y_label.setText("Математичне сподівання (середнє значення) для y")
        self.normal_distribution.sigma_x_label.setText("Стандартне відхилення для X")
        self.normal_distribution.sigma_y_label.setText("Стандартне відхилення для y")
        self.normal_distribution.random_checked.setText("Згенерувати випадкові параметри")
        self.normal_distribution.generate_btn.setText("Згенерувати")
        self.normal_distribution.save_btn.setText("Зберегти")
        self.normal_distribution.analise_btn.setText("Аналізувати")

        self.uniform_distribution.n_label.setText("Кількість елементів")
        self.uniform_distribution.min_x_label.setText(" Мінімальне значення діапазону для X ")
        self.uniform_distribution.min_y_label.setText("Мінімальне значення діапазону для y")
        self.uniform_distribution.max_x_label.setText("Максимальне значення діапазону для X")
        self.uniform_distribution.max_y_label.setText("Максимальне значення діапазону для y")
        self.uniform_distribution.random_checked.setText("Згенерувати випадкові параметри")
        self.uniform_distribution.generate_btn.setText("Згенерувати")
        self.uniform_distribution.save_btn.setText("Зберегти")
        self.uniform_distribution.analise_btn.setText("Аналізувати")

        self.exponential_distribution.n_label.setText("Кількість елементів")
        self.exponential_distribution.lambda_x_label.setText("Коефіцієнт масштабу для X ")
        self.exponential_distribution.lambda_y_label.setText("Коефіцієнт масштабу для y")
        self.exponential_distribution.random_checked.setText("Згенерувати випадкові параметри")
        self.exponential_distribution.generate_btn.setText("Згенерувати")
        self.exponential_distribution.save_btn.setText("Зберегти")
        self.exponential_distribution.analise_btn.setText("Аналізувати")

        self.poisson_distribution.n_label.setText("Кількість елементів")
        self.poisson_distribution.lambda_x_label.setText("Математичне сподівання (середнє значення) для X ")
        self.poisson_distribution.lambda_y_label.setText("Математичне сподівання (середнє значення) для y")
        self.poisson_distribution.random_checked.setText("Згенерувати випадкові параметри")
        self.poisson_distribution.generate_btn.setText("Згенерувати")
        self.poisson_distribution.save_btn.setText("Зберегти")
        self.poisson_distribution.analise_btn.setText("Аналізувати")

        self.binomial_distribution.n_label.setText("Кількість елементів")
        self.binomial_distribution.k_x_label.setText("Кількість спроб для X ")
        self.binomial_distribution.k_y_label.setText("Кількість спроб для y")
        self.binomial_distribution.p_x_label.setText("Ймовірність успіху для X")
        self.binomial_distribution.p_y_label.setText("Ймовірність успіху для y")
        self.binomial_distribution.random_checked.setText("Згенерувати випадкові параметри")
        self.binomial_distribution.generate_btn.setText("Згенерувати")
        self.binomial_distribution.save_btn.setText("Зберегти")
        self.binomial_distribution.analise_btn.setText("Аналізувати")

        self.btn_page_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.normal_distribution))
        self.btn_page_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.uniform_distribution))
        self.btn_page3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.exponential_distribution))
        self.btn_page_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.poisson_distribution))
        self.btn_page_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.binomial_distribution))
        self.df = None

    def click_generate_normal(self):
        if self.normal_distribution.random_checked.isChecked():
            nx = random.randint(0, 300)
            mu_X = round(random.uniform(0, nx), 4)
            ny = random.randint(0, 200)
            mu_y = round(random.uniform(0, ny), 4)
            kx = random.randint(0, 50)
            sigma_X = round(random.uniform(0, kx), 4)
            ky = random.randint(0, 20)
            sigma_y = round(random.uniform(0, ky), 4)
            self.normal_distribution.lineedit_mu_x.setText(str(mu_X))
            self.normal_distribution.lineedit_mu_y.setText(str(mu_y))
            self.normal_distribution.lineedit_sigma_x.setText(str(sigma_X))
            self.normal_distribution.lineedit_sigma_y.setText(str(sigma_y))

        # Генеруємо дані
        mu_X = float(self.normal_distribution.lineedit_mu_x.text())
        sigma_X = float(self.normal_distribution.lineedit_sigma_x.text())
        n = int(self.normal_distribution.lineedit_n.text())
        mu_y = float(self.normal_distribution.lineedit_mu_y.text())
        sigma_y = float(self.normal_distribution.lineedit_sigma_y.text())

        X = np.random.normal(mu_X, sigma_X, n).reshape(-1, 1)
        y = np.random.normal(mu_y, sigma_y, n)

        # Створюємо DataFrame
        self.normal_distribution.df = pd.DataFrame(np.hstack((X, y.reshape(-1, 1))), columns=['X', 'y'])
        TableWidget().set(self.normal_distribution.tableWidget_2, self.normal_distribution.df)
        # self.df = self.normal_distribution.df

    def click_generate_uniform(self):
        if self.uniform_distribution.random_checked.isChecked():
            nx = random.randint(0, 300)
            min_X = round(random.uniform(0, nx), 4)
            ny = random.randint(0, 200)
            min_y = round(random.uniform(0, ny), 4)
            kx = random.randint(0, 50)
            max_X = round(random.uniform(0, kx), 4)
            ky = random.randint(0, 20)
            max_y = round(random.uniform(0, ky), 4)
            self.uniform_distribution.lineedit_min_x.setText(str(min_X))
            self.uniform_distribution.lineedit_min_y.setText(str(min_y))
            self.uniform_distribution.lineedit_max_x.setText(str(max_X))
            self.uniform_distribution.lineedit_max_y.setText(str(max_y))

        # Генеруємо дані
        min_X = float(self.uniform_distribution.lineedit_min_x.text())
        max_X = float(self.uniform_distribution.lineedit_max_x.text())
        n = int(self.uniform_distribution.lineedit_n.text())
        min_y = float(self.uniform_distribution.lineedit_min_y.text())
        max_y = float(self.uniform_distribution.lineedit_max_y.text())

        X = np.array([round(random.uniform(min_X, max_X), 4) for _ in range(n)])
        y = np.array([round(random.uniform(min_y, max_y), 4) for _ in range(n)])

        # Створюємо DataFrame
        self.uniform_distribution.df = pd.DataFrame({'X': X, 'y': y})
        TableWidget().set(self.uniform_distribution.tableWidget_2, self.uniform_distribution.df)
        # self.df = self.uniform_distribution.df

    def click_generate_exponential(self):
        if self.exponential_distribution.random_checked.isChecked():
            nx = random.randint(0, 20)
            scale_X = round(random.uniform(0, nx), 4)
            ny = random.randint(0, 18)
            scale_y = round(random.uniform(0, ny), 4)
            # kx = random.randint(0, 50)
            # max_X = round(random.uniform(0, kx),4)
            # ky = random.randint(0, 20)
            # max_y = round(random.uniform(0, ky),4)
            self.exponential_distribution.lineedit_lambda_x.setText(str(scale_X))
            self.exponential_distribution.lineedit_lambda_y.setText(str(scale_y))
            # self.uniform_distribution.lineedit_max_x.setText(str(max_X))
            # self.uniform_distribution.lineedit_max_y.setText(str(max_y))

        # Генеруємо дані
        scale_X = float(self.exponential_distribution.lineedit_lambda_x.text())
        scale_y = float(self.exponential_distribution.lineedit_lambda_y.text())
        n = int(self.exponential_distribution.lineedit_n.text())
        # min_y = float(self.uniform_distribution.lineedit_min_y.text())
        # max_y = float(self.uniform_distribution.lineedit_max_y.text())

        X = np.random.exponential(scale=scale_X, size=n)
        y = np.random.exponential(scale=scale_y, size=n)

        # Створюємо DataFrame
        self.exponential_distribution.df = pd.DataFrame({'X': X, 'y': y})
        TableWidget().set(self.exponential_distribution.tableWidget_2, self.exponential_distribution.df)
        # self.df = self.exponential_distribution.df

    def click_generate_poisson(self):
        if self.poisson_distribution.random_checked.isChecked():
            nx = random.randint(0, 300)
            lambda_X = round(random.uniform(0, nx), 4)
            ny = random.randint(0, 180)
            lambda_y = round(random.uniform(0, ny), 4)
            # kx = random.randint(0, 50)
            # max_X = round(random.uniform(0, kx),4)
            # ky = random.randint(0, 20)
            # max_y = round(random.uniform(0, ky),4)
            self.poisson_distribution.lineedit_lambda_x.setText(str(lambda_X))
            self.poisson_distribution.lineedit_lambda_y.setText(str(lambda_y))
            # self.uniform_distribution.lineedit_max_x.setText(str(max_X))
            # self.uniform_distribution.lineedit_max_y.setText(str(max_y))

        # Генеруємо дані
        lambda_X = float(self.poisson_distribution.lineedit_lambda_x.text())
        lambda_y = float(self.poisson_distribution.lineedit_lambda_y.text())
        n = int(self.poisson_distribution.lineedit_n.text())
        # min_y = float(self.uniform_distribution.lineedit_min_y.text())
        # max_y = float(self.uniform_distribution.lineedit_max_y.text())

        X = np.random.poisson(lambda_X, n)
        y = np.random.poisson(lambda_y, n)

        # Створюємо DataFrame
        self.poisson_distribution.df = pd.DataFrame({'X': X, 'y': y})
        TableWidget().set(self.poisson_distribution.tableWidget_2, self.poisson_distribution.df)
        # self.df = self.poisson_distribution.df

    def click_generate_binomial(self):
        if self.binomial_distribution.random_checked.isChecked():
            nx = random.randint(0, 300)
            try_X = round(random.uniform(0, nx), 4)
            ny = random.randint(0, 200)
            try_y = round(random.uniform(0, ny), 4)
            # kx = random.randint(0, 1)
            prob_X = round(random.uniform(0, 1), 4)
            # ky = random.randint(0, 20)
            prob_y = round(random.uniform(0, 1), 4)
            self.binomial_distribution.lineedit_k_x.setText(str(try_X))
            self.binomial_distribution.lineedit_k_y.setText(str(try_y))
            self.binomial_distribution.lineedit_p_x.setText(str(prob_X))
            self.binomial_distribution.lineedit_p_y.setText(str(prob_y))

        # Генеруємо дані
        try_X = float(self.binomial_distribution.lineedit_k_x.text())
        prob_X = float(self.binomial_distribution.lineedit_p_x.text())
        n = int(self.binomial_distribution.lineedit_n.text())
        try_y = float(self.binomial_distribution.lineedit_k_y.text())
        prob_y = float(self.binomial_distribution.lineedit_p_y.text())

        X = np.random.binomial(try_X, prob_X, n)
        y = np.random.binomial(try_y, prob_y, n)

        # Створюємо DataFrame
        self.binomial_distribution.df = pd.DataFrame({'X': X, 'y': y})
        TableWidget().set(self.binomial_distribution.tableWidget_2, self.binomial_distribution.df)
        # self.df = self.binomial_distribution.df

    def click_save_normal(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save CSV", "", "CSV Files (*.csv);;All Files (*)",
                                                             options=options)

        if file_path:
            self.normal_distribution.df.to_csv(file_path, index=False)
            print(f"File saved to {file_path}")

    def transfer_data_normal(self):
        self.df=self.normal_distribution.df
        self.data_transferred.emit(self.df)

    def click_save_uniform(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save CSV", "", "CSV Files (*.csv);;All Files (*)",
                                                             options=options)

        if file_path:
            self.uniform_distribution.df.to_csv(file_path, index=False)
            print(f"File saved to {file_path}")

    def transfer_data_uniform(self):
        self.df=self.uniform_distribution.df
        self.data_transferred.emit(self.df)

    def click_save_exponential(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save CSV", "", "CSV Files (*.csv);;All Files (*)",
                                                             options=options)

        if file_path:
            self.exponential_distribution.df.to_csv(file_path, index=False)
            print(f"File saved to {file_path}")

    def transfer_data_exponential(self):
        self.df=self.exponential_distribution.df
        self.data_transferred.emit(self.df)

    def click_save_poisson(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save CSV", "", "CSV Files (*.csv);;All Files (*)",
                                                             options=options)

        if file_path:
            self.poisson_distribution.df.to_csv(file_path, index=False)
            print(f"File saved to {file_path}")

    def transfer_data_poisson(self):
        self.df=self.poisson_distribution.df
        self.data_transferred.emit(self.df)

    def click_save_binomial(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save CSV", "", "CSV Files (*.csv);;All Files (*)",
                                                             options=options)

        if file_path:
            self.binomial_distribution.df.to_csv(file_path, index=False)
            print(f"File saved to {file_path}")

    def transfer_data_binomial(self):
        self.df=self.binomial_distribution.df
        self.data_transferred.emit(self.df)

    def closeEvent(self, event):
        self.closed.emit()  # Відправляємо сигнал про закриття вікна
