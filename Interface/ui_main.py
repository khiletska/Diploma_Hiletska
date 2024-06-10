import numpy as np
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog

from Interface.GenerateWindow import GenerateWindow
from Interface.PafeLasso import PageLasso
from Interface.PageClassificationTree import PageClassificationTree
from Interface.PageCrossValidation import PageCrossValidation
from Interface.PageCubicSpline import PageCubicSpline
from Interface.PageKCrossValidation import PageKCrossValidation
from Interface.PageKNNClassification import PageKNNClassification
from Interface.PageKNNRegression import PageKNNRegression
from Interface.PageLinearDiscriminant import PageLinearDiscriminant
from Interface.PageLinearRegression import PageLinearRegression
from Interface.PageLogisticRegression import PageLogisticRegression
from Interface.PageMultipleLinearRegression import PageMultipleLinearRegression
from Interface.PageNaturalCubicSpline import PageNaturalCubicSpline
from Interface.PagePolynomialRegression import PagePolynomialRegression
from Interface.PageQuadraticDiscriminant import PageQuadraticDiscriminant
from Interface.PageRegressionTree import PageRegressionTree
from Interface.PageRidgeRegression import PageRidgeRegression
from Methods.KNNClassification import KNNClassification
from Methods.KNNRegression import KNNRegression
from Methods.LeaveOneOutCrossValidation import LeaveOneOutCrossValidation
from Methods.LinearRegresion import LinearRegression
from Methods.LogisticRegression import MyLogisticRegression
from Methods.MultipleLinearRegression import MultipleLinearRegression
from Methods.Naturalcubicspline import NaturalCubicSpline
from Methods.PolynomialRegression import PolynomialRegression
from Methods.Cubicspline import CubicSpline
from Methods.RidgeRegression import RidgeRegression
from Methods.LassoRegression import LassoRegression
from Methods.RegressionTree import RegressionTree
from Methods.ClassificationTree import ClassificationTree
from Methods.LinearDiscriminant import LinearDiscriminant
from Methods.QuadraticDiscriminant import QuadraticDiscriminant
from Interface.TableWidget import TableWidget
from Interface.PageData import PageData
import matplotlib
from Methods.kFoldCrossValidation import KFoldCrossValidation

matplotlib.use('Qt5Agg')


