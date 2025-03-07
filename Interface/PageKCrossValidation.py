from PyQt5 import QtCore, QtGui, QtWidgets

from Interface.CheckCombobox import CheckCombobox
from Interface.MplCanvas import MplCanvas


class PageKCrossValidation(QtWidgets.QWidget):
    def __init__(self, stl_btn, font):
        super().__init__()
        self.setObjectName("page_7")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.tabWidget_kCrossValidation = QtWidgets.QTabWidget(self)
        self.tabWidget_kCrossValidation.setFont(font)
        self.tabWidget_kCrossValidation.setObjectName("tabWidget_kCrossValidation")
        self.tab_3 = QtWidgets.QWidget(flags=QtCore.Qt.Widget)
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_choose_x_kCrossValidation = QtWidgets.QLabel(self.tab_3)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_choose_x_kCrossValidation.sizePolicy().hasHeightForWidth())
        self.label_choose_x_kCrossValidation.setSizePolicy(size_policy)
        self.label_choose_x_kCrossValidation.setMinimumSize(QtCore.QSize(0, 60))
        self.label_choose_x_kCrossValidation.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_choose_x_kCrossValidation.setFont(font)
        self.label_choose_x_kCrossValidation.setObjectName("label_choose_x_kCrossValidation")
        self.verticalLayout_20.addWidget(self.label_choose_x_kCrossValidation)
        self.combobox_x_kCrossValidation = CheckCombobox()

        self.verticalLayout_20.addWidget(self.combobox_x_kCrossValidation)
        self.chosen_x_kCrossValidation = QtWidgets.QLabel(self.tab_3)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.chosen_x_kCrossValidation.sizePolicy().hasHeightForWidth())
        self.chosen_x_kCrossValidation.setSizePolicy(size_policy)
        self.chosen_x_kCrossValidation.setMinimumSize(QtCore.QSize(0, 60))
        self.chosen_x_kCrossValidation.setMaximumSize(QtCore.QSize(16777215, 60))
        self.chosen_x_kCrossValidation.setFont(font)
        self.chosen_x_kCrossValidation.setObjectName("chosen_x_kCrossValidation")
        self.verticalLayout_20.addWidget(self.chosen_x_kCrossValidation)
        self.label_choose_y_kCrossValidation = QtWidgets.QLabel(self.tab_3)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_choose_y_kCrossValidation.sizePolicy().hasHeightForWidth())
        self.label_choose_y_kCrossValidation.setSizePolicy(size_policy)
        self.label_choose_y_kCrossValidation.setMinimumSize(QtCore.QSize(0, 60))
        self.label_choose_y_kCrossValidation.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_choose_y_kCrossValidation.setFont(font)
        self.label_choose_y_kCrossValidation.setObjectName("label_choose_y_kCrossValidation")
        self.verticalLayout_20.addWidget(self.label_choose_y_kCrossValidation)
        self.comboBox_y_kCrossValidation = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_y_kCrossValidation.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_y_kCrossValidation.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBox_y_kCrossValidation.setObjectName("comboBox_y_kCrossValidation")
        self.verticalLayout_20.addWidget(self.comboBox_y_kCrossValidation)
        self.label_num_k_kCrossValidation = QtWidgets.QLabel(self.tab_3)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_num_k_kCrossValidation.sizePolicy().hasHeightForWidth())
        self.label_num_k_kCrossValidation.setSizePolicy(size_policy)
        self.label_num_k_kCrossValidation.setMinimumSize(QtCore.QSize(0, 60))
        self.label_num_k_kCrossValidation.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_num_k_kCrossValidation.setFont(font)
        self.label_num_k_kCrossValidation.setObjectName("label_num_k_kCrossValidation")
        self.verticalLayout_20.addWidget(self.label_num_k_kCrossValidation)
        self.lineEdit_num_k_kCrossValidation = QtWidgets.QLineEdit(self.tab_3)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.lineEdit_num_k_kCrossValidation.sizePolicy().hasHeightForWidth())
        self.lineEdit_num_k_kCrossValidation.setSizePolicy(size_policy)
        self.lineEdit_num_k_kCrossValidation.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_num_k_kCrossValidation.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_num_k_kCrossValidation.setObjectName("lineEdit_num_k_kCrossValidation")
        self.verticalLayout_20.addWidget(self.lineEdit_num_k_kCrossValidation)
        self.btn_find_kCrossValidation = QtWidgets.QPushButton(self.tab_3)
        self.btn_find_kCrossValidation.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_find_kCrossValidation.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btn_find_kCrossValidation.setFont(font)
        self.btn_find_kCrossValidation.setStyleSheet(stl_btn)
        self.btn_find_kCrossValidation.setObjectName("btn_find_kCrossValidation")
        self.verticalLayout_20.addWidget(self.btn_find_kCrossValidation)
        self.horizontalLayout_10.addLayout(self.verticalLayout_20)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_3)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(size_policy)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.horizontalLayout_10.addWidget(self.tableWidget_2)
        self.tabWidget_kCrossValidation.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget(flags=QtCore.Qt.Widget)
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_mink_kCrossValidation = QtWidgets.QLabel(self.tab_4)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_mink_kCrossValidation.sizePolicy().hasHeightForWidth())
        self.label_mink_kCrossValidation.setSizePolicy(size_policy)
        self.label_mink_kCrossValidation.setMinimumSize(QtCore.QSize(0, 60))
        self.label_mink_kCrossValidation.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_mink_kCrossValidation.setFont(font)
        self.label_mink_kCrossValidation.setObjectName("label_mink_kCrossValidation")
        self.verticalLayout_21.addWidget(self.label_mink_kCrossValidation)
        self.lineEdit_mink_kCrossValidation = QtWidgets.QLineEdit(self.tab_4)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.lineEdit_mink_kCrossValidation.sizePolicy().hasHeightForWidth())
        self.lineEdit_mink_kCrossValidation.setSizePolicy(size_policy)
        self.lineEdit_mink_kCrossValidation.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_mink_kCrossValidation.setObjectName("lineEdit_mink_kCrossValidation")
        self.verticalLayout_21.addWidget(self.lineEdit_mink_kCrossValidation)
        self.label_max_k_kCrossValidation = QtWidgets.QLabel(self.tab_4)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_max_k_kCrossValidation.sizePolicy().hasHeightForWidth())
        self.label_max_k_kCrossValidation.setSizePolicy(size_policy)
        self.label_max_k_kCrossValidation.setMinimumSize(QtCore.QSize(0, 60))
        self.label_max_k_kCrossValidation.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_max_k_kCrossValidation.setFont(font)
        self.label_max_k_kCrossValidation.setObjectName("label_max_k_kCrossValidation")
        self.verticalLayout_21.addWidget(self.label_max_k_kCrossValidation)
        self.lineEdit_max_k_kCrossValidation = QtWidgets.QLineEdit(self.tab_4)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.lineEdit_max_k_kCrossValidation.sizePolicy().hasHeightForWidth())
        self.lineEdit_max_k_kCrossValidation.setSizePolicy(size_policy)
        self.lineEdit_max_k_kCrossValidation.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_max_k_kCrossValidation.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_max_k_kCrossValidation.setObjectName("lineEdit_max_k_kCrossValidation")
        self.verticalLayout_21.addWidget(self.lineEdit_max_k_kCrossValidation)
        self.label_method_kCrossValidation = QtWidgets.QLabel(self.tab_4)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_method_kCrossValidation.sizePolicy().hasHeightForWidth())
        self.label_method_kCrossValidation.setSizePolicy(size_policy)
        self.label_method_kCrossValidation.setMinimumSize(QtCore.QSize(0, 60))
        self.label_method_kCrossValidation.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_method_kCrossValidation.setFont(font)
        self.label_method_kCrossValidation.setObjectName("label_method_kCrossValidation")
        self.verticalLayout_21.addWidget(self.label_method_kCrossValidation)
        self.comboBox_method_kCrossValidation = QtWidgets.QComboBox(self.tab_4)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.comboBox_method_kCrossValidation.sizePolicy().hasHeightForWidth())
        self.comboBox_method_kCrossValidation.setSizePolicy(size_policy)
        self.comboBox_method_kCrossValidation.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_method_kCrossValidation.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBox_method_kCrossValidation.setObjectName("comboBox_method_kCrossValidation")
        self.comboBox_method_kCrossValidation.addItems(["Лінійна регресія", "KNN регресія"])
        self.verticalLayout_21.addWidget(self.comboBox_method_kCrossValidation)
        self.btn_find_best_kCrossValidation = QtWidgets.QPushButton(self.tab_4)
        self.btn_find_best_kCrossValidation.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_find_best_kCrossValidation.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btn_find_best_kCrossValidation.setFont(font)
        self.btn_find_best_kCrossValidation.setStyleSheet(stl_btn)
        self.btn_find_best_kCrossValidation.setObjectName("btn_find_best_kCrossValidation")
        self.verticalLayout_21.addWidget(self.btn_find_best_kCrossValidation)
        self.horizontalLayout_11.addLayout(self.verticalLayout_21)
        self.canvas_best_kCrossValidation = MplCanvas(self)
        self.horizontalLayout_11.addWidget(self.canvas_best_kCrossValidation)
        self.tabWidget_kCrossValidation.addTab(self.tab_4, "")
        self.verticalLayout_19.addWidget(self.tabWidget_kCrossValidation)
