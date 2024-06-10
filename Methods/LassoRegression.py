import numpy as np
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error


class LassoRegression:
    def __init__(self, x, y):
        self._X = x.values
        self._y = y.values
        self._mse = 0
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(self._X)
        self._X_train, self._X_test, self._y_train, self._y_test = train_test_split(X_scaled, self._y, test_size=0.2,
                                                                                    random_state=42)
        self._y_predict = None
        self._y_predict_best = None
        self._best_alpha = 0
        self._best_mse = 0
        self._mean_test_scores = None

    def perform_lasso_regression(self, alpha=1.0):
        # Initialize the Lasso regression model with grid search
        lasso = Lasso(alpha=alpha)
        param_grid = {
            'max_iter': [1000, 2000, 5000],
            'tol': [1e-4, 1e-5, 1e-3]
        }
        grid_search = GridSearchCV(lasso, param_grid, cv=5, scoring='neg_mean_squared_error')
        grid_search.fit(self._X_train, self._y_train)

        # Retrieve the best model
        best_lasso = grid_search.best_estimator_

        # Make predictions
        self._y_predict = best_lasso.predict(self._X_test)

        # Evaluate the model
        self._mse = mean_squared_error(self._y_test, self._y_predict)
        return best_lasso

    def plot_lasso(self, canvas):
        canvas.axes.cla()
        canvas.axes.scatter(self._y_test, self._y_predict, edgecolor='k', alpha=0.7, color='b')
        canvas.axes.plot([self._y_test.min(), self._y_test.max()], [self._y_test.min(), self._y_test.max()], 'k--',
                         lw=3)
        canvas.axes.set_xlabel("Актуальні дані")
        canvas.axes.set_ylabel("Прогнозовані дані")
        canvas.axes.set_title("Прогнозовані та актуальні дані")
        canvas.draw()

    def mse_value(self):
        return np.round(self._mse, 4)

    def predict_lasso(self, arr, alpha=1.0):
        result = self.perform_lasso_regression(alpha).predict(arr)
        return result

    def find_best_alpha(self, alpha_min, alpha_max,
                        max_iter=1000, tol=0.0001):
        print("here")
        # Generate a list of alpha values to test
        alphas = np.arange(alpha_min, alpha_max, 0.1)
        print(alphas)

        # Initialize the Lasso regression model with grid search
        lasso = Lasso(max_iter=max_iter, tol=tol)
        param_grid = {'alpha': alphas}
        grid_search = GridSearchCV(lasso, param_grid, cv=5, scoring='neg_mean_squared_error')
        grid_search.fit(self._X_train, self._y_train)

        # Retrieve the best model
        best_lasso = grid_search.best_estimator_
        print("here")
        self._best_alpha = grid_search.best_params_['alpha']
        print(self._best_alpha)
        self._best_mse = -grid_search.best_score_
        print(self._best_mse)
        self._mean_test_scores = -grid_search.cv_results_['mean_test_score']
        print(self._mean_test_scores)
        self._y_predict_best = best_lasso.predict(self._X_test)

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

        canvas.axes.plot(alpha_values, self._mean_test_scores, marker='o')

        # Add title and labels
        canvas.axes.set_title("MSE vs. a")
        canvas.axes.set_xlabel("a")
        canvas.axes.set_ylabel("Тест MSE")

        canvas.axes.axvline(self._best_alpha, color='r', linestyle='--',
                            label=f'Best alpha: {np.round(self._best_alpha, 4)}')

        canvas.draw()

    def best_mse_value(self):
        return self._best_mse

    def best_alpha_value(self):
        return self._best_alpha
