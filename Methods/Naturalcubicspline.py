import numpy as np
from sklearn.model_selection import train_test_split
import patsy as pt
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
import seaborn as sns


class NaturalCubicSpline:
    def __init__(self, x, y):
        self._X = x.values.reshape(-1, 1)
        self._y = y.values
        self._rmse = 0
        self._X_train, self._X_test, self._y_train, self._y_test = train_test_split(self._X, self._y, test_size=0.3,
                                                                                    random_state=1)
        self._ncs = 0

    def natural_cubic_spline(self):
        transformed_x3 = pt.dmatrix("cr(train,df = 3)", {"train": self._X_train}, return_type='dataframe')

        self._ncs = sm.GLM(self._y_train, transformed_x3).fit()
        predict_test = self._ncs.predict(pt.dmatrix("cr(test, df=3)", {"test": self._X_test}, return_type='dataframe'))
        self._rmse = mean_squared_error(self._y_test, predict_test, squared=False)

    def plot_nat_cub(self, canvas_nat_cub):
        canvas_nat_cub.axes.cla()
        xp = np.linspace(self._X_test.min(), self._X_test.max(), 100)
        predict = self._ncs.predict(pt.dmatrix("cr(xp, df=3)", {"xp": xp}, return_type='dataframe'))
        sns.scatterplot(ax=canvas_nat_cub.axes, x=self._X_train.reshape(1, -1)[0], y=self._y_train)
        canvas_nat_cub.axes.plot(xp, predict, color='orange', label='Natural spline with df=3')
        canvas_nat_cub.draw()

    def rmse_value(self):
        return np.round(self._rmse, 4)
