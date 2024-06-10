from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np


class KNNRegression:
    def __init__(self, x, y):
        self._X = x.values
        self._y = y.values
        self._mae = 0
        self._mse = 0
        self._rmse = 0
        self._r2 = 0

        self._best_r2 = 0
        self._best_mae = 0
        self._best_mse = 0
        self._best_rmse = 0
        self._X_train, self._X_test, self._y_train, self._y_test = train_test_split(self._X, self._y, test_size=0.2,
                                                                                    random_state=45)

    def knn_regression(self, k):
        knn_reg = KNeighborsRegressor(n_neighbors=k)
        knn_reg.fit(self._X_train, self._y_train)
        y_predict = knn_reg.predict(self._X_test)
        self._mae = mean_absolute_error(self._y_test, y_predict)
        self._mse = mean_squared_error(self._y_test, y_predict)
        self._rmse = mean_squared_error(self._y_test, y_predict, squared=False)
        self._r2 = knn_reg.score(self._X_test, self._y_test)
        return knn_reg

    def predict(self, arr, k):
        result = self.knn_regression(k).predict(arr)
        return result

    def analyze_num_neigh(self, min_val, max_val):
        error = []
        for i in range(min_val, max_val + 1):
            knn = KNeighborsRegressor(n_neighbors=i)
            knn.fit(self._X_train, self._y_train)
            predict_i = knn.predict(self._X_test)
            mae = mean_absolute_error(self._y_test, predict_i)
            error.append(mae)
        return error

    def plot_knn(self, min_val, max_val, canvas_knn_regression):
        error = self.analyze_num_neigh(min_val, max_val)
        canvas_knn_regression.axes.cla()
        canvas_knn_regression.axes.plot(range(min_val, max_val + 1), error, color='red',
                                        linestyle='dashed', marker='o',
                                        markerfacecolor='blue', markersize=10)
        canvas_knn_regression.figure.suptitle('Залежність MAE від k')
        canvas_knn_regression.draw()

    def find_best_k(self, min_val, max_val):
        error = self.analyze_num_neigh(min_val, max_val)
        min_er = min(error)
        best_k = np.array(error).argmin() + min_val
        return min_er, best_k

    def find_best_values(self, min_val, max_val):
        min_er, k_best = self.find_best_k(min_val, max_val)
        knn_reg12 = KNeighborsRegressor(n_neighbors=k_best)
        knn_reg12.fit(self._X_train, self._y_train)
        y_predict12 = knn_reg12.predict(self._X_test)
        self._best_r2 = knn_reg12.score(self._X_test, self._y_test)
        self._best_mae = mean_absolute_error(self._y_test, y_predict12)
        self._best_mse = mean_squared_error(self._y_test, y_predict12)
        self._best_rmse = mean_squared_error(self._y_test, y_predict12, squared=False)

    def mae_value(self):
        return np.round(self._mae, 4)

    def rmse_value(self):
        return np.round(self._rmse, 4)

    def mse_value(self):
        return np.round(self._mse, 4)

    def r2_value(self):
        return np.round(self._r2, 4)

    def best_mae_value(self):
        return np.round(self._best_mae, 4)

    def best_rmse_value(self):
        return np.round(self._best_rmse, 4)

    def best_mse_value(self):
        return np.round(self._best_mse, 4)

    def best_r2_value(self):
        return np.round(self._best_r2, 4)
