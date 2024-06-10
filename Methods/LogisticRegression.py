import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix


class MyLogisticRegression:
    def __init__(self, x, y):
        self._X = 0
        self._y = 0
        self.check_x(x, y)
        self.check_y()
        self._X_train, self._X_test, self._y_train, self._y_test = train_test_split(self._X, self._y, test_size=0.6,
                                                                                    random_state=45)
        self._b0 = 0
        self._coefficients = []
        self._report = 0
        self._y_predict = 0

    def check_x(self, x, y):
        if len(x.values.tolist()[0]) == 1:
            self._X = x.values.reshape(-1, 1)
            self._y = y.values
        else:
            self._X = x.values
            self._y = y.values

    def check_y(self):
        if any(element in 'No' for element in self._y):
            self._y = list(map(lambda x: x.replace('No', "0"), self._y))
            self._y = list(map(lambda x: x.replace('Yes', "1"), self._y))
            self._y = list(map(lambda x: int(x), self._y))
        elif any(element in 'T' for element in self._y):
            self._y = list(map(lambda x: x.replace('F', "0"), self._y))
            self._y = list(map(lambda x: x.replace('T', "1"), self._y))
            self._y = list(map(lambda x: int(x), self._y))
        else:
            self._y = list(map(lambda x: int(x), self._y))

    def plot_barchart(self, canvas_logistic_regression):
        canvas_logistic_regression.axes.cla()
        co, num = np.unique(self._y, return_counts=True)
        canvas_logistic_regression.axes.bar(co, num, color="Green")
        count_no_sub = num[0]
        count_sub = num[1]
        pct_of_no_sub = count_no_sub / (count_no_sub + count_sub)
        pct_of_sub = count_sub / (count_no_sub + count_sub)
        canvas_logistic_regression.figure.suptitle(
            f"Відсоток {co[0]} - {np.round(pct_of_no_sub * 100, 4)}%;"
            f"Відсоток {co[1]}-{np.round(pct_of_sub * 100, 2)}%")
        canvas_logistic_regression.draw()

    def logistic_regression(self):

        classifier = LogisticRegression()

        classifier.fit(self._X_train, self._y_train)

        self._y_predict = classifier.predict(self._X_test)

        self._b0 = classifier.intercept_

        self._coefficients = classifier.coef_

        report = classification_report(self._y_test, self._y_predict)

        self._report = report
        return classifier

    def predict(self, arr):
        result = self.logistic_regression().predict(arr)
        return result

    def plot_matrix(self, canvas_logistic_matrix):
        canvas_logistic_matrix.axes.cla()
        conf_matrix = confusion_matrix(y_true=self._y_test, y_pred=self._y_predict)
        canvas_logistic_matrix.axes.matshow(conf_matrix, alpha=0.3)
        for i in range(conf_matrix.shape[0]):
            for j in range(conf_matrix.shape[1]):
                canvas_logistic_matrix.axes.text(x=j, y=i, s=conf_matrix[i, j], va='center',
                                                 ha='center', size='xx-large')
        canvas_logistic_matrix.figure.suptitle('Матриця невідповідностей')
        canvas_logistic_matrix.draw()

    def b0_value(self):
        return np.round(self._b0[0], 4)

    def coefficients_value(self):
        res = ''
        print(self._coefficients[0][1])
        for i in range(1, len(self._coefficients[0]) + 1):
            res = res + f"b{i}={np.round(self._coefficients[0][i - 1],4)} \n"
        return res

    def report_value(self):
        return self._report

    def x_value(self):
        return self._X

    def y_value(self):
        return self._y
