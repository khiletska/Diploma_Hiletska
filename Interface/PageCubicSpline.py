from PyQt5 import QtCore, QtWidgets

from Interface.MplCanvas import MplCanvas


class PageCubicSpline(QtWidgets.QWidget):
    def __init__(self, stl_btn, font):
        super().__init__()
        self.setObjectName("page_9")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_choose_x_CubicSpline = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_choose_x_CubicSpline.sizePolicy().hasHeightForWidth())
        self.label_choose_x_CubicSpline.setSizePolicy(size_policy)
        self.label_choose_x_CubicSpline.setMinimumSize(QtCore.QSize(0, 60))
        self.label_choose_x_CubicSpline.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_choose_x_CubicSpline.setFont(font)
        self.label_choose_x_CubicSpline.setObjectName("label_choose_x_CubicSpline")
        self.verticalLayout_23.addWidget(self.label_choose_x_CubicSpline)
        self.comboBox_x_CubicSpline = QtWidgets.QComboBox(self)
        self.comboBox_x_CubicSpline.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_x_CubicSpline.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBox_x_CubicSpline.setObjectName("comboBox_x_CubicSpline")

        self.verticalLayout_23.addWidget(self.comboBox_x_CubicSpline)
        self.label_choose_y_CubicSpline = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_choose_y_CubicSpline.sizePolicy().hasHeightForWidth())
        self.label_choose_y_CubicSpline.setSizePolicy(size_policy)
        self.label_choose_y_CubicSpline.setMinimumSize(QtCore.QSize(0, 60))
        self.label_choose_y_CubicSpline.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_choose_y_CubicSpline.setFont(font)
        self.label_choose_y_CubicSpline.setObjectName("label_choose_y_CubicSpline")
        self.verticalLayout_23.addWidget(self.label_choose_y_CubicSpline)
        self.comboBox_y_CubicSpline = QtWidgets.QComboBox(self)
        self.comboBox_y_CubicSpline.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_y_CubicSpline.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBox_y_CubicSpline.setObjectName("comboBox_y_CubicSpline")

        self.verticalLayout_23.addWidget(self.comboBox_y_CubicSpline)
        # self.label_data_predict_CubicSpline = QtWidgets.QLabel(self)
        # size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        # size_policy.setHorizontalStretch(0)
        # size_policy.setVerticalStretch(0)
        # size_policy.setHeightForWidth(self.label_data_predict_CubicSpline.sizePolicy().hasHeightForWidth())
        # self.label_data_predict_CubicSpline.setSizePolicy(size_policy)
        # self.label_data_predict_CubicSpline.setMinimumSize(QtCore.QSize(0, 60))
        # self.label_data_predict_CubicSpline.setMaximumSize(QtCore.QSize(16777215, 60))
        # self.label_data_predict_CubicSpline.setFont(font)
        # self.label_data_predict_CubicSpline.setObjectName("label_data_predict_CubicSpline")
        # self.verticalLayout_23.addWidget(self.label_data_predict_CubicSpline)
        self.btn_predict_CubicSpline = QtWidgets.QPushButton(self)
        self.btn_predict_CubicSpline.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_predict_CubicSpline.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btn_predict_CubicSpline.setFont(font)
        self.btn_predict_CubicSpline.setStyleSheet(stl_btn)
        self.btn_predict_CubicSpline.setObjectName("btn_predict_CubicSpline")
        self.verticalLayout_23.addWidget(self.btn_predict_CubicSpline)
        self.label_rmse_CubicSpline = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_rmse_CubicSpline.sizePolicy().hasHeightForWidth())
        self.label_rmse_CubicSpline.setSizePolicy(size_policy)
        self.label_rmse_CubicSpline.setMinimumSize(QtCore.QSize(0, 60))
        self.label_rmse_CubicSpline.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_rmse_CubicSpline.setFont(font)
        self.label_rmse_CubicSpline.setObjectName("label_rmse_CubicSpline")
        self.verticalLayout_23.addWidget(self.label_rmse_CubicSpline)
        self.horizontalLayout_13.addLayout(self.verticalLayout_23)
        self.canvas_CubicSpline = MplCanvas(self)
        self.horizontalLayout_13.addWidget(self.canvas_CubicSpline)
