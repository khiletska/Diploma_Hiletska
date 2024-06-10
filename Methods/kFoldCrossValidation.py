import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import LeaveOneOut


class KFoldCrossValidation:
    def __init__(self, x, y):
        self._X = 0
        self._y = 0
        self.check_x(x, y)
        self._means1, self._mins1, self._maxs1 = list(), list(), list()
        self._folds = []
        self._ideal = 0

    def check_x(self, x, y):
        if len(x.values.tolist()[0]) == 1:
            self._X = x.values.reshape(-1, 1)
            self._y = y.values
        else:
            self._X = x.values
            self._y = y.values

    def compare_methods(self, k):
        df = pd.DataFrame(columns=["Метод", "min", "середнє", "max"])
        cvk = KFold(n_splits=k, random_state=1, shuffle=True)
        model = LinearRegression()
        scores = cross_val_score(model, self._X, self._y, scoring='neg_mean_squared_error',
                                 cv=cvk, n_jobs=-1)
        scores = np.abs(scores)
        df.loc[len(df.index)] = ["Лінійна регресія", np.round(np.min(scores), 4), np.round(np.mean(scores), 4),
                                 np.round(np.max(scores), 4)]
        model2 = KNeighborsRegressor()
        scores2 = cross_val_score(model2, self._X, self._y, scoring='neg_mean_squared_error',
                                  cv=cvk, n_jobs=-1)
        scores2 = np.abs(scores2)
        df.loc[len(df.index)] = ["KNN регресія", np.round(np.min(scores2), 4), np.round(np.mean(scores2), 4),
                                 np.round(np.max(scores2), 4)]
        return df

    def find_best_k(self, mink, maxk, method):
        self._folds = range(mink, maxk + 1)
        model = 0
        if method == "Лінійна регресія":
            model = LinearRegression()
        elif method == "KNN регресія":
            model = KNeighborsRegressor()
        scores = cross_val_score(model, self._X, self._y, scoring='neg_mean_squared_error', cv=LeaveOneOut(), n_jobs=-1)
        scores = np.abs(scores)
        self._ideal = np.mean(scores)
        for k in self._folds:
            cv = KFold(n_splits=k, shuffle=True, random_state=1)
            scores1 = cross_val_score(model, self._X, self._y, scoring='neg_mean_squared_error', cv=cv, n_jobs=-1)
            scores1 = np.abs(scores1)
            k_mean = np.mean(scores1)
            k_min = np.min(scores1)
            k_max = np.max(scores1)
            self._means1.append(k_mean)
            self._mins1.append(k_mean - k_min)
            self._maxs1.append(k_max - k_mean)

    def plot_best(self, mink, maxk, method, canvas_best_kcrosvalid):
        canvas_best_kcrosvalid.axes.cla()
        self.find_best_k(mink, maxk, method)
        canvas_best_kcrosvalid.axes.errorbar(self._folds, self._means1, yerr=[self._mins1, self._maxs1], fmt='o')
        canvas_best_kcrosvalid.axes.plot(self._folds, [self._ideal for _ in range(len(self._folds))], color='r')
        canvas_best_kcrosvalid.draw()

    def x_value(self):
        return self._X
