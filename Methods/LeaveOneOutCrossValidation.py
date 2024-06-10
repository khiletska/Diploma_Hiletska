import pandas as pd
import numpy as np
from sklearn.model_selection import LeaveOneOut
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsRegressor


class LeaveOneOutCrossValidation:
    def __init__(self, x, y):
        self._X = 0
        self._y = 0
        self.check_x(x, y)

    def check_x(self, x, y):
        if len(x.values.tolist()[0]) == 1:
            self._X = x.values.reshape(-1, 1)
            self._y = y.values
        else:
            self._X = x.values
            self._y = y.values

    def compare_methods(self):
        df = pd.DataFrame(columns=["Метод", "min", "середнє", "max"])
        cv = LeaveOneOut()
        model = LinearRegression()
        scores = cross_val_score(model, self._X, self._y, scoring="neg_mean_squared_error",
                                 cv=cv, n_jobs=-1)
        scores = np.abs(scores)
        df.loc[len(df.index)] = ["Лінійна регресія", np.round(np.min(scores), 4), np.round(np.mean(scores), 4),
                                 np.round(np.max(scores), 4)]
        model2 = KNeighborsRegressor()
        scores2 = cross_val_score(model2, self._X, self._y, scoring='neg_mean_squared_error',
                                  cv=cv, n_jobs=-1)
        scores2 = np.abs(scores2)
        df.loc[len(df.index)] = ["KNN регресія", np.round(np.min(scores2), 4), np.round(np.mean(scores2), 4),
                                 np.round(np.max(scores2), 4)]
        return df

    def x_value(self):
        return self._X
