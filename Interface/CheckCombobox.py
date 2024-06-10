from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QComboBox
from PyQt5 import QtCore


class CheckCombobox(QComboBox):

    def __init__(self):
        super(CheckCombobox, self).__init__()
        self.view().pressed.connect(self.handle_item_pressed)
        self.setModel(QStandardItemModel(self))
        self.setMinimumSize(QtCore.QSize(0, 30))
        self.setMaximumSize(QtCore.QSize(16777215, 30))

    def handle_item_pressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)
        self.check_items()

    def item_checked(self, index):
        item = self.model().item(index, 0)
        return item.checkState() == Qt.Checked

    def check_items(self):
        checked_items = []
        for i in range(self.count()):
            if self.item_checked(i):
                checked_items.append(i)
        return checked_items

    def text(self):
        item_list = self.check_items()
        checked = ""
        for i in item_list:
            text_label = self.model().item(i, 0).text()
            checked = checked + "," + text_label
        return checked
