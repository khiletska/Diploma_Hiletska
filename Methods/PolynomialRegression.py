import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import seaborn as sns


class PolynomialRegression:
    def __init__(self, x, y):
        self._X = x.values.reshape(-1, 1)
        self._y = y.values
        self._rmse = 0
        self._X_train, self._X_test, self._y_train, self._y_test = train_test_split(self._X, self._y, test_size=0.3,
                                                                                    random_state=1)
        self._pm = 0

    def fit_data(self, degree):
        poly = PolynomialFeatures(degree)
        x_train_poly = poly.fit_transform(self._X_train)
        x_test_poly = poly.fit_transform(self._X_test)
        return x_test_poly, x_train_poly

    def polynomial_regression(self, degree):
        self._pm = linear_model.LinearRegression()
        x_test_poly, x_train_poly = self.fit_data(degree)
        self._pm.fit(x_train_poly, self._y_train)
        predict_test = self._pm.predict(x_test_poly)
        self._rmse = mean_squared_error(self._y_test,
                                        predict_test,
                                        squared=False)

    def predict_regression(self, arr, degree):
        poly = PolynomialFeatures(degree)
        arr = poly.fit_transform(arr)
        r = self._pm.predict(arr)
        return np.round(r[0], 4)

    def plot_poly(self, canvas_poly_regression, degree):
        canvas_poly_regression.axes.cla()
        sns.regplot(ax=canvas_poly_regression.axes, x=self._X_train,
                    y=self._y_train,
                    ci=None,
                    order=degree,
                    line_kws={"color": "orange"})
        canvas_poly_regression.draw()

    def rmse_value(self):
        return np.round(self._rmse, 4)
