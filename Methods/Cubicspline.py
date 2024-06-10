import numpy as np
from sklearn.model_selection import train_test_split
import patsy as pt
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
import seaborn as sns


class CubicSpline:
    def __init__(self, x, y):
        self._X = x.values.reshape(-1, 1)
        self._y = y.values
        self._rmse = 0
        self._X_train, self._X_test, self._y_train, self._y_test = train_test_split(self._X, self._y, test_size=0.5,
                                                                                    random_state=1)
        self._cs = 0

    def cubic_spline(self):
        k = np.max(self._X_train) - np.min(self._X_train)
        km = np.min(self._X_train)
        k1 = km + 0.25 * k
        k2 = km + 0.5 * k
        k3 = km + 0.75 * k
        transformed_x = pt.dmatrix(
            "bs(train, knots=(k1,k2,k3), degree=3, include_intercept=False)",
            {"k1": k1, "k2": k2, "k3": k3, "train": self._X_train}, return_type='dataframe')
        self._cs = sm.GLM(self._y_train, transformed_x).fit()
        k_test = np.max(self._X_test) - np.min(self._X_test)
        km_test = np.min(self._X_test)
        k1_test = km_test + 0.25 * k_test
        k2_test = km_test + 0.5 * k_test
        k3_test = km_test + 0.75 * k_test
        pred_test = self._cs.predict(
            pt.dmatrix("bs(test, knots=(k1,k2,k3), include_intercept=False)",
                       {"k1": k1_test, "k2": k2_test, "k3": k3_test, "test": self._X_test}, return_type='dataframe'))
        self._rmse = mean_squared_error(self._y_test, pred_test, squared=False)

    def plot_cubspl(self, canvas_cubspl):
        canvas_cubspl.axes.cla()
        xp = np.linspace(self._X_test.min(), self._X_test.max(), 100)
        k_test = np.max(self._X_test) - np.min(self._X_test)
        km_test = np.min(self._X_test)
        k1_test = km_test + 0.25 * k_test
        k2_test = km_test + 0.5 * k_test
        k3_test = km_test + 0.75 * k_test
        pred = self._cs.predict(
            pt.dmatrix("bs(xp, knots=(k1,k2,k3), include_intercept=False)",
                       {"k1": k1_test, "k2": k2_test, "k3": k3_test, "xp": xp}, return_type='dataframe'))
        sns.scatterplot(ax=canvas_cubspl.axes, x=self._X_train.reshape(1, -1)[0], y=self._y_train)
        canvas_cubspl.axes.plot(xp, pred, label='Cubic spline with degree=3 (3 knots)', color='orange')
        canvas_cubspl.draw()

    def rmse_value(self):
        return np.round(self._rmse, 4)
