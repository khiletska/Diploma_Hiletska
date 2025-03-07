from PyQt5 import QtCore, QtGui, QtWidgets

from Interface.CheckCombobox import CheckCombobox
from Interface.MplCanvas import MplCanvas


class PageClassificationTree(QtWidgets.QWidget):
    def __init__(self, stl_btn, font):
        super().__init__()
        self.setObjectName("page_14")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout()
        self.verticalLayout_38.setObjectName("verticalLayout_38")

        self.label_best_parameters_cl_tree = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_best_parameters_cl_tree.sizePolicy().hasHeightForWidth())
        self.label_best_parameters_cl_tree.setSizePolicy(size_policy)
        self.label_best_parameters_cl_tree.setMinimumSize(QtCore.QSize(0, 60))
        self.label_best_parameters_cl_tree.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_best_parameters_cl_tree.setFont(font)
        self.label_best_parameters_cl_tree.setObjectName("label_best_parameters_cl_tree")
        self.verticalLayout_38.addWidget(self.label_best_parameters_cl_tree)

        self.label_x_cl_tree = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_x_cl_tree.sizePolicy().hasHeightForWidth())
        self.label_x_cl_tree.setSizePolicy(size_policy)
        self.label_x_cl_tree.setMinimumSize(QtCore.QSize(0, 60))
        self.label_x_cl_tree.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_x_cl_tree.setFont(font)
        self.label_x_cl_tree.setObjectName("label_x_cl_tree")
        self.verticalLayout_38.addWidget(self.label_x_cl_tree)
        self.combobox_x_cl_tree = CheckCombobox()
        self.verticalLayout_38.addWidget(self.combobox_x_cl_tree)
        self.label_chosen_x_cl_tree = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_chosen_x_cl_tree.sizePolicy().hasHeightForWidth())
        self.label_chosen_x_cl_tree.setSizePolicy(size_policy)
        self.label_chosen_x_cl_tree.setMinimumSize(QtCore.QSize(0, 30))
        self.label_chosen_x_cl_tree.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_chosen_x_cl_tree.setFont(font)
        self.label_chosen_x_cl_tree.setObjectName("label_x_cl_tree_choose")
        self.verticalLayout_38.addWidget(self.label_chosen_x_cl_tree)
        self.label_y_cl_tree = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_y_cl_tree.sizePolicy().hasHeightForWidth())
        self.label_y_cl_tree.setSizePolicy(size_policy)
        self.label_y_cl_tree.setMinimumSize(QtCore.QSize(0, 30))
        self.label_y_cl_tree.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_y_cl_tree.setFont(font)
        self.label_y_cl_tree.setObjectName("label_y_cl_tree")
        self.verticalLayout_38.addWidget(self.label_y_cl_tree)
        self.comboBox_y_cl_tree = QtWidgets.QComboBox(self)
        self.comboBox_y_cl_tree.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_y_cl_tree.setMaximumSize(QtCore.QSize(16777215, 30))
        self.comboBox_y_cl_tree.setObjectName("comboBox_y_cl_tree")

        self.verticalLayout_38.addWidget(self.comboBox_y_cl_tree)

        self.label_cl_tree_depth = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_cl_tree_depth.sizePolicy().hasHeightForWidth())
        self.label_cl_tree_depth.setSizePolicy(size_policy)
        self.label_cl_tree_depth.setMinimumSize(QtCore.QSize(0, 30))
        self.label_cl_tree_depth.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_cl_tree_depth.setFont(font)
        self.label_cl_tree_depth.setObjectName("label_cl_tree_depth")
        self.verticalLayout_38.addWidget(self.label_cl_tree_depth)
        self.lineEdit_depth_cl_tree = QtWidgets.QLineEdit(self)
        self.lineEdit_depth_cl_tree.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_depth_cl_tree.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_depth_cl_tree.setObjectName("lineEdit_depth_cl_tree")
        self.verticalLayout_38.addWidget(self.lineEdit_depth_cl_tree)

        self.label_cl_tree_split = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_cl_tree_split.sizePolicy().hasHeightForWidth())
        self.label_cl_tree_split.setSizePolicy(size_policy)
        self.label_cl_tree_split.setMinimumSize(QtCore.QSize(0, 30))
        self.label_cl_tree_split.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_cl_tree_split.setFont(font)
        self.label_cl_tree_split.setObjectName("label_cl_tree_split")
        self.verticalLayout_38.addWidget(self.label_cl_tree_split)
        self.lineEdit_cl_tree_split = QtWidgets.QLineEdit(self)
        self.lineEdit_cl_tree_split.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_cl_tree_split.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_cl_tree_split.setObjectName("lineEdit_cl_tree_split")
        self.verticalLayout_38.addWidget(self.lineEdit_cl_tree_split)

        self.label_cl_tree_leaf = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_cl_tree_leaf.sizePolicy().hasHeightForWidth())
        self.label_cl_tree_leaf.setSizePolicy(size_policy)
        self.label_cl_tree_leaf.setMinimumSize(QtCore.QSize(0, 30))
        self.label_cl_tree_leaf.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_cl_tree_leaf.setFont(font)
        self.label_cl_tree_leaf.setObjectName("label_cl_tree_leaf")
        self.verticalLayout_38.addWidget(self.label_cl_tree_leaf)
        self.lineEdit_cl_tree_leaf = QtWidgets.QLineEdit(self)
        self.lineEdit_cl_tree_leaf.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_cl_tree_leaf.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_cl_tree_leaf.setObjectName("lineEdit_cl_tree_leaf")
        self.verticalLayout_38.addWidget(self.lineEdit_cl_tree_leaf)

        self.label_predict_cl_tree = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_predict_cl_tree.sizePolicy().hasHeightForWidth())
        self.label_predict_cl_tree.setSizePolicy(size_policy)
        self.label_predict_cl_tree.setMinimumSize(QtCore.QSize(0, 30))
        self.label_predict_cl_tree.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_predict_cl_tree.setFont(font)
        self.label_predict_cl_tree.setObjectName("label_predict_cl_tree")
        self.verticalLayout_38.addWidget(self.label_predict_cl_tree)
        self.lineEdit_x_cl_tree = QtWidgets.QLineEdit(self)
        self.lineEdit_x_cl_tree.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_x_cl_tree.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_x_cl_tree.setObjectName("lineEdit_x_cl_tree")
        self.verticalLayout_38.addWidget(self.lineEdit_x_cl_tree)
        self.result_predict_cl_tree = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.result_predict_cl_tree.sizePolicy().hasHeightForWidth())
        self.result_predict_cl_tree.setSizePolicy(size_policy)
        self.result_predict_cl_tree.setMinimumSize(QtCore.QSize(0, 30))
        self.result_predict_cl_tree.setMaximumSize(QtCore.QSize(16777215, 30))
        self.result_predict_cl_tree.setFont(font)
        self.result_predict_cl_tree.setObjectName("result_cl_tree")
        self.verticalLayout_38.addWidget(self.result_predict_cl_tree)
        self.btn_predict_cl_tree = QtWidgets.QPushButton(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.btn_predict_cl_tree.sizePolicy().hasHeightForWidth())
        self.btn_predict_cl_tree.setSizePolicy(size_policy)
        self.btn_predict_cl_tree.setMinimumSize(QtCore.QSize(200, 50))
        self.btn_predict_cl_tree.setMaximumSize(QtCore.QSize(200, 50))
        self.btn_predict_cl_tree.setFont(font)
        self.btn_predict_cl_tree.setStyleSheet(stl_btn)
        self.btn_predict_cl_tree.setObjectName("btn_predict_cl_tree")
        self.verticalLayout_38.addWidget(self.btn_predict_cl_tree)
        self.line_7 = QtWidgets.QFrame(self, flags=QtCore.Qt.Widget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_38.addWidget(self.line_7)
        self.result_cl_tree_text = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.result_cl_tree_text.sizePolicy().hasHeightForWidth())
        self.result_cl_tree_text.setSizePolicy(size_policy)
        self.result_cl_tree_text.setMinimumSize(QtCore.QSize(0, 30))
        self.result_cl_tree_text.setMaximumSize(QtCore.QSize(16777215, 30))
        self.result_cl_tree_text.setFont(font)
        self.result_cl_tree_text.setObjectName("result_predict_cl_tree_text")
        self.verticalLayout_38.addWidget(self.result_cl_tree_text)
        self.line_8 = QtWidgets.QFrame(self, flags=QtCore.Qt.Widget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_38.addWidget(self.line_8)
        self.report_cl_tree = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.report_cl_tree.sizePolicy().hasHeightForWidth())
        self.report_cl_tree.setSizePolicy(size_policy)
        self.report_cl_tree.setMinimumSize(QtCore.QSize(0, 30))
        self.report_cl_tree.setMaximumSize(QtCore.QSize(16777215, 30))
        self.report_cl_tree.setFont(font)
        self.report_cl_tree.setObjectName("report_cl_tree")
        self.verticalLayout_38.addWidget(self.report_cl_tree)
        self.horizontalLayout_35.addLayout(self.verticalLayout_38)

        self.verticalLayout_39 = QtWidgets.QVBoxLayout()
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.canvas_cl_tree = MplCanvas(self)
        self.verticalLayout_39.addWidget(self.canvas_cl_tree)
        self.canvas_cl_tree_matrix = MplCanvas(self)
        self.verticalLayout_39.addWidget(self.canvas_cl_tree_matrix)
        self.horizontalLayout_35.addLayout(self.verticalLayout_39)
