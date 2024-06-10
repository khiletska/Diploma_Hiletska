from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np


class RidgeRegression:
    def __init__(self, x, y):
        self._X = x.values
        self._y = y.values
        self._mse = 0
        self._X_train, self._X_test, self._y_train, self._y_test = train_test_split(self._X, self._y, test_size=0.2,
                                                                                    random_state=42)
        self._y_predict = None
        self._y_predict_best = None
        self._best_alpha = 0
        self._best_mse = 0
        self._mean_test_scores = None

    # Function to perform Ridge regression with pipeline and cross-validation
    def perform_ridge_regression(self, alpha=1.0):
        pipeline = make_pipeline(StandardScaler(), Ridge(alpha=alpha))
        pipeline.fit(self._X_train, self._y_train)
        self._y_predict = pipeline.predict(self._X_test)
        self._mse = mean_squared_error(self._y_test, self._y_predict)
        return pipeline

    def plot_ridge(self, canvas):
        canvas.axes.cla()
        canvas.axes.scatter(self._y_test, self._y_predict, alpha=0.5)

        # Add title and labels
        canvas.axes.set_title("Прогнозовані та актуальні дані")
        canvas.axes.set_xlabel("Актуальні дані")
        canvas.axes.set_ylabel("Прогнозовані дані")

        canvas.axes.plot([self._y_test.min(), self._y_test.max()], [self._y_test.min(), self._y_test.max()],
                         'r--')  # Reference line

        canvas.draw()

    def mse_value(self):
        return np.round(self._mse, 4)

    def predict_ridge(self, arr, alpha=1.0):
        result = self.perform_ridge_regression(alpha).predict(arr)
        return result

    def find_best_alpha(self, mina, max_a):
        pipeline = make_pipeline(StandardScaler(), Ridge())

        # Define the grid of alpha values to search
        # alpha_values = np.logspace(mina, max_a, 50)
        alpha_values = np.arange(mina, max_a, 0.1)
        param_grid = {'ridge__alpha': alpha_values}

        # Setting up GridSearchCV
        grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)

        grid_search.fit(self._X_train, self._y_train)

        best_model = grid_search.best_estimator_
        self._best_alpha = grid_search.best_params_['ridge__alpha']

        # Making predictions
        self._y_predict_best = best_model.predict(self._X_test)

        # Calculating mean squared error
        self._best_mse = mean_squared_error(self._y_test, self._y_predict_best)
        self._mean_test_scores = -grid_search.cv_results_['mean_test_score']

    def plot_res_best_alpha(self, canvas_best):
        canvas_best.axes.cla()
        canvas_best.axes.scatter(self._y_test, self._y_predict_best, alpha=0.5)

        # Add title and labels
        canvas_best.axes.set_title("Прогнозовані та актуальні дані")
        canvas_best.axes.set_xlabel("Актуальні дані")
        canvas_best.axes.set_ylabel("Прогнозовані дані")
        canvas_best.axes.plot([self._y_test.min(), self._y_test.max()], [self._y_test.min(), self._y_test.max()],
                              'r--')  # Reference line

        canvas_best.draw()

    def plot_best_alpha_mse(self, mina, max_a, canvas):
        canvas.axes.cla()
        alpha_values = np.arange(mina, max_a, 0.1)
        print(alpha_values)
        canvas.axes.plot(alpha_values, self._mean_test_scores, marker='o')

        # Add title and labels
        canvas.axes.set_title("MSE vs. alpha")
        canvas.axes.set_xlabel("alpha")
        canvas.axes.set_ylabel("Тест MSE")

        canvas.axes.axvline(self._best_alpha, color='r', linestyle='--',
                            label=f'Найкраще a: {np.round(self._best_alpha, 4)}')

        canvas.draw()

    def best_mse_value(self):
        return self._best_mse

    def best_alpha_value(self):
        return self._best_alpha