class UiMainWindow(object):
    def __init__(self):
        self.page_16 = None
        self.page_15 = None
        self.page_14 = None
        self.page_13 = None
        self.page_12 = None
        self.page_11 = None
        self.page_10 = None
        self.page_9 = None
        self.page_8 = None
        self.page_7 = None
        self.page_6 = None
        self.page_5 = None
        self.page_4 = None
        self.page_3 = None
        self.page_2 = None
        self.page_1 = None
        self.data = None
        self.stackedWidget = None
        self.verticalLayout_5 = None
        self.frame_pages = None
        self.btn_page_15 = None
        self.btn_page_16 = None
        self.btn_page_14 = None
        self.btn_page_13 = None
        self.btn_page_12 = None
        self.btn_page_11 = None
        self.btn_page_10 = None
        self.btn_page_9 = None
        self.btn_page_8 = None
        self.btn_page_7 = None
        self.btn_page_6 = None
        self.btn_page_5 = None
        self.btn_page_4 = None
        self.btn_page3 = None
        self.btn_page_2 = None
        self.btn_page_1 = None
        self.btn_data = None
        self.Btn_home = None
        self.verticalLayout_4 = None
        self.frame_top_menus = None
        self.verticalLayout_3 = None
        self.frame_left_menu = None
        self.horizontalLayout_2 = None
        self.Content = None
        self.verticalLayout = None
        self.centralWidget = None
        self.verticalLayout_30 = None
        self.horizontalLayout_30 = None
        self.generate_data_window = None  # Додано атрибут для зберігання вікна з даними

        self._data = pd.DataFrame()
        self._X = []
        self._X_multy = []
        self._y = 0
        self._y_multy = 0
        self._X_knn_regression = []
        self._y_knn_regression = 0
        self._X_knnClassification = []
        self._y_knnClassification = 0
        self._X_LogisticRegression = []
        self._y_LogisticRegression = 0
        self._X_CrossValidation = []
        self._y_CrossValidation = 0
        self._X_kCrossValidation = []
        self._y_kCrossValidation = 0
        self._X_PolynomialRegression = []
        self._y_PolynomialRegression = 0
        self._X_CubicSpline = []
        self._y_CubicSpline = 0
        self._X_NaturalCubicSpline = []
        self._y_NaturalCubicSpline = 0
        self._X_ridge = []
        self._y_ridge = 0
        self._X_lasso = []
        self._y_lasso = 0
        self._X_regression_tree = []
        self._y_regression_tree = 0
        self._X_cl_tree = []
        self._y_cl_tree = 0
        self._X_LinearDiscriminant = []
        self._y_LinearDiscriminant = 0
        self._X_QuadraticDiscriminant = []
        self._y_QuadraticDiscriminant = 0

    def set_up_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(1063, 800)
        main_window.setMinimumSize(QtCore.QSize(50, 50))
        main_window.setStyleSheet("background-color:  rgb(255, 255, 255);")
        self.centralWidget = QtWidgets.QWidget(main_window, flags=QtCore.Qt.Widget)
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
        self.frame_left_menu.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(100, 16777215))
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
        self.Btn_home = QtWidgets.QPushButton(self.frame_top_menus)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.Btn_home.sizePolicy().hasHeightForWidth())
        self.Btn_home.setSizePolicy(size_policy)
        self.Btn_home.setMinimumSize(QtCore.QSize(70, 50))
        self.Btn_home.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Btn_home.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "border: 2px solid;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Katrusia\\курсова\\Interface\\interface-setting-menu-1.png"),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.Btn_home.setIcon(icon)
        self.Btn_home.setObjectName("Btn_home")
        self.verticalLayout_4.addWidget(self.Btn_home)
        self.btn_data = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_data.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        stl_btn = "QPushButton {\n" \
                  "    color: rgb(255, 255, 255);\n" \
                  "    background-color: rgb(200, 196, 74);\n" \
                  "    border: 2px solid;\n" \
                  "}\n" \
                  "QPushButton:hover {\n" \
                  "    background-color:rgb(211, 207, 78);\n" \
                  "}"
        self.btn_data.setFont(font)
        self.btn_data.setStyleSheet(stl_btn)
        self.btn_data.setObjectName("btn_data")
        self.verticalLayout_4.addWidget(self.btn_data)
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
        self.btn_page_6 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_6.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_page_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btn_page_6.setStyleSheet(stl_btn)
        self.btn_page_6.setText("")
        self.btn_page_6.setIcon(icon1)
        self.btn_page_6.setObjectName("btn_page_6")
        self.verticalLayout_4.addWidget(self.btn_page_6)
        self.btn_page_7 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_7.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_page_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btn_page_7.setFont(font)
        self.btn_page_7.setStyleSheet(stl_btn)
        self.btn_page_7.setText("")
        self.btn_page_7.setIcon(icon1)
        self.btn_page_7.setObjectName("btn_page_7")
        self.verticalLayout_4.addWidget(self.btn_page_7)
        self.btn_page_8 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_8.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_page_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btn_page_8.setFont(font)
        self.btn_page_8.setStyleSheet(stl_btn)
        self.btn_page_8.setText("")
        self.btn_page_8.setIcon(icon1)
        self.btn_page_8.setObjectName("btn_page_8")
        self.verticalLayout_4.addWidget(self.btn_page_8)
        self.btn_page_9 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_9.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_page_9.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btn_page_9.setFont(font)
        self.btn_page_9.setStyleSheet(stl_btn)
        self.btn_page_9.setText("")
        self.btn_page_9.setIcon(icon1)
        self.btn_page_9.setObjectName("btn_page_9")
        self.verticalLayout_4.addWidget(self.btn_page_9)
        self.btn_page_10 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_10.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_page_10.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btn_page_10.setStyleSheet(stl_btn)
        self.btn_page_10.setText("")
        self.btn_page_10.setIcon(icon1)
        self.btn_page_10.setObjectName("btn_page_10")
        self.verticalLayout_4.addWidget(self.btn_page_10)
        self.btn_page_11 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_11.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_page_11.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btn_page_11.setFont(font)
        self.btn_page_11.setStyleSheet(stl_btn)
        self.btn_page_11.setText("")
        self.btn_page_11.setIcon(icon1)
        self.btn_page_11.setObjectName("btn_page_11")
        self.verticalLayout_4.addWidget(self.btn_page_11)

        self.btn_page_12 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_12.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_page_12.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btn_page_12.setFont(font)
        self.btn_page_12.setStyleSheet(stl_btn)
        self.btn_page_12.setText("")
        self.btn_page_12.setIcon(icon1)
        self.btn_page_12.setObjectName("btn_page_12")
        self.verticalLayout_4.addWidget(self.btn_page_12)

        self.btn_page_13 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_13.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_page_13.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btn_page_13.setFont(font)
        self.btn_page_13.setStyleSheet(stl_btn)
        self.btn_page_13.setText("")
        self.btn_page_13.setIcon(icon1)
        self.btn_page_13.setObjectName("btn_page_13")
        self.verticalLayout_4.addWidget(self.btn_page_13)

        self.btn_page_14 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_14.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_page_14.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btn_page_14.setFont(font)
        self.btn_page_14.setStyleSheet(stl_btn)
        self.btn_page_14.setText("")
        self.btn_page_14.setIcon(icon1)
        self.btn_page_14.setObjectName("btn_page_14")
        self.verticalLayout_4.addWidget(self.btn_page_14)

        self.btn_page_15 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_15.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_page_15.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btn_page_15.setFont(font)
        self.btn_page_15.setStyleSheet(stl_btn)
        self.btn_page_15.setText("")
        self.btn_page_15.setIcon(icon1)
        self.btn_page_15.setObjectName("btn_page_15")
        self.verticalLayout_4.addWidget(self.btn_page_15)

        self.btn_page_16 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_16.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_page_16.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btn_page_16.setFont(font)
        self.btn_page_16.setStyleSheet(stl_btn)
        self.btn_page_16.setText("")
        self.btn_page_16.setIcon(icon1)
        self.btn_page_16.setObjectName("btn_page_16")
        self.verticalLayout_4.addWidget(self.btn_page_16)

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

        self.data = PageData(stl_btn, font)
        self.data.btn_open.clicked.connect(self.clicker)
        self.data.btn_generate.clicked.connect(self.new_window)
        self.stackedWidget.addWidget(self.data)

        self.page_1 = PageLinearRegression(stl_btn, font)
        self.page_1.comboBox_x.activated.connect(self.chosen)
        self.page_1.comboBox_y.activated.connect(self.chosen)
        self.stackedWidget.addWidget(self.page_1)

        # ----------------Page Multiple Linear Regression-------------------------
        self.page_2 = PageMultipleLinearRegression(stl_btn, font)
        self.page_2.combobox_x_multy_regression.activated.connect(self.chosen_multy_regression)
        self.page_2.comboBox_y_multy_regression.activated.connect(self.chosen_multy_regression)
        self.stackedWidget.addWidget(self.page_2)

        # ----------------Page KNN Regression-------------------------
        self.page_3 = PageKNNRegression(stl_btn, font)
        self.page_3.combobox_x_knnRegression.activated.connect(self.chosen_knn_regression)
        self.page_3.comboBox_Y_knnRegression.activated.connect(self.chosen_knn_regression)
        self.stackedWidget.addWidget(self.page_3)
        # -----------------Page4 -----------------
        self.page_4 = PageKNNClassification(stl_btn, font)
        self.page_4.combobox_x_knnClassification.activated.connect(self.chosen_knn_classification)
        self.page_4.combobox_y_knnClassification.activated.connect(self.chosen_knn_classification)
        self.stackedWidget.addWidget(self.page_4)
        # -----------------------------Page5--------------------
        self.page_5 = PageLogisticRegression(stl_btn, font)
        self.page_5.combobox_x_LogisticRegression.activated.connect(self.chosen_logistic_regression)
        self.page_5.comboBox_y_LogisticRegression.activated.connect(self.chosen_logistic_regression)
        self.stackedWidget.addWidget(self.page_5)

        # ----------------Page6-----------------------------------------
        self.page_6 = PageCrossValidation(stl_btn, font)
        self.page_6.combobox_x_CrossValidation.activated.connect(self.chosen_cross_validation)
        self.page_6.comboBox_y_CrossValidation.activated.connect(self.chosen_cross_validation)

        self.stackedWidget.addWidget(self.page_6)

        # --------------------------Page7----------------------------------
        self.page_7 = PageKCrossValidation(stl_btn, font)
        self.page_7.combobox_x_kCrossValidation.activated.connect(self.chosen_k_cross_validation)
        self.page_7.comboBox_y_kCrossValidation.activated.connect(self.chosen_k_cross_validation)
        self.stackedWidget.addWidget(self.page_7)

        # ---------------Page8--------------------------------------------
        self.page_8 = PagePolynomialRegression(stl_btn, font)
        self.page_8.comboBox_x_PolynomialRegression.activated.connect(self.chosen_poly_regression)
        self.page_8.comboBox_y_PolynomialRegression.activated.connect(self.chosen_poly_regression)
        self.stackedWidget.addWidget(self.page_8)
        # ----------------------------Page9-----------------------------------
        self.page_9 = PageCubicSpline(stl_btn, font)
        self.page_9.comboBox_x_CubicSpline.activated.connect(self.chosen_cub_spline)
        self.page_9.comboBox_y_CubicSpline.activated.connect(self.chosen_cub_spline)
        self.stackedWidget.addWidget(self.page_9)

        # -----------------------------Page10---------------------------------
        self.page_10 = PageNaturalCubicSpline(stl_btn, font)
        self.page_10.comboBox_x_NaturalCubicSpline.activated.connect(self.chosen_natural_cub)
        self.page_10.comboBox_y_NaturalCubicSpline.activated.connect(self.chosen_natural_cub)
        self.stackedWidget.addWidget(self.page_10)

        # ---------------Page11 Ridge--------------------------------------------
        self.page_11 = PageRidgeRegression(stl_btn, font)
        self.page_11.combobox_x_ridge.activated.connect(self.chosen_ridge)
        self.page_11.comboBox_y_ridge.activated.connect(self.chosen_ridge)
        self.stackedWidget.addWidget(self.page_11)

        # ---------------Page12 Lasso--------------------------------------------
        self.page_12 = PageLasso(stl_btn, font)
        self.page_12.combobox_x_lasso.activated.connect(self.chosen_lasso)
        self.page_12.comboBox_y_lasso.activated.connect(self.chosen_lasso)
        self.stackedWidget.addWidget(self.page_12)

        # ----------------Page 13 Regression tree-------------------------
        self.page_13 = PageRegressionTree(stl_btn, font)
        self.page_13.combobox_x_regression_tree.activated.connect(self.chosen_regression_tree)
        self.page_13.comboBox_y_regression_tree.activated.connect(self.chosen_regression_tree)
        self.stackedWidget.addWidget(self.page_13)

        # ----------------Page 14 Classification tree-------------------------
        self.page_14 = PageClassificationTree(stl_btn, font)
        self.page_14.combobox_x_cl_tree.activated.connect(self.chosen_cl_tree)
        self.page_14.comboBox_y_cl_tree.activated.connect(self.chosen_cl_tree)
        self.stackedWidget.addWidget(self.page_14)

        # -----------------------------Page 15 Linear Discriminant Analysis--------------------
        self.page_15 = PageLinearDiscriminant(stl_btn, font)
        self.page_15.combobox_x_LinearDiscriminant.activated.connect(self.chosen_lin_disc)
        self.page_15.comboBox_y_LinearDiscriminant.activated.connect(self.chosen_lin_disc)
        self.stackedWidget.addWidget(self.page_15)

        # -----------------------------Page 16 Quadratic Discriminant Analysis--------------------
        self.page_16 = PageQuadraticDiscriminant(stl_btn, font)
        self.page_16.combobox_x_QuadraticDiscriminant.activated.connect(self.chosen_quadratic_discriminant)
        self.page_16.comboBox_y_QuadraticDiscriminant.activated.connect(self.chosen_quadratic_discriminant)
        self.stackedWidget.addWidget(self.page_16)

        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        main_window.setCentralWidget(self.centralWidget)

        self.page_1.predict_btn.clicked.connect(self.predict_lin)
        self.page_2.btn_predict_multy_regression.clicked.connect(self.predict_multy_lin_regression)
        self.page_3.btn_predict_knnRegression.clicked.connect(self.predict_knn_regression)
        self.page_3.btn_find_neigh_knnRegression.clicked.connect(self.find_best_k_knn_regression)
        self.page_4.btn_predict_knnClassification.clicked.connect(self.predict_knn_classification)
        self.page_4.btn_find_best_k_knnClassification.clicked.connect(self.find_best_k_knn_classification)
        self.page_5.btn_predict_LogisticRegression.clicked.connect(self.predict_result_logistic_regression)
        self.page_6.btn_find_CrossValidation.clicked.connect(self.find_cross_validation)
        self.page_7.btn_find_kCrossValidation.clicked.connect(self.find_k_cross_validation)
        self.page_7.btn_find_best_kCrossValidation.clicked.connect(self.find_best_k_cross_validation)
        self.page_8.btn_find_PolynomialRegression.clicked.connect(self.find_poly_regression)
        self.page_9.btn_predict_CubicSpline.clicked.connect(self.predict_cub_spline)
        self.page_10.btn_predict_NaturalCubicSpline.clicked.connect(self.predict_natural_cub)
        self.page_11.btn_find_ridge.clicked.connect(self.predict_ridge)
        self.page_11.btn_find_best_alpha.clicked.connect(self.find_best_alpha)
        self.page_12.btn_find_lasso.clicked.connect(self.predict_lasso)
        self.page_12.btn_find_best_alpha_lasso.clicked.connect(self.find_best_alpha_lasso)
        self.page_13.btn_predict_regression_tree.clicked.connect(self.predict_regression_tree)
        self.page_14.btn_predict_cl_tree.clicked.connect(self.predict_cl_tree)
        self.page_15.btn_predict_LinearDiscriminant.clicked.connect(self.predict_result_lin_disc)
        self.page_16.btn_predict_QuadraticDiscriminant.clicked.connect(self.predict_result_quadratic_discriminant)
        # if self.generate_data_window:
        #     self.generate_data_window.normal_distribution.analise_btn.clicked.connect(self.normal_df)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Analytics"))
        self.Btn_home.setText(_translate("MainWindow", ""))
        self.btn_data.setText(_translate("MainWindow", "Дані"))
        self.data.btn_open.setText(_translate("MainWindow", "Відкрити файл"))
        self.page_1.x_label.setText(_translate("MainWindow", "Оберіть стовпець для X"))
        self.page_1.y_label.setText(_translate("MainWindow", "Оберіть стовпець для Y"))
        self.page_1.predict_btn.setText(_translate("MainWindow", "Передбачити"))
        self.page_1.label_predict_linear.setText(
            _translate("MainWindow", "Введіть координату точки x для передбачення y"))
        self.page_1.label_2.setText(_translate("MainWindow", "Результати"))
        self.page_1.equation.setText(_translate("MainWindow", ""))
        self.page_1.label_b0.setText(_translate("MainWindow", ""))
        self.page_1.label_b1.setText(_translate("MainWindow", ""))
        self.page_1.label_mse.setText(_translate("MainWindow", ""))
        self.page_1.label_r2.setText(_translate("MainWindow", ""))
        self.page_1.label_result.setText(_translate("MainWindow", ""))
        self.page_2.label_x_multy_regression.setText(_translate("MainWindow", "Оберіть стовпці для X"))
        self.page_2.label_y_multy_regression.setText(_translate("MainWindow", "Оберіть стовпець для Y"))
        self.page_2.label_predict_multy_regression.setText(
            _translate("MainWindow", "Введіть дані X (розділені ;) для передбачення y"))
        self.page_2.result_predict_multy.setText(_translate("MainWindow", ""))
        self.page_2.btn_predict_multy_regression.setText(_translate("MainWindow", "Передбачити"))
        self.page_2.result_multy_regression_text.setText(_translate("MainWindow", "Результати"))
        self.page_2.equation_multy_regression.setText(_translate("MainWindow", ""))
        self.page_2.b0_multy_regression.setText(_translate("MainWindow", ""))
        self.page_2.r2_multy_regression.setText(_translate("MainWindow", ""))
        self.page_2.label_chosen_multy.setText(_translate("MainWindow", ""))
        self.page_3.label_x_knn_regression.setText(_translate("MainWindow", "Оберіть стовпець для X"))
        self.page_3.label_chosen_x_knnRegression.setText(_translate("MainWindow", ""))
        self.page_3.label_y_knn_regression.setText(_translate("MainWindow", "Оберіть стовпець для Y"))
        self.page_3.label_k.setText(_translate("MainWindow", "k - кількість сусідів:"))
        self.page_3.label_data_predict_text.setText(_translate("MainWindow", "Дані для передбачення результату"))
        self.page_3.btn_predict_knnRegression.setText(_translate("MainWindow", "Передбачити"))
        self.page_3.label_r2_knnRegression.setText(_translate("MainWindow", ""))
        self.page_3.label_result_knnRegression.setText(_translate("MainWindow", ""))
        self.page_3.label_mae_knnRegression.setText(_translate("MainWindow", ""))
        self.page_3.label_mse_knnRegression.setText(_translate("MainWindow", ""))
        self.page_3.label_rmse_knnRegression.setText(_translate("MainWindow", ""))
        self.page_3.label_min_k.setText(_translate("MainWindow", "Мінімальна кількість сусідів"))
        self.page_3.label_max_k.setText(_translate("MainWindow", "Максимальна кількість сусідів"))
        self.page_3.btn_find_neigh_knnRegression.setText(_translate("MainWindow", "Знайти"))
        self.page_3.label_result_neigh.setText(_translate("MainWindow", ""))
        self.page_3.label_r2best_knnRegression.setText(_translate("MainWindow", ""))
        self.page_3.label_mae_best_knnRegression.setText(_translate("MainWindow", ""))
        self.page_3.label_mse_best_knnRegression.setText(_translate("MainWindow", ""))
        self.page_3.label_rmse_best_knnRegression.setText(_translate("MainWindow", ""))

        self.page_4.label_choose_x_knnClassification.setText(_translate("MainWindow", "Оберіть стовпці для X"))
        self.page_4.x_knnClassification.setText(_translate("MainWindow", ""))
        self.page_4.label_choose_y_knnClassification.setText(_translate("MainWindow", "Оберіть стовпець для Y"))
        self.page_4.label_num_clas.setText(_translate("MainWindow", "Кількість класів для розбиття"))
        self.page_4.range_clas.setText(_translate("MainWindow", ""))
        self.page_4.label_k_knnClassification.setText(_translate("MainWindow", "k - кількість сусідів "))
        self.page_4.label_data_knnClassification.setText(_translate("MainWindow", "Дані  для передбачення"))
        self.page_4.btn_predict_knnClassification.setText(_translate("MainWindow", "Передбачити"))
        self.page_4.label_res_knn.setText(_translate("MainWindow", ""))
        self.page_4.tabWidget.setTabText(self.page_4.tabWidget.indexOf(self.page_4.tab),
                                         _translate("MainWindow", "Передбачити"))
        self.page_4.label_min_k_knnClassification.setText(_translate("MainWindow", "Мінімальна кількість сусідів"))
        self.page_4.label_max_k_knnClassification.setText(_translate("MainWindow", "Максимальна кількість сусідів"))
        self.page_4.btn_find_best_k_knnClassification.setText(_translate("MainWindow", "Знайти"))
        self.page_4.label_best_k_knnClassification.setText(_translate("MainWindow", ""))
        self.page_4.label_best_result_knnClassification.setText(_translate("MainWindow", ""))
        self.page_4.tabWidget.setTabText(self.page_4.tabWidget.indexOf(self.page_4.tab_2),
                                         _translate("MainWindow", "Знайти найкраще значення k"))
        self.page_5.label_choose_x_LogisticRegression.setText(_translate("MainWindow", "Оберіть стовпці для X"))
        self.page_5.chosen_x_LogisticRegression.setText(_translate("MainWindow", ""))
        self.page_5.label_choose_y_LogisticRegression.setText(_translate("MainWindow", "Оберіть стовпець для Y"))
        self.page_5.label_data_predict_LogisticRegression.setText(_translate("MainWindow", "Дані для передбачення"))
        self.page_5.predict_LogisticRegression.setText(_translate("MainWindow", ""))
        self.page_5.btn_predict_LogisticRegression.setText(_translate("MainWindow", "Передбачити"))
        self.page_5.b0_LogisticRegression.setText(_translate("MainWindow", ""))
        self.page_5.coefficient_LogisticRegression.setText(_translate("MainWindow", ""))
        self.page_5.score_LogisticRegression.setText(_translate("MainWindow", ""))
        self.page_6.label_choose_x_CrossValidation.setText(_translate("MainWindow", "Оберіть стовпці для X"))
        self.page_6.chosen_x_CrossValidation.setText(_translate("MainWindow", ""))
        self.page_6.label_choose_y_CrossValidation.setText(_translate("MainWindow", "Оберіть стовпець для Y"))
        self.page_6.btn_find_CrossValidation.setText(_translate("MainWindow", "Знайти"))
        self.page_7.label_choose_x_kCrossValidation.setText(_translate("MainWindow", "Оберіть стовпці для X"))
        self.page_7.chosen_x_kCrossValidation.setText(_translate("MainWindow", ""))
        self.page_7.label_choose_y_kCrossValidation.setText(_translate("MainWindow", "Оберіть стовпець для Y"))
        self.page_7.label_num_k_kCrossValidation.setText(_translate("MainWindow", "Значення k"))
        self.page_7.btn_find_kCrossValidation.setText(_translate("MainWindow", "Знайти"))
        self.page_7.tabWidget_kCrossValidation.setTabText(
            self.page_7.tabWidget_kCrossValidation.indexOf(self.page_7.tab_3),
            _translate("MainWindow", "k-кратна перехресна перевірка"))
        self.page_7.label_mink_kCrossValidation.setText(_translate("MainWindow", "Мінімальне значення k"))
        self.page_7.label_max_k_kCrossValidation.setText(_translate("MainWindow", "Максимальне значення k"))
        self.page_7.label_method_kCrossValidation.setText(_translate("MainWindow", "Метод"))
        self.page_7.btn_find_best_kCrossValidation.setText(_translate("MainWindow", "Знайти"))
        self.page_7.tabWidget_kCrossValidation.setTabText(
            self.page_7.tabWidget_kCrossValidation.indexOf(self.page_7.tab_4),
            _translate("MainWindow", "Знайти найкраще значення k"))
        self.page_8.label_choose_x_PolynomialRegression.setText(_translate("MainWindow", "Оберіть стовпець для X"))
        self.page_8.label_choose_y_PolynomialRegression.setText(_translate("MainWindow", "Оберіть стовпець для Y"))
        self.page_8.label_degree.setText(_translate("MainWindow", "Степінь"))
        self.page_8.label_data_predict_PolynomialRegression.setText(_translate("MainWindow", "Дані для передбачення"))
        self.page_8.btn_find_PolynomialRegression.setText(_translate("MainWindow", "Знайти"))
        self.page_8.label_rmse_PolynomialRegression.setText(_translate("MainWindow", ""))
        self.page_9.label_choose_x_CubicSpline.setText(_translate("MainWindow", "Оберіть стовпець для X"))
        self.page_9.label_choose_y_CubicSpline.setText(_translate("MainWindow", "Оберіть стовпець для Y"))
        self.page_9.btn_predict_CubicSpline.setText(_translate("MainWindow", "Передбачити"))

        self.page_10.label_choose_x_NaturalCubicSpline.setText(_translate("MainWindow", "Оберіть стовпець для X"))
        self.page_10.label_choose_y_NaturalCubicSpline.setText(_translate("MainWindow", "Оберіть стовпець для Y"))
        self.page_10.btn_predict_NaturalCubicSpline.setText(_translate("MainWindow", "Передбачити"))
        self.page_10.label_rmse_NaturalCubicSpline.setText(_translate("MainWindow", ""))

        self.page_11.label_choose_x_ridge.setText(_translate("MainWindow", "Оберіть стовпець для X"))
        self.page_11.label_chosen_ridge.setText(_translate("MainWindow", ""))
        self.page_11.label_choose_y_ridge.setText(_translate("MainWindow", "Оберіть стовпець для Y"))
        self.page_11.label_alpha.setText(_translate("MainWindow", "a"))
        self.page_11.label_data_predict_ridge.setText(_translate("MainWindow", "Дані для передбачення"))
        self.page_11.btn_find_ridge.setText(_translate("MainWindow", "Знайти"))
        self.page_11.label_mse_ridge.setText(_translate("MainWindow", ""))
        self.page_11.tabWidget_ridge.setTabText(self.page_11.tabWidget_ridge.indexOf(self.page_11.tab_7),
                                                _translate("MainWindow", "Передбачити"))
        self.page_11.tabWidget_ridge.setTabText(self.page_11.tabWidget_ridge.indexOf(self.page_11.tab_8),
                                                _translate("MainWindow", "Знайти найкраще значення a"))
        self.page_11.label_min_alpha.setText(_translate("MainWindow", "Мінімальнe a"))
        self.page_11.label_max_alpha.setText(_translate("MainWindow", "Максимальнe a"))
        self.page_11.btn_find_best_alpha.setText(_translate("MainWindow", "Знайти"))
        self.page_11.label_best_alpha.setText(_translate("MainWindow", ""))
        self.page_11.label_best_result_alpha.setText(_translate("MainWindow", ""))

        self.page_12.label_choose_x_lasso.setText(_translate("MainWindow", "Оберіть стовпець для X"))
        self.page_12.label_chosen_lasso.setText(_translate("MainWindow", ""))
        self.page_12.label_choose_y_lasso.setText(_translate("MainWindow", "Оберіть стовпець для Y"))
        self.page_12.label_alpha_lasso.setText(_translate("MainWindow", "A"))
        self.page_12.label_data_predict_lasso.setText(_translate("MainWindow", "Дані для передбачення"))
        self.page_12.btn_find_lasso.setText(_translate("MainWindow", "Знайти"))
        self.page_12.label_mse_lasso.setText(_translate("MainWindow", ""))
        self.page_12.tabWidget_lasso.setTabText(self.page_12.tabWidget_lasso.indexOf(self.page_12.tab_9),
                                                _translate("MainWindow", "Передбачити"))
        self.page_12.tabWidget_lasso.setTabText(self.page_12.tabWidget_lasso.indexOf(self.page_12.tab_10),
                                                _translate("MainWindow", "Знайти найкраще значення a"))
        self.page_12.label_min_alpha_lasso.setText(_translate("MainWindow", "Мінімальнe a"))
        self.page_12.label_max_alpha_lasso.setText(_translate("MainWindow", "Максимальнe a"))
        self.page_12.btn_find_best_alpha_lasso.setText(_translate("MainWindow", "Знайти"))
        self.page_12.label_best_alpha_lasso.setText(_translate("MainWindow", ""))
        self.page_12.label_best_result_alpha_lasso.setText(_translate("MainWindow", ""))

        self.page_13.label_x_regression_tree.setText(_translate("MainWindow", "Оберіть стовпці для X"))
        self.page_13.label_y_regression_tree.setText(_translate("MainWindow", "Оберіть стовпець для Y"))
        self.page_13.label_predict_regression_tree.setText(
            _translate("MainWindow", "Введіть дані X (розділені ;) для передбачення y"))
        self.page_13.btn_predict_regression_tree.setText(_translate("MainWindow", "Передбачити"))
        self.page_13.result_regression_tree.setText(_translate("MainWindow", "Результати"))
        self.page_13.mse_regression_tree.setText(_translate("MainWindow", ""))
        self.page_13.label_regression_tree_depth.setText(
            _translate("MainWindow", "Введіть максимальну глибину дерева (наприклад, 10):"))
        self.page_13.label_regression_tree_split.setText(_translate("MainWindow",
                                                                    "Введіть мінімальну кількість зразків,"
                                                                    "необхідних для \n"
                                                                    "розділення внутрішньої вершини (наприклад, 2)"))
        self.page_13.label_regression_tree_leaf.setText(
            _translate("MainWindow", "Введіть мінімальну кількість зразків, необхідних для листка (наприклад, 1)"))
        self.page_13.label_best_parameters_regression_tree.setText(_translate("MainWindow", ""))

        self.page_14.label_x_cl_tree.setText(_translate("MainWindow", "Оберіть стовпці для X"))
        self.page_14.label_y_cl_tree.setText(_translate("MainWindow", "Оберіть стовпець для Y"))
        self.page_14.label_predict_cl_tree.setText(
            _translate("MainWindow", "Введіть дані X (розділені ;) для передбачення y"))
        self.page_14.btn_predict_cl_tree.setText(_translate("MainWindow", "Передбачити"))
        self.page_14.result_cl_tree_text.setText(_translate("MainWindow", "Результати"))
        self.page_14.report_cl_tree.setText(_translate("MainWindow", ""))
        self.page_14.label_cl_tree_depth.setText(
            _translate("MainWindow", "Введіть максимальну глибину дерева (наприклад, 10):"))
        self.page_14.label_cl_tree_split.setText(_translate("MainWindow",
                                                            "Введіть мінімальну кількість зразків, необхідних для \n "
                                                            "розділення внутрішньої вершини (наприклад, 2)"))
        self.page_14.label_cl_tree_leaf.setText(
            _translate("MainWindow", "Введіть мінімальну кількість зразків, необхідних для листка (наприклад, 1)"))
        self.page_14.label_best_parameters_cl_tree.setText(_translate("MainWindow", ""))

        self.page_15.label_choose_x_LinearDiscriminant.setText(_translate("MainWindow", "Оберіть стовпці для X"))
        self.page_15.chosen_x_LinearDiscriminant.setText(_translate("MainWindow", ""))
        self.page_15.label_choose_y_LinearDiscriminant.setText(_translate("MainWindow", "Оберіть стовпець для Y"))
        self.page_15.label_data_predict_LinearDiscriminant.setText(_translate("MainWindow", "Дані для передбачення"))
        self.page_15.predict_LinearDiscriminant.setText(_translate("MainWindow", ""))
        self.page_15.btn_predict_LinearDiscriminant.setText(_translate("MainWindow", "Передбачити"))
        self.page_15.report_LinearDiscriminant.setText(_translate("MainWindow", ""))
        self.page_15.accuracy_LinearDiscriminant.setText(_translate("MainWindow", ""))

        self.page_16.label_choose_x_QuadraticDiscriminant.setText(_translate("MainWindow", "Оберіть стовпці для X"))
        self.page_16.chosen_x_QuadraticDiscriminant.setText(_translate("MainWindow", ""))
        self.page_16.label_choose_y_QuadraticDiscriminant.setText(_translate("MainWindow", "Оберіть стовпець для Y"))
        self.page_16.label_data_predict_QuadraticDiscriminant.setText(_translate("MainWindow", "Дані для передбачення"))
        self.page_16.predict_QuadraticDiscriminant.setText(_translate("MainWindow", ""))
        self.page_16.btn_predict_QuadraticDiscriminant.setText(_translate("MainWindow", "Передбачити"))
        self.page_16.report_QuadraticDiscriminant.setText(_translate("MainWindow", ""))
        self.page_16.accuracy_QuadraticDiscriminant.setText(_translate("MainWindow", ""))

        self.page_3.tabWidget_2.setTabText(self.page_3.tabWidget_2.indexOf(self.page_3.tab_6),
                                           _translate("MainWindow", "Знайти найкраще значення k"))
        self.page_3.tabWidget_2.setTabText(self.page_3.tabWidget_2.indexOf(self.page_3.tab_5),
                                           _translate("MainWindow", "регресія K- найближчих сусідів "))
        self.data.btn_generate.setText(_translate("MainWindow", "Згенерувати дані"))

    def clicker(self):
        f_name = QFileDialog.getOpenFileName()
        if f_name != ('', ''):
            # self.page_1.canvas1.axes.cla()
            # self.page_1.canvas1.draw()
            # self.page_3.canvas_knnRegression.axes.cla()
            # self.page_3.canvas_knnRegression.draw()
            # self.page_4.canvas_knnClassification.axes.cla()
            # self.page_4.canvas_knnClassification.draw()
            # self.page_4.canvas_knnClassification_best.axes.cla()
            # self.page_4.canvas_knnClassification_best.draw()
            # self.page_4.canvas_knnClassification_best_matrix.axes.cla()
            # self.page_4.canvas_knnClassification_best_matrix.draw()
            # self.page_5.canvas_LogisticRegression.axes.cla()
            # self.page_5.canvas_LogisticRegression.figure.suptitle("")
            # self.page_5.canvas_LogisticRegression.draw()
            # self.page_5.canvas_logic_matrix.axes.cla()
            # self.page_5.canvas_logic_matrix.draw()
            # self.page_7.canvas_best_kCrossValidation.axes.cla()
            # self.page_7.canvas_best_kCrossValidation.draw()
            # self.page_8.canvas_PolynomialRegression.axes.cla()
            # self.page_8.canvas_PolynomialRegression.draw()
            # self.page_9.canvas_CubicSpline.axes.cla()
            # self.page_9.canvas_CubicSpline.draw()
            # self.page_10.canvas_NaturalCubicSpline.axes.cla()
            # self.page_10.canvas_NaturalCubicSpline.draw()
            # self.page_11.canvas_ridge.axes.cla()
            # self.page_11.canvas_ridge.draw()
            # self.page_11.canvas_ridge_best.axes.cla()
            # self.page_11.canvas_ridge_best.draw()
            # self.page_11.canvas_ridge_best_mse.axes.cla()
            # self.page_11.canvas_ridge_best_mse.draw()
            # self.page_12.canvas_lasso.axes.cla()
            # self.page_12.canvas_lasso.draw()
            # self.page_12.canvas_lasso_best.axes.cla()
            # self.page_12.canvas_lasso_best.draw()
            # self.page_12.canvas_lasso_best_mse.axes.cla()
            # self.page_12.canvas_lasso_best_mse.draw()
            # self.page_13.canvas_regression_tree.axes.cla()
            # self.page_13.canvas_regression_tree.draw()
            # self.page_14.canvas_cl_tree.axes.cla()
            # self.page_14.canvas_cl_tree.draw()
            # self.page_14.canvas_cl_tree_matrix.axes.cla()
            # self.page_14.canvas_cl_tree_matrix.draw()
            # self.page_15.canvas_LinearDiscriminant.axes.cla()
            # self.page_15.canvas_LinearDiscriminant.draw()
            # self.page_15.canvas_LinearDiscriminant_matrix.axes.cla()
            # self.page_15.canvas_LinearDiscriminant_matrix.draw()
            # self.page_16.canvas_QuadraticDiscriminant.axes.cla()
            # self.page_16.canvas_QuadraticDiscriminant.draw()
            # self.page_1.comboBox_x.clear()
            # self.page_1.comboBox_y.clear()
            # self.page_2.comboBox_y_multy_regression.clear()
            # self.page_3.comboBox_Y_knnRegression.clear()
            # self.page_4.combobox_y_knnClassification.clear()
            # self.page_5.comboBox_y_LogisticRegression.clear()
            # self.page_6.comboBox_y_CrossValidation.clear()
            # self.page_7.comboBox_y_kCrossValidation.clear()
            # self.page_8.comboBox_y_PolynomialRegression.clear()
            # self.page_8.comboBox_x_PolynomialRegression.clear()
            # self.page_9.comboBox_x_CubicSpline.clear()
            # self.page_9.comboBox_y_CubicSpline.clear()
            # self.page_10.comboBox_x_NaturalCubicSpline.clear()
            # self.page_10.comboBox_y_NaturalCubicSpline.clear()
            # self.page_2.combobox_x_multy_regression.clear()
            # self.page_3.combobox_x_knnRegression.clear()
            # self.page_4.combobox_x_knnClassification.clear()
            # self.page_5.combobox_x_LogisticRegression.clear()
            # self.page_6.combobox_x_CrossValidation.clear()
            # self.page_7.combobox_x_kCrossValidation.clear()
            # self.page_11.combobox_x_ridge.clear()
            # self.page_11.comboBox_y_ridge.clear()
            # self.page_12.combobox_x_lasso.clear()
            # self.page_12.comboBox_y_lasso.clear()
            # self.page_13.combobox_x_regression_tree.clear()
            # self.page_13.comboBox_y_regression_tree.clear()
            # self.page_14.combobox_x_cl_tree.clear()
            # self.page_14.comboBox_y_cl_tree.clear()
            # self.page_15.combobox_x_LinearDiscriminant.clear()
            # self.page_15.comboBox_y_LinearDiscriminant.clear()
            # self.page_16.combobox_x_QuadraticDiscriminant.clear()
            # self.page_16.comboBox_y_QuadraticDiscriminant.clear()
            # self.page_1.equation.setText("")
            # self.page_1.label_b0.setText("")
            # self.page_1.label_b1.setText("")
            # self.page_1.label_mse.setText("")
            # self.page_1.label_r2.setText("")
            # self.page_1.label_result.setText("")
            # self.page_1.lin_reg_predict.clear()
            # self.page_2.result_predict_multy.setText("")
            # self.page_2.equation_multy_regression.setText("")
            # self.page_2.b0_multy_regression.setText("")
            # self.page_2.r2_multy_regression.setText("")
            # self.page_2.label_chosen_multy.setText("")
            # self.page_2.lineEdit_x_multy_regression.clear()
            # self.page_3.label_chosen_x_knnRegression.setText("")
            # self.page_3.label_r2_knnRegression.setText("")
            # self.page_3.label_result_knnRegression.setText("")
            # self.page_3.label_mae_knnRegression.setText("")
            # self.page_3.label_mse_knnRegression.setText("")
            # self.page_3.label_rmse_knnRegression.setText("")
            # self.page_3.label_result_neigh.setText("")
            # self.page_3.label_r2best_knnRegression.setText("")
            # self.page_3.label_mae_best_knnRegression.setText("")
            # self.page_3.label_mse_best_knnRegression.setText("")
            # self.page_3.label_rmse_best_knnRegression.setText("")
            # self.page_3.lineEdit_num_neigh.clear()
            # self.page_3.lineEdit_data_predict.clear()
            # self.page_3.lineEdit_min_neigh.clear()
            # self.page_3.lineEdit_max_neigh.clear()
            # self.page_4.x_knnClassification.setText("")
            # self.page_4.range_clas.setText("")
            # self.page_4.label_res_knn.setText("")
            # self.page_4.label_best_k_knnClassification.setText("")
            # self.page_4.label_best_result_knnClassification.setText("")
            # self.page_4.result_predict_knnClassification.setText("")
            # self.page_4.lineEdit_num_class_knnClassification.clear()
            # self.page_4.lineEdit_k_knnClassification.clear()
            # self.page_4.lineEdit_data_knnClassification.clear()
            # self.page_4.lineEdit_min_k_knnClassification.clear()
            # self.page_4.lineEdit_max_k_knnClassification.clear()
            # self.page_5.chosen_x_LogisticRegression.setText("")
            # self.page_5.predict_LogisticRegression.setText("")
            # self.page_5.b0_LogisticRegression.setText("")
            # self.page_5.coefficient_LogisticRegression.setText("")
            # self.page_5.score_LogisticRegression.setText("")
            # self.page_5.lineEdit_data_LogisticRegression.clear()
            # self.page_6.chosen_x_CrossValidation.setText("")
            # self.page_7.chosen_x_kCrossValidation.setText("")
            # self.page_7.lineEdit_mink_kCrossValidation.clear()
            # self.page_7.lineEdit_num_k_kCrossValidation.clear()
            # self.page_7.lineEdit_max_k_kCrossValidation.clear()
            # self.page_8.label_rmse_PolynomialRegression.setText("")
            # self.page_8.label_result_PolynomialRegression.setText("")
            # self.page_8.lineEdit_degree.clear()
            # self.page_8.lineEdit_data_PolynomialRegression.clear()
            # self.page_9.label_rmse_CubicSpline.setText("")
            # self.page_10.label_rmse_NaturalCubicSpline.setText("")
            # self.page_11.label_chosen_ridge.setText("")
            # self.page_11.label_result_ridge.setText("")
            # self.page_11.label_mse_ridge.setText("")
            # self.page_11.label_best_alpha.setText("")
            # self.page_11.label_best_result_alpha.setText("")
            # self.page_11.lineEdit_alpha.clear()
            # self.page_11.lineEdit_data_ridge.clear()
            # self.page_11.lineEdit_min_alpha.clear()
            # self.page_11.lineEdit_max_alpha.clear()
            # self.page_12.label_chosen_lasso.setText("")
            # self.page_12.label_mse_lasso.setText("")
            # self.page_12.label_best_alpha_lasso.setText("")
            # self.page_12.label_best_result_alpha_lasso.setText("")
            # self.page_12.label_result_lasso.setText("")
            # self.page_12.lineEdit_alpha_lasso.clear()
            # self.page_12.lineEdit_data_lasso.clear()
            # self.page_12.lineEdit_min_alpha_lasso.clear()
            # self.page_12.lineEdit_max_alpha_lasso.clear()
            # self.page_13.mse_regression_tree.setText("")
            # self.page_13.label_best_parameters_regression_tree.setText("")
            # self.page_13.lineEdit_depth_regression_tree.clear()
            # self.page_13.lineEdit_regression_tree_split.clear()
            # self.page_13.lineEdit_regression_tree_leaf.clear()
            # self.page_13.lineEdit_x_regression_tree.clear()
            # self.page_14.report_cl_tree.setText("")
            # self.page_14.label_best_parameters_cl_tree.setText("")
            # self.page_14.result_predict_cl_tree.setText("")
            # self.page_14.lineEdit_depth_cl_tree.clear()
            # self.page_14.lineEdit_cl_tree_split.clear()
            # self.page_14.lineEdit_cl_tree_leaf.clear()
            # self.page_14.lineEdit_x_cl_tree.clear()
            # self.page_15.chosen_x_LinearDiscriminant.setText("")
            # self.page_15.predict_LinearDiscriminant.setText("")
            # self.page_15.report_LinearDiscriminant.setText("")
            # self.page_15.accuracy_LinearDiscriminant.setText("")
            # self.page_15.lineEdit_data_LinearDiscriminant.clear()
            # self.page_16.chosen_x_QuadraticDiscriminant.setText("")
            # self.page_16.predict_QuadraticDiscriminant.setText("")
            # self.page_16.report_QuadraticDiscriminant.setText("")
            # self.page_16.accuracy_QuadraticDiscriminant.setText("")
            # self.page_16.lineEdit_data_QuadraticDiscriminant.clear()

            data = pd.read_csv(str(f_name[0]))
            TableWidget().set(self.data.tableWidget, data)
            self._data = data

            self.clear_data()
            # self.page_1.comboBox_x.addItems(self._data.columns.values.tolist())
            # self.page_1.comboBox_y.addItems(self._data.columns.values.tolist())
            # self.page_2.comboBox_y_multy_regression.addItems(self._data.columns.values.tolist())
            # self.page_3.comboBox_Y_knnRegression.addItems(self._data.columns.values.tolist())
            # self.page_4.combobox_y_knnClassification.addItems(self._data.columns.values.tolist())
            # self.page_5.comboBox_y_LogisticRegression.addItems(self._data.columns.values.tolist())
            # self.page_6.comboBox_y_CrossValidation.addItems(self._data.columns.values.tolist())
            # self.page_7.comboBox_y_kCrossValidation.addItems(self._data.columns.values.tolist())
            # self.page_8.comboBox_y_PolynomialRegression.addItems(self._data.columns.values.tolist())
            # self.page_8.comboBox_x_PolynomialRegression.addItems(self._data.columns.values.tolist())
            # self.page_9.comboBox_x_CubicSpline.addItems(self._data.columns.values.tolist())
            # self.page_9.comboBox_y_CubicSpline.addItems(self._data.columns.values.tolist())
            # self.page_10.comboBox_x_NaturalCubicSpline.addItems(self._data.columns.values.tolist())
            # self.page_10.comboBox_y_NaturalCubicSpline.addItems(self._data.columns.values.tolist())
            # self.page_11.comboBox_y_ridge.addItems(self._data.columns.values.tolist())
            # self.page_12.comboBox_y_lasso.addItems(self._data.columns.values.tolist())
            # self.page_13.comboBox_y_regression_tree.addItems(self._data.columns.values.tolist())
            # self.page_14.comboBox_y_cl_tree.addItems(self._data.columns.values.tolist())
            # self.page_15.comboBox_y_LinearDiscriminant.addItems(self._data.columns.values.tolist())
            # self.page_16.comboBox_y_QuadraticDiscriminant.addItems(self._data.columns.values.tolist())
            #
            # for i in range(len(self._data.columns.values.tolist())):
            #     self.page_2.combobox_x_multy_regression.addItem(self._data.columns.values.tolist()[i])
            #     self.page_3.combobox_x_knnRegression.addItem(self._data.columns.values.tolist()[i])
            #     self.page_4.combobox_x_knnClassification.addItem(self._data.columns.values.tolist()[i])
            #     self.page_5.combobox_x_LogisticRegression.addItem(self._data.columns.values.tolist()[i])
            #     self.page_6.combobox_x_CrossValidation.addItem(self._data.columns.values.tolist()[i])
            #     self.page_7.combobox_x_kCrossValidation.addItem(self._data.columns.values.tolist()[i])
            #     self.page_11.combobox_x_ridge.addItem(self._data.columns.values.tolist()[i])
            #     self.page_12.combobox_x_lasso.addItem(self._data.columns.values.tolist()[i])
            #     self.page_13.combobox_x_regression_tree.addItem(self._data.columns.values.tolist()[i])
            #     self.page_14.combobox_x_cl_tree.addItem(self._data.columns.values.tolist()[i])
            #     self.page_15.combobox_x_LinearDiscriminant.addItem(self._data.columns.values.tolist()[i])
            #     self.page_16.combobox_x_QuadraticDiscriminant.addItem(self._data.columns.values.tolist()[i])
            #     item = self.page_11.combobox_x_ridge.model().item(i, 0)
            #     item.setCheckState(Qt.Unchecked)
            #
            #     item_quadratic_discriminant = self.page_16.combobox_x_QuadraticDiscriminant.model().item(i, 0)
            #     item_quadratic_discriminant.setCheckState(Qt.Unchecked)
            #
            #     item_linear_discriminant = self.page_15.combobox_x_LinearDiscriminant.model().item(i, 0)
            #     item_linear_discriminant.setCheckState(Qt.Unchecked)
            #
            #     item_regression_tree = self.page_13.combobox_x_regression_tree.model().item(i, 0)
            #     item_regression_tree.setCheckState(Qt.Unchecked)
            #
            #     item_cl_tree = self.page_14.combobox_x_cl_tree.model().item(i, 0)
            #     item_cl_tree.setCheckState(Qt.Unchecked)
            #
            #     item_lasso = self.page_12.combobox_x_lasso.model().item(i, 0)
            #     item_lasso.setCheckState(Qt.Unchecked)
            #
            #     item_knn = self.page_3.combobox_x_knnRegression.model().item(i, 0)
            #     item_knn.setCheckState(Qt.Unchecked)
            #
            #     item_knn_classification = self.page_4.combobox_x_knnClassification.model().item(i, 0)
            #     item_knn_classification.setCheckState(Qt.Unchecked)
            #     item_logistic_regression = self.page_5.combobox_x_LogisticRegression.model().item(i, 0)
            #     item_logistic_regression.setCheckState(Qt.Unchecked)
            #     item_cross_validation = self.page_6.combobox_x_CrossValidation.model().item(i, 0)
            #     item_cross_validation.setCheckState(Qt.Unchecked)
            #     item_k_cross_validation = self.page_7.combobox_x_kCrossValidation.model().item(i, 0)
            #     item_k_cross_validation.setCheckState(Qt.Unchecked)

    def clear_data(self):
        self.page_1.canvas1.axes.cla()
        self.page_1.canvas1.draw()
        self.page_3.canvas_knnRegression.axes.cla()
        self.page_3.canvas_knnRegression.draw()
        self.page_4.canvas_knnClassification.axes.cla()
        self.page_4.canvas_knnClassification.draw()
        self.page_4.canvas_knnClassification_best.axes.cla()
        self.page_4.canvas_knnClassification_best.draw()
        self.page_4.canvas_knnClassification_best_matrix.axes.cla()
        self.page_4.canvas_knnClassification_best_matrix.draw()
        self.page_5.canvas_LogisticRegression.axes.cla()
        self.page_5.canvas_LogisticRegression.figure.suptitle("")
        self.page_5.canvas_LogisticRegression.draw()
        self.page_5.canvas_logic_matrix.axes.cla()
        self.page_5.canvas_logic_matrix.draw()
        self.page_7.canvas_best_kCrossValidation.axes.cla()
        self.page_7.canvas_best_kCrossValidation.draw()
        self.page_8.canvas_PolynomialRegression.axes.cla()
        self.page_8.canvas_PolynomialRegression.draw()
        self.page_9.canvas_CubicSpline.axes.cla()
        self.page_9.canvas_CubicSpline.draw()
        self.page_10.canvas_NaturalCubicSpline.axes.cla()
        self.page_10.canvas_NaturalCubicSpline.draw()
        self.page_11.canvas_ridge.axes.cla()
        self.page_11.canvas_ridge.draw()
        self.page_11.canvas_ridge_best.axes.cla()
        self.page_11.canvas_ridge_best.draw()
        self.page_11.canvas_ridge_best_mse.axes.cla()
        self.page_11.canvas_ridge_best_mse.draw()
        self.page_12.canvas_lasso.axes.cla()
        self.page_12.canvas_lasso.draw()
        self.page_12.canvas_lasso_best.axes.cla()
        self.page_12.canvas_lasso_best.draw()
        self.page_12.canvas_lasso_best_mse.axes.cla()
        self.page_12.canvas_lasso_best_mse.draw()
        self.page_13.canvas_regression_tree.axes.cla()
        self.page_13.canvas_regression_tree.draw()
        self.page_14.canvas_cl_tree.axes.cla()
        self.page_14.canvas_cl_tree.draw()
        self.page_14.canvas_cl_tree_matrix.axes.cla()
        self.page_14.canvas_cl_tree_matrix.draw()
        self.page_15.canvas_LinearDiscriminant.axes.cla()
        self.page_15.canvas_LinearDiscriminant.draw()
        self.page_15.canvas_LinearDiscriminant_matrix.axes.cla()
        self.page_15.canvas_LinearDiscriminant_matrix.draw()
        self.page_16.canvas_QuadraticDiscriminant.axes.cla()
        self.page_16.canvas_QuadraticDiscriminant.draw()
        self.page_1.comboBox_x.clear()
        self.page_1.comboBox_y.clear()
        self.page_2.comboBox_y_multy_regression.clear()
        self.page_3.comboBox_Y_knnRegression.clear()
        self.page_4.combobox_y_knnClassification.clear()
        self.page_5.comboBox_y_LogisticRegression.clear()
        self.page_6.comboBox_y_CrossValidation.clear()
        self.page_7.comboBox_y_kCrossValidation.clear()
        self.page_8.comboBox_y_PolynomialRegression.clear()
        self.page_8.comboBox_x_PolynomialRegression.clear()
        self.page_9.comboBox_x_CubicSpline.clear()
        self.page_9.comboBox_y_CubicSpline.clear()
        self.page_10.comboBox_x_NaturalCubicSpline.clear()
        self.page_10.comboBox_y_NaturalCubicSpline.clear()
        self.page_2.combobox_x_multy_regression.clear()
        self.page_3.combobox_x_knnRegression.clear()
        self.page_4.combobox_x_knnClassification.clear()
        self.page_5.combobox_x_LogisticRegression.clear()
        self.page_6.combobox_x_CrossValidation.clear()
        self.page_7.combobox_x_kCrossValidation.clear()
        self.page_11.combobox_x_ridge.clear()
        self.page_11.comboBox_y_ridge.clear()
        self.page_12.combobox_x_lasso.clear()
        self.page_12.comboBox_y_lasso.clear()
        self.page_13.combobox_x_regression_tree.clear()
        self.page_13.comboBox_y_regression_tree.clear()
        self.page_14.combobox_x_cl_tree.clear()
        self.page_14.comboBox_y_cl_tree.clear()
        self.page_15.combobox_x_LinearDiscriminant.clear()
        self.page_15.comboBox_y_LinearDiscriminant.clear()
        self.page_16.combobox_x_QuadraticDiscriminant.clear()
        self.page_16.comboBox_y_QuadraticDiscriminant.clear()
        self.page_1.equation.setText("")
        self.page_1.label_b0.setText("")
        self.page_1.label_b1.setText("")
        self.page_1.label_mse.setText("")
        self.page_1.label_r2.setText("")
        self.page_1.label_result.setText("")
        self.page_1.lin_reg_predict.clear()
        self.page_2.result_predict_multy.setText("")
        self.page_2.equation_multy_regression.setText("")
        self.page_2.b0_multy_regression.setText("")
        self.page_2.r2_multy_regression.setText("")
        self.page_2.label_chosen_multy.setText("")
        self.page_2.lineEdit_x_multy_regression.clear()
        self.page_3.label_chosen_x_knnRegression.setText("")
        self.page_3.label_r2_knnRegression.setText("")
        self.page_3.label_result_knnRegression.setText("")
        self.page_3.label_mae_knnRegression.setText("")
        self.page_3.label_mse_knnRegression.setText("")
        self.page_3.label_rmse_knnRegression.setText("")
        self.page_3.label_result_neigh.setText("")
        self.page_3.label_r2best_knnRegression.setText("")
        self.page_3.label_mae_best_knnRegression.setText("")
        self.page_3.label_mse_best_knnRegression.setText("")
        self.page_3.label_rmse_best_knnRegression.setText("")
        self.page_3.lineEdit_num_neigh.clear()
        self.page_3.lineEdit_data_predict.clear()
        self.page_3.lineEdit_min_neigh.clear()
        self.page_3.lineEdit_max_neigh.clear()
        self.page_4.x_knnClassification.setText("")
        self.page_4.range_clas.setText("")
        self.page_4.label_res_knn.setText("")
        self.page_4.label_best_k_knnClassification.setText("")
        self.page_4.label_best_result_knnClassification.setText("")
        self.page_4.result_predict_knnClassification.setText("")
        self.page_4.lineEdit_num_class_knnClassification.clear()
        self.page_4.lineEdit_k_knnClassification.clear()
        self.page_4.lineEdit_data_knnClassification.clear()
        self.page_4.lineEdit_min_k_knnClassification.clear()
        self.page_4.lineEdit_max_k_knnClassification.clear()
        self.page_5.chosen_x_LogisticRegression.setText("")
        self.page_5.predict_LogisticRegression.setText("")
        self.page_5.b0_LogisticRegression.setText("")
        self.page_5.coefficient_LogisticRegression.setText("")
        self.page_5.score_LogisticRegression.setText("")
        self.page_5.lineEdit_data_LogisticRegression.clear()
        self.page_6.chosen_x_CrossValidation.setText("")
        self.page_7.chosen_x_kCrossValidation.setText("")
        self.page_7.lineEdit_mink_kCrossValidation.clear()
        self.page_7.lineEdit_num_k_kCrossValidation.clear()
        self.page_7.lineEdit_max_k_kCrossValidation.clear()
        self.page_8.label_rmse_PolynomialRegression.setText("")
        self.page_8.label_result_PolynomialRegression.setText("")
        self.page_8.lineEdit_degree.clear()
        self.page_8.lineEdit_data_PolynomialRegression.clear()
        self.page_9.label_rmse_CubicSpline.setText("")
        self.page_10.label_rmse_NaturalCubicSpline.setText("")
        self.page_11.label_chosen_ridge.setText("")
        self.page_11.label_result_ridge.setText("")
        self.page_11.label_mse_ridge.setText("")
        self.page_11.label_best_alpha.setText("")
        self.page_11.label_best_result_alpha.setText("")
        self.page_11.lineEdit_alpha.clear()
        self.page_11.lineEdit_data_ridge.clear()
        self.page_11.lineEdit_min_alpha.clear()
        self.page_11.lineEdit_max_alpha.clear()
        self.page_12.label_chosen_lasso.setText("")
        self.page_12.label_mse_lasso.setText("")
        self.page_12.label_best_alpha_lasso.setText("")
        self.page_12.label_best_result_alpha_lasso.setText("")
        self.page_12.label_result_lasso.setText("")
        self.page_12.lineEdit_alpha_lasso.clear()
        self.page_12.lineEdit_data_lasso.clear()
        self.page_12.lineEdit_min_alpha_lasso.clear()
        self.page_12.lineEdit_max_alpha_lasso.clear()
        self.page_13.mse_regression_tree.setText("")
        self.page_13.label_best_parameters_regression_tree.setText("")
        self.page_13.lineEdit_depth_regression_tree.clear()
        self.page_13.lineEdit_regression_tree_split.clear()
        self.page_13.lineEdit_regression_tree_leaf.clear()
        self.page_13.lineEdit_x_regression_tree.clear()
        self.page_14.report_cl_tree.setText("")
        self.page_14.label_best_parameters_cl_tree.setText("")
        self.page_14.result_predict_cl_tree.setText("")
        self.page_14.lineEdit_depth_cl_tree.clear()
        self.page_14.lineEdit_cl_tree_split.clear()
        self.page_14.lineEdit_cl_tree_leaf.clear()
        self.page_14.lineEdit_x_cl_tree.clear()
        self.page_15.chosen_x_LinearDiscriminant.setText("")
        self.page_15.predict_LinearDiscriminant.setText("")
        self.page_15.report_LinearDiscriminant.setText("")
        self.page_15.accuracy_LinearDiscriminant.setText("")
        self.page_15.lineEdit_data_LinearDiscriminant.clear()
        self.page_16.chosen_x_QuadraticDiscriminant.setText("")
        self.page_16.predict_QuadraticDiscriminant.setText("")
        self.page_16.report_QuadraticDiscriminant.setText("")
        self.page_16.accuracy_QuadraticDiscriminant.setText("")
        self.page_16.lineEdit_data_QuadraticDiscriminant.clear()

        self.page_1.comboBox_x.addItems(self._data.columns.values.tolist())
        self.page_1.comboBox_y.addItems(self._data.columns.values.tolist())
        self.page_2.comboBox_y_multy_regression.addItems(self._data.columns.values.tolist())
        self.page_3.comboBox_Y_knnRegression.addItems(self._data.columns.values.tolist())
        self.page_4.combobox_y_knnClassification.addItems(self._data.columns.values.tolist())
        self.page_5.comboBox_y_LogisticRegression.addItems(self._data.columns.values.tolist())
        self.page_6.comboBox_y_CrossValidation.addItems(self._data.columns.values.tolist())
        self.page_7.comboBox_y_kCrossValidation.addItems(self._data.columns.values.tolist())
        self.page_8.comboBox_y_PolynomialRegression.addItems(self._data.columns.values.tolist())
        self.page_8.comboBox_x_PolynomialRegression.addItems(self._data.columns.values.tolist())
        self.page_9.comboBox_x_CubicSpline.addItems(self._data.columns.values.tolist())
        self.page_9.comboBox_y_CubicSpline.addItems(self._data.columns.values.tolist())
        self.page_10.comboBox_x_NaturalCubicSpline.addItems(self._data.columns.values.tolist())
        self.page_10.comboBox_y_NaturalCubicSpline.addItems(self._data.columns.values.tolist())
        self.page_11.comboBox_y_ridge.addItems(self._data.columns.values.tolist())
        self.page_12.comboBox_y_lasso.addItems(self._data.columns.values.tolist())
        self.page_13.comboBox_y_regression_tree.addItems(self._data.columns.values.tolist())
        self.page_14.comboBox_y_cl_tree.addItems(self._data.columns.values.tolist())
        self.page_15.comboBox_y_LinearDiscriminant.addItems(self._data.columns.values.tolist())
        self.page_16.comboBox_y_QuadraticDiscriminant.addItems(self._data.columns.values.tolist())

        for i in range(len(self._data.columns.values.tolist())):
            self.page_2.combobox_x_multy_regression.addItem(self._data.columns.values.tolist()[i])
            self.page_3.combobox_x_knnRegression.addItem(self._data.columns.values.tolist()[i])
            self.page_4.combobox_x_knnClassification.addItem(self._data.columns.values.tolist()[i])
            self.page_5.combobox_x_LogisticRegression.addItem(self._data.columns.values.tolist()[i])
            self.page_6.combobox_x_CrossValidation.addItem(self._data.columns.values.tolist()[i])
            self.page_7.combobox_x_kCrossValidation.addItem(self._data.columns.values.tolist()[i])
            self.page_11.combobox_x_ridge.addItem(self._data.columns.values.tolist()[i])
            self.page_12.combobox_x_lasso.addItem(self._data.columns.values.tolist()[i])
            self.page_13.combobox_x_regression_tree.addItem(self._data.columns.values.tolist()[i])
            self.page_14.combobox_x_cl_tree.addItem(self._data.columns.values.tolist()[i])
            self.page_15.combobox_x_LinearDiscriminant.addItem(self._data.columns.values.tolist()[i])
            self.page_16.combobox_x_QuadraticDiscriminant.addItem(self._data.columns.values.tolist()[i])
            item = self.page_11.combobox_x_ridge.model().item(i, 0)
            item.setCheckState(Qt.Unchecked)

            item_quadratic_discriminant = self.page_16.combobox_x_QuadraticDiscriminant.model().item(i, 0)
            item_quadratic_discriminant.setCheckState(Qt.Unchecked)

            item_linear_discriminant = self.page_15.combobox_x_LinearDiscriminant.model().item(i, 0)
            item_linear_discriminant.setCheckState(Qt.Unchecked)

            item_regression_tree = self.page_13.combobox_x_regression_tree.model().item(i, 0)
            item_regression_tree.setCheckState(Qt.Unchecked)

            item_cl_tree = self.page_14.combobox_x_cl_tree.model().item(i, 0)
            item_cl_tree.setCheckState(Qt.Unchecked)

            item_lasso = self.page_12.combobox_x_lasso.model().item(i, 0)
            item_lasso.setCheckState(Qt.Unchecked)

            item_knn = self.page_3.combobox_x_knnRegression.model().item(i, 0)
            item_knn.setCheckState(Qt.Unchecked)

            item_knn_classification = self.page_4.combobox_x_knnClassification.model().item(i, 0)
            item_knn_classification.setCheckState(Qt.Unchecked)
            item_logistic_regression = self.page_5.combobox_x_LogisticRegression.model().item(i, 0)
            item_logistic_regression.setCheckState(Qt.Unchecked)
            item_cross_validation = self.page_6.combobox_x_CrossValidation.model().item(i, 0)
            item_cross_validation.setCheckState(Qt.Unchecked)
            item_k_cross_validation = self.page_7.combobox_x_kCrossValidation.model().item(i, 0)
            item_k_cross_validation.setCheckState(Qt.Unchecked)

    def chosen(self):
        if self.page_1.comboBox_x.currentIndexChanged:
            self._X.clear()
            self._X.append(self.page_1.comboBox_x.currentText())
        if self.page_1.comboBox_y.currentIndexChanged:
            self._y = self.page_1.comboBox_y.currentText()
        regression = LinearRegression(self._data[self._X[0]], self._data[self._y])
        regression.plot(self.page_1.canvas1)
        self.page_1.equation.setText(f"Рівняння: y={regression.b1_value()}*x+{regression.b0_value()}")
        self.page_1.label_mse.setText(f"MSE= {regression.mse_value()}")
        self.page_1.label_r2.setText(f"R^2= {regression.r2_value()}")
        self.page_1.label_b0.setText(f"b0= {regression.b0_value()}")
        self.page_1.label_b1.setText(f"b1= {regression.b1_value()}")

    def predict_lin(self):
        start_time = time.time()
        regression1 = LinearRegression(self._data[self._X[0]], self._data[self._y])
        try:
            self.page_1.label_result.setStyleSheet("background-color: rgb(255, 255, 255);")
            ar = np.array([[float(self.page_1.lin_reg_predict.text())]])
            res = regression1.predict(ar)
            self.page_1.label_result.setText(
                f"при x={float(self.page_1.lin_reg_predict.text())} y={np.round(res[0][0], 4)}")
        except:
            self.page_1.label_result.setText(f"Введіть правильні дані")
            self.page_1.label_result.setStyleSheet("background-color: rgb(255, 115, 117);")
        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання predict_lin: {execution_time:.4f} секунд")

    def chosen_multy_regression(self):
        if self.page_2.combobox_x_multy_regression.currentIndexChanged:
            text = self.page_2.combobox_x_multy_regression.text()
            resultant_string = text[1:]
            self.page_2.label_chosen_multy.setText(resultant_string)
            self._X_multy = self.page_2.label_chosen_multy.text().split(",")
        if self.page_2.comboBox_y_multy_regression.currentIndexChanged:
            self._y_multy = self.page_2.comboBox_y_multy_regression.currentText()

    def predict_multy_lin_regression(self):
        start_time = time.time()
        regression_multy = MultipleLinearRegression(self._data[self._X_multy], self._data[self._y_multy])
        regression_multy.linear_regression()
        self.page_2.equation_multy_regression.setText(f"Рівняння: {regression_multy.equation()}")
        self.page_2.r2_multy_regression.setText(f"R^2= {regression_multy.r2_value()}")
        self.page_2.b0_multy_regression.setText(f"b0= {regression_multy.b0_value()}")
        if self.page_2.lineEdit_x_multy_regression.text() != "":
            try:
                self.page_2.result_predict_multy.setStyleSheet("background-color: rgb(255, 255, 255);")
                ar_float = []
                ar = self.page_2.lineEdit_x_multy_regression.text().split(';')
                for i in ar:
                    ar_float.append(float(i))
                res = regression_multy.predict([ar_float])
                res_str = "при x={"
                for a in ar_float:
                    res_str = res_str + f"{a},"
                res_str = res_str[:-1] + "}"
                self.page_2.result_predict_multy.setText(f"{res_str} y={np.round(res[0], 4)}")
            except:
                self.page_2.result_predict_multy.setText(f"Введіть коректні дані")
                self.page_2.result_predict_multy.setStyleSheet("background-color: rgb(255, 115, 117);")
        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання predict_multy_lin_regression: {execution_time:.4f} секунд")

    def chosen_knn_regression(self):
        if self.page_3.combobox_x_knnRegression.currentTextChanged:
            text = self.page_3.combobox_x_knnRegression.text()
            resultant_string = text[1:]
            self.page_3.label_chosen_x_knnRegression.setText(resultant_string)
            self._X_knn_regression = self.page_3.label_chosen_x_knnRegression.text().split(",")
        if self.page_3.comboBox_Y_knnRegression.currentIndexChanged:
            self._y_knn_regression = self.page_3.comboBox_Y_knnRegression.currentText()

    def predict_knn_regression(self):
        start_time = time.time()
        self.page_3.label_k.setStyleSheet("background-color: rgb(255, 255, 255);")
        regr_knn = KNNRegression(self._data[self._X_knn_regression], self._data[self._y_knn_regression])
        try:
            regr_knn.knn_regression(int(self.page_3.lineEdit_num_neigh.text()))
            self.page_3.label_mae_knnRegression.setText(f"MAE={regr_knn.mae_value()}")
            self.page_3.label_mse_knnRegression.setText(f"MSE={regr_knn.mse_value()}")
            self.page_3.label_rmse_knnRegression.setText(f"RMSE={regr_knn.rmse_value()}")
            self.page_3.label_r2_knnRegression.setText(f"R^2= {regr_knn.r2_value()}")
        except:
            self.page_3.label_k.setText("k - кількість сусідів:          Обов'язкове поле")
            self.page_3.label_k.setStyleSheet("background-color: rgb(255, 115, 117);")
            self.page_3.label_mae_knnRegression.setText("")
            self.page_3.label_mse_knnRegression.setText("")
            self.page_3.label_rmse_knnRegression.setText("")
            self.page_3.label_r2_knnRegression.setText("")

        if self.page_3.lineEdit_data_predict.text() != "":
            self.page_3.label_result_knnRegression.setText("")
            try:
                self.page_3.label_data_predict_text.setStyleSheet("background-color: rgb(255, 255, 255);")
                ar_float = []
                ar = self.page_3.lineEdit_data_predict.text().split(';')
                for i in ar:
                    ar_float.append(float(i))
                res = regr_knn.predict([ar_float], int(self.page_3.lineEdit_num_neigh.text()))
                res_str = "при x={"
                for a in ar_float:
                    res_str = res_str + f"{a},"
                res_str = res_str[:-1] + "}"
                self.page_3.label_result_knnRegression.setText(f"{res_str} y={np.round(res[0], 4)}")
            except:
                self.page_3.label_data_predict_text.setText(
                    "Дані для передбачення результату          Введіть коректні дані")
                self.page_3.label_data_predict_text.setStyleSheet("background-color: rgb(255, 115, 117);")

        else:
            self.page_3.label_result_knnRegression.setText("")

        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання predict_knn_regression: {execution_time:.4f} секунд")

    def find_best_k_knn_regression(self):
        start_time = time.time()  # Початковий час
        try:
            self.page_3.label_result_neigh.setStyleSheet("background-color: rgb(255, 255, 255);")
            regression_knn_best = KNNRegression(self._data[self._X_knn_regression], self._data[self._y_knn_regression])
            regression_knn_best.plot_knn(int(self.page_3.lineEdit_min_neigh.text()),
                                         int(self.page_3.lineEdit_max_neigh.text()),
                                         self.page_3.canvas_knnRegression)
            min_er, best_k = regression_knn_best.find_best_k(int(self.page_3.lineEdit_min_neigh.text()),
                                                             int(self.page_3.lineEdit_max_neigh.text()))
            self.page_3.label_result_neigh.setText(f"Найкращий результат {np.round(min_er, 4)} при k={best_k} ")
            regression_knn_best.find_best_values(int(self.page_3.lineEdit_min_neigh.text()),
                                                 int(self.page_3.lineEdit_max_neigh.text()))
            self.page_3.label_mae_best_knnRegression.setText(f"MAE={regression_knn_best.best_mae_value()}")
            self.page_3.label_mse_best_knnRegression.setText(f"MSE={regression_knn_best.best_mse_value()}")
            self.page_3.label_rmse_best_knnRegression.setText(f"RMSE={regression_knn_best.best_rmse_value()}")
            self.page_3.label_r2best_knnRegression.setText(f"R^2= {regression_knn_best.best_r2_value()}")
        except:
            self.page_3.label_result_neigh.setText("Введіть коректні дані")
            self.page_3.label_result_neigh.setStyleSheet("background-color: rgb(255, 115, 117);")
            self.page_3.label_mae_best_knnRegression.setText("")
            self.page_3.label_mse_best_knnRegression.setText("")
            self.page_3.label_rmse_best_knnRegression.setText("")
            self.page_3.label_r2best_knnRegression.setText("")
        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання find_best_k_knn_regression: {execution_time:.4f} секунд")

    def chosen_knn_classification(self):
        if self.page_4.combobox_x_knnClassification.currentTextChanged:
            text = self.page_4.combobox_x_knnClassification.text()
            resultant_string = text[1:]
            self.page_4.x_knnClassification.setText(resultant_string)
            self._X_knnClassification = self.page_4.x_knnClassification.text().split(",")
        if self.page_4.combobox_y_knnClassification.currentIndexChanged:
            self._y_knnClassification = self.page_4.combobox_y_knnClassification.currentText()

    def predict_knn_classification(self):
        start_time = time.time()  # Початковий ча
        self.page_4.result_predict_knnClassification.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_4.label_k_knnClassification.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_4.label_data_knnClassification.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_4.range_clas.setStyleSheet("background-color: rgb(255, 255, 255);")

        knn_classification = KNNClassification(self._data[self._X_knnClassification],
                                               self._data[self._y_knnClassification])
        if self.page_4.lineEdit_num_class_knnClassification.text() != "":
            try:
                res = knn_classification.make_classes(int(self.page_4.lineEdit_num_class_knnClassification.text()))
                self.page_4.range_clas.setText(res)
            except:
                self.page_4.range_clas.setText("Введіть коректні дані")
                self.page_4.range_clas.setStyleSheet("background-color: rgb(255, 115, 117);")

        if self.page_4.lineEdit_k_knnClassification.text() != "":
            try:
                self.page_4.label_k_knnClassification.setText("k - кількість сусідів")
                knn_classification.knn_classification(int(self.page_4.lineEdit_k_knnClassification.text()))
                self.page_4.label_res_knn.setText(knn_classification.res_value())
                knn_classification.plot_matrix(self.page_4.canvas_knnClassification)
            except:
                self.page_4.label_k_knnClassification.setText("k - кількість сусідів            Введіть коректні дані")
                self.page_4.label_k_knnClassification.setStyleSheet("background-color: rgb(255, 115, 117);")
        else:
            self.page_4.label_k_knnClassification.setText("k - кількість сусідів            Обов'язкове поле")
            self.page_4.label_k_knnClassification.setStyleSheet("background-color: rgb(255, 115, 117);")

        if self.page_4.lineEdit_data_knnClassification.text() != "":
            try:
                self.page_4.label_data_knnClassification.setText("Дані  для передбачення")
                ar_float = []
                ar = self.page_4.lineEdit_data_knnClassification.text().split(';')
                for i in ar:
                    ar_float.append(float(i))
                res = knn_classification.predict([ar_float], int(self.page_4.lineEdit_k_knnClassification.text()))
                self.page_4.result_predict_knnClassification.setText(f"{np.round(res[0], 4)}")
            except:
                self.page_4.label_data_knnClassification.setText(
                    "Дані  для передбачення            Введіть коректні дані")
                self.page_4.label_data_knnClassification.setStyleSheet("background-color: rgb(255, 115, 117);")

        else:
            self.page_4.result_predict_knnClassification.setText("")

        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання predict_knn_classification: {execution_time:.4f} секунд")

    def find_best_k_knn_classification(self):
        start_time = time.time()  # Початковий час
        self.page_4.label_best_k_knnClassification.setStyleSheet("background-color: rgb(255, 255, 255);")
        knn_classification_best = KNNClassification(self._data[self._X_knnClassification],
                                                    self._data[self._y_knnClassification])
        if self.page_4.lineEdit_num_class_knnClassification.text() != "":
            try:
                knn_classification_best.make_classes(int(self.page_4.lineEdit_num_class_knnClassification.text()))
            except:
                self.page_4.label_best_k_knnClassification.setText("Введіть коректну кількість класів")
                self.page_4.label_best_k_knnClassification.setStyleSheet("background-color: rgb(255, 115, 117);")
        try:
            knn_classification_best.plot_knn_clas(int(self.page_4.lineEdit_min_k_knnClassification.text()),
                                                  int(self.page_4.lineEdit_max_k_knnClassification.text()),
                                                  self.page_4.canvas_knnClassification_best)
            min_er, best_k = knn_classification_best.find_best_k(
                int(self.page_4.lineEdit_min_k_knnClassification.text()),
                int(self.page_4.lineEdit_max_k_knnClassification.text()))
            self.page_4.label_best_k_knnClassification.setText(
                f"Найкращий результат {np.round(min_er, 4)} при k={best_k} ")
            knn_classification_best.find_best_values(int(self.page_4.lineEdit_min_k_knnClassification.text()),
                                                     int(self.page_4.lineEdit_max_k_knnClassification.text()))
            self.page_4.label_best_result_knnClassification.setText(knn_classification_best.best_res_value())
            knn_classification_best.plot_best_matrix(self.page_4.canvas_knnClassification_best_matrix)
        except:
            self.page_4.label_best_k_knnClassification.setText("Введіть коректні дані")
            self.page_4.label_best_k_knnClassification.setStyleSheet("background-color: rgb(255, 115, 117);")

        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання find_best_k_knn_classification: {execution_time:.4f} секунд")

    def chosen_logistic_regression(self):
        if self.page_5.combobox_x_LogisticRegression.currentTextChanged:
            text = self.page_5.combobox_x_LogisticRegression.text()
            resultant_string = text[1:]
            self.page_5.chosen_x_LogisticRegression.setText(resultant_string)
            self._X_LogisticRegression = self.page_5.chosen_x_LogisticRegression.text().split(",")
        if self.page_5.comboBox_y_LogisticRegression.currentIndexChanged:
            self._y_LogisticRegression = self.page_5.comboBox_y_LogisticRegression.currentText()

    def predict_result_logistic_regression(self):
        start_time = time.time()  # Початковий час
        self.page_5.b0_LogisticRegression.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_5.predict_LogisticRegression.setStyleSheet("background-color: rgb(255, 255, 255);")
        try:
            logicregr = MyLogisticRegression(self._data[self._X_LogisticRegression],
                                             self._data[self._y_LogisticRegression])
            try:
                logicregr.plot_barchart(self.page_5.canvas_LogisticRegression)
                logicregr.logistic_regression()
                self.page_5.b0_LogisticRegression.setText(f"b0={logicregr.b0_value()}")
                self.page_5.coefficient_LogisticRegression.setText(logicregr.coefficients_value())
                self.page_5.score_LogisticRegression.setText(logicregr.report_value())
                logicregr.plot_matrix(self.page_5.canvas_logic_matrix)
            except:
                self.page_5.b0_LogisticRegression.setText("Введіть коректні дані")
                self.page_5.b0_LogisticRegression.setStyleSheet("background-color: rgb(255, 115, 117);")
        except:
            self.page_5.predict_LogisticRegression.setText("Введіть коректні дані")
            self.page_5.predict_LogisticRegression.setStyleSheet("background-color: rgb(255, 115, 117);")

        if self.page_5.lineEdit_data_LogisticRegression.text() != "":
            try:
                ar_float = []
                ar = self.page_5.lineEdit_data_LogisticRegression.text().split(';')
                for i in ar:
                    ar_float.append(float(i))
                res = logicregr.predict([ar_float])
                resstr = "при x={"
                for a in ar_float:
                    resstr = resstr + f"{a},"
                resstr = resstr[:-1] + "}"
                self.page_5.predict_LogisticRegression.setText(f"{resstr} y={np.round(res[0], 4)}")
            except:
                self.page_5.predict_LogisticRegression.setText("Введіть коректні дані")
                self.page_5.predict_LogisticRegression.setStyleSheet("background-color: rgb(255, 115, 117);")
        else:
            self.page_5.predict_LogisticRegression.setText("")

        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання predict_result_logistic_regression: {execution_time:.4f} секунд")

    def chosen_cross_validation(self):

        if self.page_6.combobox_x_CrossValidation.currentTextChanged:
            text = self.page_6.combobox_x_CrossValidation.text()
            resultant_string = text[1:]
            self.page_6.chosen_x_CrossValidation.setText(resultant_string)
            self._X_CrossValidation = self.page_6.chosen_x_CrossValidation.text().split(",")
        if self.page_6.comboBox_y_CrossValidation.currentIndexChanged:
            self._y_CrossValidation = self.page_6.comboBox_y_CrossValidation.currentText()

    def find_cross_validation(self):
        start_time = time.time()
        self.page_6.chosen_x_CrossValidation.setStyleSheet("background-color: rgb(255, 255, 255);")
        try:
            cross_validation = LeaveOneOutCrossValidation(self._data[self._X_CrossValidation],
                                                          self._data[self._y_CrossValidation])
            tab = cross_validation.compare_methods()
            TableWidget().set(self.page_6.tableWidget_CrossValidation, tab)
            header = self.page_6.tableWidget_CrossValidation.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        except:
            self.page_6.chosen_x_CrossValidation.setText("Введіть коректні дані")
            self.page_6.chosen_x_CrossValidation.setStyleSheet("background-color: rgb(255, 115, 117);")

        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання find_cross_validation: {execution_time:.4f} секунд")

    def chosen_k_cross_validation(self):
        if self.page_7.combobox_x_kCrossValidation.currentTextChanged:
            text = self.page_7.combobox_x_kCrossValidation.text()
            resultant_string = text[1:]
            self.page_7.chosen_x_kCrossValidation.setText(resultant_string)
            self._X_kCrossValidation = self.page_7.chosen_x_kCrossValidation.text().split(",")
        if self.page_6.comboBox_y_CrossValidation.currentIndexChanged:
            self._y_kCrossValidation = self.page_7.comboBox_y_kCrossValidation.currentText()

    def find_k_cross_validation(self):
        start_time = time.time()  # Початковий час
        self.page_7.label_num_k_kCrossValidation.setStyleSheet("background-color: rgb(255, 255, 255);")
        if self.page_7.lineEdit_num_k_kCrossValidation.text() != '':
            try:
                k_cross_validation = KFoldCrossValidation(self._data[self._X_kCrossValidation],
                                                          self._data[self._y_kCrossValidation])
                tab = k_cross_validation.compare_methods(int(self.page_7.lineEdit_num_k_kCrossValidation.text()))
                TableWidget().set(self.page_7.tableWidget_2, tab)
                header = self.page_7.tableWidget_2.horizontalHeader()
                header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
                header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
                header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
                header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            except:
                self.page_7.label_num_k_kCrossValidation.setText("Значення k         Введіть коректні дані")
                self.page_7.label_num_k_kCrossValidation.setStyleSheet("background-color: rgb(255, 115, 117);")
        else:
            self.page_7.label_num_k_kCrossValidation.setText("Значення k         Обов'язкове поле")
            self.page_7.label_num_k_kCrossValidation.setStyleSheet("background-color: rgb(255, 115, 117);")

        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання find_k_cross_validation: {execution_time:.4f} секунд")

    def find_best_k_cross_validation(self):
        start_time = time.time()  # Початковий час
        self.page_7.label_max_k_kCrossValidation.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_7.label_mink_kCrossValidation.setStyleSheet("background-color: rgb(255, 255, 255);")
        if self.page_7.lineEdit_mink_kCrossValidation.text() != '' \
                and self.page_7.lineEdit_max_k_kCrossValidation.text() != '':
            k_cross_validation = KFoldCrossValidation(self._data[self._X_kCrossValidation],
                                                      self._data[self._y_kCrossValidation])

            try:
                mink = int(self.page_7.lineEdit_mink_kCrossValidation.text())
                max_k = int(self.page_7.lineEdit_max_k_kCrossValidation.text())
                k_cross_validation.plot_best(mink, max_k, self.page_7.comboBox_method_kCrossValidation.currentText(),
                                             self.page_7.canvas_best_kCrossValidation)
            except:
                self.page_7.label_mink_kCrossValidation.setText(
                    "Мінімальне значення k            Введіть коректні дані")
                self.page_7.label_mink_kCrossValidation.setStyleSheet("background-color: rgb(255, 115, 117);")
        elif self.page_7.lineEdit_mink_kCrossValidation.text() == '' \
                and self.page_7.lineEdit_max_k_kCrossValidation.text() != '':
            self.page_7.label_mink_kCrossValidation.setText("Мінімальне значення k            Обов'язкове поле")
            self.page_7.label_mink_kCrossValidation.setStyleSheet("background-color: rgb(255, 115, 117);")
        elif self.page_7.lineEdit_mink_kCrossValidation.text() != '' \
                and self.page_7.lineEdit_max_k_kCrossValidation.text() == '':
            self.page_7.label_max_k_kCrossValidation.setText("Максимальне значення k            Обов'язкове поле")
            self.page_7.label_max_k_kCrossValidation.setStyleSheet("background-color: rgb(255, 115, 117);")

        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання find_best_k_cross_validation: {execution_time:.4f} секунд")

    def chosen_poly_regression(self):
        if self.page_8.comboBox_x_PolynomialRegression.currentIndexChanged:
            self._X_PolynomialRegression.clear()
            self._X_PolynomialRegression.append(self.page_8.comboBox_x_PolynomialRegression.currentText())
        if self.page_8.comboBox_y_PolynomialRegression.currentIndexChanged:
            self._y_PolynomialRegression = self.page_8.comboBox_y_PolynomialRegression.currentText()

    def find_poly_regression(self):
        start_time = time.time()  # Початковий час
        self.page_8.label_degree.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_8.label_result_PolynomialRegression.setStyleSheet("background-color: rgb(255, 255, 255);")
        poly_regression = PolynomialRegression(self._data[self._X_PolynomialRegression[0]],
                                               self._data[self._y_PolynomialRegression])
        if self.page_8.lineEdit_degree.text() != "":
            try:
                d = int(self.page_8.lineEdit_degree.text())
                poly_regression.polynomial_regression(d)
                self.page_8.label_rmse_PolynomialRegression.setText(f"RMSE={poly_regression.rmse_value()}")
                poly_regression.plot_poly(self.page_8.canvas_PolynomialRegression,
                                          int(self.page_8.lineEdit_degree.text()))
            except:
                self.page_8.label_degree.setText("Степінь      Введіть коректні дані")
                self.page_8.label_degree.setStyleSheet("background-color: rgb(255, 115, 117);")

            if self.page_8.lineEdit_data_PolynomialRegression.text() != "":
                try:
                    arr = np.array([[float(self.page_8.lineEdit_data_PolynomialRegression.text())]])
                    d = int(self.page_8.lineEdit_degree.text())
                    res = poly_regression.predict_regression(arr, d)
                    self.page_8.label_result_PolynomialRegression.setText(
                        f"при x={float(self.page_8.lineEdit_data_PolynomialRegression.text())} y={res}")
                except:
                    self.page_8.label_result_PolynomialRegression.setText("Введіть коректні дані")
                    self.page_8.label_result_PolynomialRegression.setStyleSheet("background-color: rgb(255, 115, 117);")
            else:
                self.page_8.label_result_PolynomialRegression.setText("")
        else:
            self.page_8.label_degree.setText("Степінь      Обов'язкове поле")
            self.page_8.label_degree.setStyleSheet("background-color: rgb(255, 115, 117);")

        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання find_poly_regression: {execution_time:.4f} секунд")

    def chosen_cub_spline(self):
        if self.page_9.comboBox_x_CubicSpline.currentIndexChanged:
            self._X_CubicSpline.clear()
            self._X_CubicSpline.append(self.page_9.comboBox_x_CubicSpline.currentText())

        if self.page_9.comboBox_y_CubicSpline.currentIndexChanged:
            self._y_CubicSpline = self.page_9.comboBox_y_CubicSpline.currentText()

    def predict_cub_spline(self):
        start_time = time.time()  # Початковий час
        self.page_9.label_rmse_CubicSpline.setStyleSheet("background-color: rgb(255, 255, 255);")
        try:
            cub_spline = CubicSpline(self._data[self._X_CubicSpline[0]], self._data[self._y_CubicSpline])
            cub_spline.cubic_spline()
            self.page_9.label_rmse_CubicSpline.setText(f"RMSE={cub_spline.rmse_value()}")
            cub_spline.plot_cubspl(self.page_9.canvas_CubicSpline)
        except:
            self.page_9.label_rmse_CubicSpline.setText("Введіть коректні дані")
            self.page_9.label_rmse_CubicSpline.setStyleSheet("background-color: rgb(255, 115, 117);")
        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання predict_cub_spline: {execution_time:.4f} секунд")

    def chosen_natural_cub(self):
        if self.page_10.comboBox_x_NaturalCubicSpline.currentIndexChanged:
            self._X_NaturalCubicSpline.clear()
            self._X_NaturalCubicSpline.append(self.page_10.comboBox_x_NaturalCubicSpline.currentText())
        if self.page_10.comboBox_y_NaturalCubicSpline.currentIndexChanged:
            self._y_NaturalCubicSpline = self.page_10.comboBox_y_NaturalCubicSpline.currentText()

    def predict_natural_cub(self):
        start_time = time.time()  # Початковий час
        self.page_10.label_rmse_NaturalCubicSpline.setStyleSheet("background-color: rgb(255, 255, 255);")
        try:
            natural_cub = NaturalCubicSpline(self._data[self._X_NaturalCubicSpline[0]],
                                             self._data[self._y_NaturalCubicSpline])
            natural_cub.natural_cubic_spline()
            self.page_10.label_rmse_NaturalCubicSpline.setText(f"RMSE={natural_cub.rmse_value()}")
            natural_cub.plot_nat_cub(self.page_10.canvas_NaturalCubicSpline)
        except:
            self.page_10.label_rmse_NaturalCubicSpline.setText("Введіть коректні дані")
            self.page_10.label_rmse_NaturalCubicSpline.setStyleSheet("background-color: rgb(255, 115, 117);")
        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання predict_natural_cub: {execution_time:.4f} секунд")

    def chosen_ridge(self):
        if self.page_11.combobox_x_ridge.currentIndexChanged:
            text = self.page_11.combobox_x_ridge.text()
            resultant_string = text[1:]
            self.page_11.label_chosen_ridge.setText(resultant_string)
            self._X_ridge = self.page_11.label_chosen_ridge.text().split(",")
        if self.page_11.comboBox_y_ridge.currentIndexChanged:
            self._y_ridge = self.page_11.comboBox_y_ridge.currentText()

    def predict_ridge(self):
        start_time = time.time()  # Початковий час
        self.page_11.label_alpha.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_11.label_result_ridge.setStyleSheet("background-color: rgb(255, 255, 255);")
        ridge = RidgeRegression(self._data[self._X_ridge], self._data[self._y_ridge])
        if self.page_11.lineEdit_alpha.text() != "":
            try:
                d = float(self.page_11.lineEdit_alpha.text())
                ridge.perform_ridge_regression(d)
                self.page_11.label_mse_ridge.setText(f"MSE={ridge.mse_value()}")
                ridge.plot_ridge(self.page_11.canvas_ridge)
            except:
                self.page_11.label_alpha.setText("Степінь      Введіть коректні дані")
                self.page_11.label_alpha.setStyleSheet("background-color: rgb(255, 115, 117);")

            if self.page_11.lineEdit_data_ridge.text() != "":
                try:
                    d = float(self.page_11.lineEdit_alpha.text())
                    ar_float = []
                    ar = self.page_11.lineEdit_data_ridge.text().split(';')
                    for i in ar:
                        ar_float.append(float(i))
                    res = ridge.predict_ridge([ar_float], d)
                    res_str = "при x={"
                    for a in ar_float:
                        res_str = res_str + f"{a},"
                    res_str = res_str[:-1] + "}"
                    self.page_11.label_result_ridge.setText(f"{res_str} y={np.round(res[0], 4)}")
                except:
                    self.page_11.label_result_ridge.setText("Введіть коректні дані")
                    self.page_11.label_result_ridge.setStyleSheet("background-color: rgb(255, 115, 117);")
            else:
                self.page_11.label_result_ridge.setText("")
        else:
            self.page_11.label_alpha.setText("alpha      Обов'язкове поле")
            self.page_11.label_alpha.setStyleSheet("background-color: rgb(255, 115, 117);")
        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання predict_ridge: {execution_time:.4f} секунд")

    def find_best_alpha(self):
        start_time = time.time()  # Початковий час
        try:
            self.page_11.label_best_result_alpha.setStyleSheet("background-color: rgb(255, 255, 255);")
            ridge_best = RidgeRegression(self._data[self._X_ridge], self._data[self._y_ridge])
            ridge_best.find_best_alpha(float(self.page_11.lineEdit_min_alpha.text()),
                                       float(self.page_11.lineEdit_max_alpha.text()))

            ridge_best.plot_res_best_alpha(self.page_11.canvas_ridge_best)

            self.page_11.label_best_result_alpha.setText(
                f"Найкращий результат {np.round(ridge_best.best_mse_value(), 4)} "
                f"при alpha={np.round(ridge_best.best_alpha_value(), 4)} ")
            ridge_best.plot_best_alpha_mse(float(self.page_11.lineEdit_min_alpha.text()),
                                           float(self.page_11.lineEdit_max_alpha.text()),
                                           self.page_11.canvas_ridge_best_mse)
        except:
            self.page_11.label_best_result_alpha.setText("Введіть коректні дані")
            self.page_11.label_best_result_alpha.setStyleSheet("background-color: rgb(255, 115, 117);")
        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання find_best_alpha: {execution_time:.4f} секунд")

    def chosen_lasso(self):
        if self.page_12.combobox_x_lasso.currentIndexChanged:
            text = self.page_12.combobox_x_lasso.text()
            resultant_string = text[1:]
            self.page_12.label_chosen_lasso.setText(resultant_string)
            self._X_lasso = self.page_12.label_chosen_lasso.text().split(",")

        if self.page_12.comboBox_y_lasso.currentIndexChanged:
            self._y_lasso = self.page_12.comboBox_y_lasso.currentText()

    def predict_lasso(self):
        start_time = time.time()  # Початковий час
        self.page_12.label_alpha_lasso.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_12.label_result_lasso.setStyleSheet("background-color: rgb(255, 255, 255);")
        lasso = LassoRegression(self._data[self._X_lasso], self._data[self._y_lasso])
        if self.page_12.lineEdit_alpha_lasso.text() != "":
            try:
                d = float(self.page_12.lineEdit_alpha_lasso.text())
                lasso.perform_lasso_regression(d)
                self.page_12.label_mse_lasso.setText(f"MSE={lasso.mse_value()}")
                lasso.plot_lasso(self.page_12.canvas_lasso)
            except:
                self.page_12.label_alpha_lasso.setText("Степінь      Введіть коректні дані")
                self.page_12.label_alpha_lasso.setStyleSheet("background-color: rgb(255, 115, 117);")

            if self.page_12.lineEdit_data_lasso.text() != "":
                try:
                    d = float(self.page_12.lineEdit_alpha_lasso.text())
                    ar_float = []
                    ar = self.page_12.lineEdit_data_lasso.text().split(';')
                    for i in ar:
                        ar_float.append(float(i))
                    res = lasso.predict_lasso([ar_float], d)
                    res_str = "при x={"
                    for a in ar_float:
                        res_str = res_str + f"{a},"
                    res_str = res_str[:-1] + "}"
                    self.page_12.label_result_lasso.setText(f"{res_str} y={np.round(res[0], 4)}")
                except:
                    self.page_12.label_result_lasso.setText("Введіть коректні дані")
                    self.page_12.label_result_lasso.setStyleSheet("background-color: rgb(255, 115, 117);")
            else:
                self.page_12.label_result_lasso.setText("")
        else:
            self.page_12.label_alpha_lasso.setText("alpha      Обов'язкове поле")
            self.page_12.label_alpha_lasso.setStyleSheet("background-color: rgb(255, 115, 117);")
        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання predict_lasso: {execution_time:.4f} секунд")

    def find_best_alpha_lasso(self):
        start_time = time.time()  # Початковий час
        try:
            self.page_12.label_best_result_alpha_lasso.setStyleSheet("background-color: rgb(255, 255, 255);")
            lasso_best = LassoRegression(self._data[self._X_lasso], self._data[self._y_lasso])
            lasso_best.find_best_alpha(float(self.page_12.lineEdit_min_alpha_lasso.text()),
                                       float(self.page_12.lineEdit_max_alpha_lasso.text()))

            lasso_best.plot_res_best_alpha(self.page_12.canvas_lasso_best)

            self.page_12.label_best_result_alpha_lasso.setText(
                f"Найкращий результат {np.round(lasso_best.best_mse_value(), 4)}"
                f"при alpha={np.round(lasso_best.best_alpha_value(), 4)} ")

            lasso_best.plot_best_alpha_mse(float(self.page_12.lineEdit_min_alpha_lasso.text()),
                                        float(self.page_12.lineEdit_max_alpha_lasso.text()),
                                        self.page_12.canvas_lasso_best_mse)
        except:
            self.page_12.label_best_result_alpha_lasso.setText("Введіть коректні дані")
            self.page_12.label_best_result_alpha_lasso.setStyleSheet("background-color: rgb(255, 115, 117);")
        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання find_best_alpha_lasso: {execution_time:.4f} секунд")

    def chosen_regression_tree(self):

        if self.page_13.combobox_x_regression_tree.currentIndexChanged:
            text = self.page_13.combobox_x_regression_tree.text()
            resultant_string = text[1:]
            self.page_13.label_chosen_x_regression_tree.setText(resultant_string)
            self._X_regression_tree = self.page_13.label_chosen_x_regression_tree.text().split(",")

        if self.page_13.comboBox_y_regression_tree.currentIndexChanged:
            self._y_regression_tree = self.page_13.comboBox_y_regression_tree.currentText()
        if self.page_13.label_chosen_x_regression_tree.text() != "":
            regression_tree_best = RegressionTree(self._data[self._X_regression_tree],
                                                  self._data[self._y_regression_tree])
            regression_tree_best.perform_best_regression_tree()
            self.page_13.label_best_parameters_regression_tree.setText(
                f"Найкращі параметри:{regression_tree_best.best_params_value()}")
                # f", min к-сть на листку {regression_tree_best.best_params_value()[2]},"
                # f" min к-сть для поділу вершини {regression_tree_best.best_params_value()[1]}"
                # f" ")

    def predict_regression_tree(self):
        start_time = time.time()  # Початковий час
        self.page_13.result_regression_tree.setStyleSheet("background-color: rgb(255, 255, 255);")
        regression_tree = RegressionTree(self._data[self._X_regression_tree], self._data[self._y_regression_tree])
        if self.page_13.lineEdit_depth_regression_tree.text() != "" \
                and self.page_13.lineEdit_regression_tree_leaf.text() != "" \
                and self.page_13.lineEdit_regression_tree_split.text() != "":
            try:
                d = int(self.page_13.lineEdit_depth_regression_tree.text())
                s = int(self.page_13.lineEdit_regression_tree_split.text())
                leaf = int(self.page_13.lineEdit_regression_tree_leaf.text())
                reg = regression_tree.perform_regression_tree(d, s, leaf)
                self.page_13.mse_regression_tree.setText(f"MSE={regression_tree.mse_value()}")
                regression_tree.plot_regression_tree(self.page_13.canvas_regression_tree, self._X_regression_tree, reg)
            except:
                self.page_13.result_regression_tree.setText("Степінь      Введіть коректні дані")
                self.page_13.result_regression_tree.setStyleSheet("background-color: rgb(255, 115, 117);")

            if self.page_13.lineEdit_x_regression_tree.text() != "":
                try:
                    d = int(self.page_13.lineEdit_depth_regression_tree.text())
                    s = int(self.page_13.lineEdit_regression_tree_split.text())
                    leaf = int(self.page_13.lineEdit_regression_tree_leaf.text())
                    ar_float = []
                    ar = self.page_13.lineEdit_x_regression_tree.text().split(';')
                    for i in ar:
                        ar_float.append(float(i))
                    res = regression_tree.predict_regression_tree([ar_float], d, s, leaf)
                    res_str = "при x={"
                    for a in ar_float:
                        res_str = res_str + f"{a},"
                    res_str = res_str[:-1] + "}"
                    self.page_13.result_predict_regression_tree.setText(f"{res_str} y={np.round(res, 4)}")
                except:
                    self.page_13.result_predict_regression_tree.setText("Введіть коректні дані")
                    self.page_13.result_predict_regression_tree.setStyleSheet("background-color: rgb(255, 115, 117);")
            else:
                self.page_13.result_predict_regression_tree.setText("")
        else:
            self.page_13.result_regression_tree.setText("      Обов'язкове поле")
            self.page_13.result_regression_tree.setStyleSheet("background-color: rgb(255, 115, 117);")
        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання predict_regression_tree: {execution_time:.4f} секунд")


    def chosen_cl_tree(self):

        if self.page_14.combobox_x_cl_tree.currentIndexChanged:
            text = self.page_14.combobox_x_cl_tree.text()
            resultant_string = text[1:]
            self.page_14.label_chosen_x_cl_tree.setText(resultant_string)
            self._X_cl_tree = self.page_14.label_chosen_x_cl_tree.text().split(",")

        if self.page_14.comboBox_y_cl_tree.currentIndexChanged:
            self._y_cl_tree = self.page_14.comboBox_y_cl_tree.currentText()

        if self.page_14.label_chosen_x_cl_tree.text() != "":
            cl_tree_best = ClassificationTree(self._data[self._X_cl_tree], self._data[self._y_cl_tree])
            cl_tree_best.perform_best_cl_tree()

            self.page_14.label_best_parameters_cl_tree.setText(
                f"Найкращі параметри: {cl_tree_best.best_params_value()}")

    def predict_cl_tree(self):
        start_time = time.time()  # Початковий час
        self.page_14.result_cl_tree_text.setStyleSheet("background-color: rgb(255, 255, 255);")
        cl_tree = ClassificationTree(self._data[self._X_cl_tree], self._data[self._y_cl_tree])
        if self.page_14.lineEdit_depth_cl_tree.text() != "" and self.page_14.lineEdit_cl_tree_leaf.text() != "" \
                and self.page_14.lineEdit_cl_tree_split.text() != "":
            try:
                d = int(self.page_14.lineEdit_depth_cl_tree.text())
                s = int(self.page_14.lineEdit_cl_tree_split.text())
                leaf = int(self.page_14.lineEdit_cl_tree_leaf.text())
                cl = cl_tree.perform_classification_tree(d, s, leaf)
                self.page_14.report_cl_tree.setText(cl_tree.report_value())

                cl_tree.plot_cl_tree(self.page_14.canvas_cl_tree, self._X_cl_tree, cl)
                cl_tree.plot_cl_matrix(self.page_14.canvas_cl_tree_matrix)
            except:
                self.page_14.result_cl_tree_text.setText("Степінь      Введіть коректні дані")
                self.page_14.result_cl_tree_text.setStyleSheet("background-color: rgb(255, 115, 117);")

            if self.page_14.lineEdit_x_cl_tree.text() != "":
                try:
                    d = int(self.page_14.lineEdit_depth_cl_tree.text())
                    s = int(self.page_14.lineEdit_cl_tree_split.text())
                    leaf = int(self.page_14.lineEdit_cl_tree_leaf.text())
                    ar_float = []
                    ar = self.page_14.lineEdit_x_cl_tree.text().split(';')
                    for i in ar:
                        ar_float.append(float(i))
                    res = cl_tree.predict_cl_tree([ar_float], d, s, leaf)
                    res_str = "при x={"
                    for a in ar_float:
                        res_str = res_str + f"{a},"
                    res_str = res_str[:-1] + "}"
                    self.page_14.result_predict_cl_tree.setText(f"{res_str} y={res}")
                except:
                    self.page_14.result_predict_cl_tree.setText("Введіть коректні дані")
                    self.page_14.result_predict_cl_tree.setStyleSheet("background-color: rgb(255, 115, 117);")
            else:
                self.page_14.result_predict_cl_tree.setText("")
        else:
            self.page_14.result_cl_tree_text.setText("      Обов'язкове поле")
            self.page_14.result_cl_tree_text.setStyleSheet("background-color: rgb(255, 115, 117);")
        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання predict_cl_tree: {execution_time:.4f} секунд")

    def chosen_lin_disc(self):
        if self.page_15.combobox_x_LinearDiscriminant.currentTextChanged:
            text = self.page_15.combobox_x_LinearDiscriminant.text()
            resultant_string = text[1:]
            self.page_15.chosen_x_LinearDiscriminant.setText(resultant_string)
            self._X_LinearDiscriminant = self.page_15.chosen_x_LinearDiscriminant.text().split(",")
        if self.page_15.comboBox_y_LinearDiscriminant.currentIndexChanged:
            self._y_LinearDiscriminant = self.page_15.comboBox_y_LinearDiscriminant.currentText()
            self.page_15.label_choose_x_LinearDiscriminant.setText(
                f"Виберіть <={len(np.unique(self._data[self._y_LinearDiscriminant])) - 1} стовпців")

    def predict_result_lin_disc(self):
        start_time = time.time()  # Початковий час
        self.page_15.report_LinearDiscriminant.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_15.predict_LinearDiscriminant.setStyleSheet("background-color: rgb(255, 255, 255);")
        try:
            lin_disc = LinearDiscriminant(self._data[self._X_LinearDiscriminant],
                                          self._data[self._y_LinearDiscriminant])
        except:
            self.page_15.predict_LinearDiscriminant.setText("Введіть коректні дані ")
            self.page_15.predict_LinearDiscriminant.setStyleSheet("background-color: rgb(255, 115, 117);")
        try:
            lin_disc.perform_lda()
            lin_disc.plot_lda(self.page_15.canvas_LinearDiscriminant)
            lin_disc.plot_lda_matrix(self.page_15.canvas_LinearDiscriminant_matrix)
        except:
            self.page_15.report_LinearDiscriminant.setText("Введіть коректні дані")
            self.page_15.report_LinearDiscriminant.setStyleSheet("background-color: rgb(255, 115, 117);")
        if self.page_15.lineEdit_data_LinearDiscriminant.text() != "":
            try:
                ar_float = []
                ar = self.page_15.lineEdit_data_LinearDiscriminant.text().split(';')
                for i in ar:
                    ar_float.append(float(i))
                res = lin_disc.predict_lda([ar_float])
                res_str = "при x={"
                for a in ar_float:
                    res_str = res_str + f"{a},"
                res_str = res_str[:-1] + "}"
                self.page_15.predict_LinearDiscriminant.setText(f"{res_str} y={np.round(res, 4)}")
            except:
                self.page_15.predict_LinearDiscriminant.setText("Введіть коректні дані")
                self.page_15.predict_LinearDiscriminant.setStyleSheet("background-color: rgb(255, 115, 117);")
        else:
            self.page_15.predict_LinearDiscriminant.setText("")

        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання predict_result_lin_disc: {execution_time:.4f} секунд")

    def chosen_quadratic_discriminant(self):
        if self.page_16.combobox_x_QuadraticDiscriminant.currentTextChanged:
            text = self.page_16.combobox_x_QuadraticDiscriminant.text()
            resultant_string = text[1:]
            self.page_16.chosen_x_QuadraticDiscriminant.setText(resultant_string)
            self._X_QuadraticDiscriminant = self.page_16.chosen_x_QuadraticDiscriminant.text().split(",")
        if self.page_16.comboBox_y_QuadraticDiscriminant.currentIndexChanged:
            self._y_QuadraticDiscriminant = self.page_16.comboBox_y_QuadraticDiscriminant.currentText()

    def predict_result_quadratic_discriminant(self):
        start_time = time.time()  # Початковий час
        self.page_16.report_QuadraticDiscriminant.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_16.predict_QuadraticDiscriminant.setStyleSheet("background-color: rgb(255, 255, 255);")
        try:
            quad_disc = QuadraticDiscriminant(self._data[self._X_QuadraticDiscriminant],
                                              self._data[self._y_QuadraticDiscriminant])
        except:
            self.page_16.predict_QuadraticDiscriminant.setText("Введіть коректні дані ")
            self.page_16.predict_QuadraticDiscriminant.setStyleSheet("background-color: rgb(255, 115, 117);")
        try:
            quad_disc.perform_qda()
            quad_disc.plot_qda_matrix(self.page_16.canvas_QuadraticDiscriminant)
        except:
            self.page_16.report_QuadraticDiscriminant.setText("Введіть коректні дані")
            self.page_16.report_QuadraticDiscriminant.setStyleSheet("background-color: rgb(255, 115, 117);")
        if self.page_16.lineEdit_data_QuadraticDiscriminant.text() != "":
            try:
                ar_float = []
                ar = self.page_16.lineEdit_data_QuadraticDiscriminant.text().split(';')
                for i in ar:
                    ar_float.append(float(i))
                res = quad_disc.predict_qda([ar_float])
                res_str = "при x={"
                for a in ar_float:
                    res_str = res_str + f"{a},"
                res_str = res_str[:-1] + "}"
                self.page_16.predict_QuadraticDiscriminant.setText(f"{res_str} y={np.round(res[0], 4)}")
            except:
                self.page_16.predict_QuadraticDiscriminant.setText("Введіть коректні дані")
                self.page_16.predict_QuadraticDiscriminant.setStyleSheet("background-color: rgb(255, 115, 117);")
        else:
            self.page_16.predict_QuadraticDiscriminant.setText("")

        end_time = time.time()  # Кінцевий час
        execution_time = end_time - start_time
        print(f"Час виконання predict_result_quadratic_discriminant: {execution_time:.4f} секунд")

    def new_window(self):
        # data_generator = DataGenerator()
        # data = data_generator.generate_data()

        if not self.generate_data_window:  # Створюємо вікно, якщо воно ще не створене
            self.generate_data_window = GenerateWindow()
            self.generate_data_window.data_transferred.connect(self.update_table)
            # self.generate_data_window.set_up_ui()
            self.generate_data_window.closed.connect(
                self.generate_window_closed)  # Підключаємо сигнал про закриття вікна

        # self.data.generate_data_window.data_label.setText(data)  # Оновлюємо дані вікна
        self.generate_data_window.show()  # Показуємо вікно

    def generate_window_closed(self):
        self.generate_data_window = None  # Скидаємо вікно, коли воно закрите

    def update_table(self):
        TableWidget().set(self.data.tableWidget, self.generate_data_window.df)
        self._data = self.generate_data_window.df
        self.clear_data()
