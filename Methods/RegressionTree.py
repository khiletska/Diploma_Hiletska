from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, GridSearchCV


class RegressionTree:
    def __init__(self, x, y):
        self._X = x.values
        self._y = y.values
        self._mse = 0
        self._X_train, self._X_test, self._y_train, self._y_test = train_test_split(self._X, self._y, test_size=0.2,
                                                                                    random_state=42)
        self._y_predict = None
        self._y_predict_best = None
        self._best_params = None
        self._best_mse = 0

    def perform_regression_tree(self, max_depth, min_samples_split, min_samples_leaf):
        regressor = DecisionTreeRegressor(max_depth=max_depth, min_samples_split=min_samples_split,
                                          min_samples_leaf=min_samples_leaf, random_state=42)
        regressor.fit(self._X_train, self._y_train)
        self._y_predict = regressor.predict(self._X_test)
        self._mse = mean_squared_error(self._y_test, self._y_predict)
        return regressor

    def perform_best_regression_tree(self):
        param_grid = {
            'max_depth': [5, 10, 15, 20, 25],
            'min_samples_split': [2, 10, 20, 50],
            'min_samples_leaf': [1, 5, 10, 20]
        }
        regressor = DecisionTreeRegressor(random_state=42)
        grid_search = GridSearchCV(estimator=regressor, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error',
                                   n_jobs=-1, verbose=2)
        grid_search.fit(self._X_train, self._y_train)
        self._best_params = grid_search.best_params_
        best_regressor = grid_search.best_estimator_
        best_regressor.fit(self._X_train, self._y_train)
        y_predict_test = best_regressor.predict(self._X_test)
        self._best_mse = mean_squared_error(self._y_test, y_predict_test)
        return best_regressor

    def predict_regression_tree(self, user_input, max_depth, min_samples_split, min_samples_leaf):
        # user_input_array = np.array(user_input).reshape(1, -1)
        regressor = self.perform_regression_tree(max_depth, min_samples_split, min_samples_leaf)
        prediction = regressor.predict(user_input)
        print(prediction)
        return prediction[0]

    def mse_value(self):
        return self._mse

    def best_mse_value(self):
        return self._best_mse

    def best_params_value(self):
        return self._best_params

    def plot_regression_tree(self, canvas, x_columns, regressor):
        canvas.axes.cla()
        plot_tree(regressor, feature_names=x_columns, filled=True, rounded=True, ax=canvas.axes)
        canvas.draw()
