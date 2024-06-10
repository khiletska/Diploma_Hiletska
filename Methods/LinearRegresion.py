from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


class LinearRegression:
    def __init__(self, x, y):
        self._X = x.values.reshape(-1, 1)
        self._y = y.values.reshape(-1, 1)
        self._b1 = 0
        self._b0 = 0
        self._mse = 0
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
        self._mse = mean_squared_error(y_test, y_predict)
        self._r2 = r2_score(y_test, y_predict)
        self._x_test = x_test
        return regression

    def predict(self, arr):
        result = self.linear_regression().predict(arr)
        return result

    def plot(self, canvas1):
        canvas1.axes.cla()
        canvas1.axes.scatter(self._X, self._y, color="green",
                             marker="*")
        y_predict = self.linear_regression().predict(self._x_test)
        canvas1.axes.plot(self._x_test, y_predict, color="blue", linewidth=3)
        canvas1.draw()

    def b0_value(self):
        return np.round(self._b0[0], 4)

    def b1_value(self):
        return np.round(self._b1[0][0], 4)

    def mse_value(self):
        return np.round(self._mse, 4)

    def r2_value(self):
        return np.round(self._r2, 4)
