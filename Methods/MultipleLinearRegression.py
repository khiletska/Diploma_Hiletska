import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


class MultipleLinearRegression:
    def __init__(self, x, y):
        self._X = x.values
        self._y = y.values
        self._b1 = 0
        self._b0 = 0

        self._r2 = 0
        self._x_test = []
        self._regression = 0

    def linear_regression(self):
        regression = linear_model.LinearRegression()
        x_train, x_test, y_train, y_test = train_test_split(self._X, self._y, test_size=0.2, random_state=45)
        regression.fit(x_train, y_train)
        y_predict = regression.predict(x_test)
        self._b1 = regression.coef_
        self._b0 = regression.intercept_
        self._r2 = r2_score(y_test, y_predict)
        self._x_test = x_test
        return regression

    def predict(self, arr):
        result = self.linear_regression().predict(arr)
        return result

    def b0_value(self):
        return np.round(self._b0, 4)

    def equation(self):
        str_res = f'y={np.round(self._b0, 4)}'
        for i in range(len(self._b1)):
            str_res += f'+{np.round(self._b1[i], 4)}*x{i}'
        return str_res

    def r2_value(self):
        return np.round(self._r2, 4)
