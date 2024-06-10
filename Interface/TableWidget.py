from PyQt5.QtWidgets import QTableWidgetItem


class TableWidget:
    @staticmethod
    def set(widget, df):
        widget.setStyleSheet("font-size:35px;")
        n_rows, n_cols = df.shape
        widget.setColumnCount(n_cols)
        widget.setRowCount(n_rows)
        widget.setHorizontalHeaderLabels(df.columns.values.tolist())
        for i in range(widget.rowCount()):
            for j in range(widget.columnCount()):
                widget.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))
