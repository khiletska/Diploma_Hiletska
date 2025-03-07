from PyQt5 import QtCore, QtWidgets


class PageNormalDistribution(QtWidgets.QWidget):
    def __init__(self, stl_btn, font):
        super().__init__()
        self.setObjectName("page_normal")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.n_label = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.n_label.sizePolicy().hasHeightForWidth())
        self.n_label.setSizePolicy(size_policy)
        self.n_label.setMinimumSize(QtCore.QSize(0, 30))
        self.n_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.n_label.setFont(font)
        self.n_label.setObjectName("n_label")
        self.verticalLayout_6.addWidget(self.n_label)
        self.lineedit_n = QtWidgets.QLineEdit(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.lineedit_n.sizePolicy().hasHeightForWidth())
        self.lineedit_n.setSizePolicy(size_policy)
        self.lineedit_n.setObjectName("lin_reg_predict")
        self.verticalLayout_6.addWidget(self.lineedit_n)

        self.mu_x_label = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.mu_x_label.sizePolicy().hasHeightForWidth())
        self.mu_x_label.setSizePolicy(size_policy)
        self.mu_x_label.setMinimumSize(QtCore.QSize(0, 30))
        self.mu_x_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.mu_x_label.setFont(font)
        self.mu_x_label.setObjectName("mu_label")
        self.verticalLayout_6.addWidget(self.mu_x_label)
        self.lineedit_mu_x = QtWidgets.QLineEdit(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.lineedit_mu_x.sizePolicy().hasHeightForWidth())
        self.lineedit_mu_x.setSizePolicy(size_policy)
        self.lineedit_mu_x.setObjectName("lineedit_mu_x")
        self.verticalLayout_6.addWidget(self.lineedit_mu_x)

        self.sigma_x_label = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sigma_x_label.sizePolicy().hasHeightForWidth())
        self.sigma_x_label.setSizePolicy(size_policy)
        self.sigma_x_label.setMinimumSize(QtCore.QSize(0, 30))
        self.sigma_x_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.sigma_x_label.setFont(font)
        self.sigma_x_label.setObjectName("mu_label")
        self.verticalLayout_6.addWidget(self.sigma_x_label)
        self.lineedit_sigma_x = QtWidgets.QLineEdit(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.lineedit_sigma_x.sizePolicy().hasHeightForWidth())
        self.lineedit_sigma_x.setSizePolicy(size_policy)
        self.lineedit_sigma_x.setObjectName("lineedit_mu_x")
        self.verticalLayout_6.addWidget(self.lineedit_sigma_x)

        self.mu_y_label = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.mu_y_label.sizePolicy().hasHeightForWidth())
        self.mu_y_label.setSizePolicy(size_policy)
        self.mu_y_label.setMinimumSize(QtCore.QSize(0, 30))
        self.mu_y_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.mu_y_label.setFont(font)
        self.mu_y_label.setObjectName("mu_y_label")
        self.verticalLayout_6.addWidget(self.mu_y_label)
        self.lineedit_mu_y = QtWidgets.QLineEdit(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.lineedit_mu_y.sizePolicy().hasHeightForWidth())
        self.lineedit_mu_y.setSizePolicy(size_policy)
        self.lineedit_mu_y.setObjectName("lineedit_mu_x")
        self.verticalLayout_6.addWidget(self.lineedit_mu_y)

        self.sigma_y_label = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sigma_y_label.sizePolicy().hasHeightForWidth())
        self.sigma_y_label.setSizePolicy(size_policy)
        self.sigma_y_label.setMinimumSize(QtCore.QSize(0, 30))
        self.sigma_y_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.sigma_y_label.setFont(font)
        self.sigma_y_label.setObjectName("mu_y_label")
        self.verticalLayout_6.addWidget(self.sigma_y_label)
        self.lineedit_sigma_y = QtWidgets.QLineEdit(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.lineedit_sigma_y.sizePolicy().hasHeightForWidth())
        self.lineedit_sigma_y.setSizePolicy(size_policy)
        self.lineedit_sigma_y.setObjectName("lineedit_mu_x")
        self.verticalLayout_6.addWidget(self.lineedit_sigma_y)

        self.random_checked = QtWidgets.QCheckBox(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.random_checked.sizePolicy().hasHeightForWidth())
        self.random_checked.setSizePolicy(size_policy)
        self.random_checked.setMinimumSize(QtCore.QSize(0, 30))
        self.random_checked.setMaximumSize(QtCore.QSize(16777215, 30))
        self.random_checked.setFont(font)
        self.random_checked.setObjectName("mu_y_label")
        self.verticalLayout_6.addWidget(self.random_checked)

        self.generate_btn = QtWidgets.QPushButton(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.generate_btn.sizePolicy().hasHeightForWidth())
        self.generate_btn.setSizePolicy(size_policy)
        self.generate_btn.setMinimumSize(QtCore.QSize(120, 50))
        self.generate_btn.setMaximumSize(QtCore.QSize(120, 50))
        self.generate_btn.setFont(font)
        self.generate_btn.setStyleSheet(stl_btn)
        self.generate_btn.setObjectName("generate_btn")
        self.verticalLayout_6.addWidget(self.generate_btn)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        # self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.tableWidget_2 = QtWidgets.QTableWidget(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(size_policy)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.verticalLayout_7.addWidget(self.tableWidget_2)
        self.save_btn = QtWidgets.QPushButton(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(size_policy)
        self.save_btn.setMinimumSize(QtCore.QSize(280, 50))
        self.save_btn.setMaximumSize(QtCore.QSize(280, 50))
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet(stl_btn)
        self.save_btn.setObjectName("generate_btn")
        self.verticalLayout_7.addWidget(self.save_btn)
        self.analise_btn = QtWidgets.QPushButton(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.analise_btn.sizePolicy().hasHeightForWidth())
        self.analise_btn.setSizePolicy(size_policy)
        self.analise_btn.setMinimumSize(QtCore.QSize(280, 50))
        self.analise_btn.setMaximumSize(QtCore.QSize(280, 50))
        self.analise_btn.setFont(font)
        self.analise_btn.setStyleSheet(stl_btn)
        self.analise_btn.setObjectName("generate_btn")
        self.verticalLayout_7.addWidget(self.analise_btn)
        self.horizontalLayout_3.addLayout( self.verticalLayout_7)
        self.df = None







