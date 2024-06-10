from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split, GridSearchCV


class ClassificationTree:
    def __init__(self, x, y):
        self._X = x.values
        self._y = y.values
        self._report = 0
        self._X_train, self._X_test, self._y_train, self._y_test = train_test_split(self._X, self._y, test_size=0.2,
                                                                                    random_state=42)
        self._y_pred = None
        self._y_pred_best = None
        self._best_params = None
        self._accuracy = 0

    def perform_classification_tree(self, max_depth, min_samples_split, min_samples_leaf):
        # Create the classifier
        clf = DecisionTreeClassifier(max_depth=max_depth,
                                     min_samples_split=min_samples_split,
                                     min_samples_leaf=min_samples_leaf)
        # Fit the classifier on the training data
        clf.fit(self._X_train, self._y_train)
        self._y_pred = clf.predict(self._X_test)
        self._accuracy = accuracy_score(self._y_test, self._y_pred)
        self._report = classification_report(self._y_test, self._y_pred)

        return clf

    def perform_best_cl_tree(self):
        # Define the parameter grid for GridSearchCV
        param_grid = {
            'max_depth': [5, 10, 20, 30, 40, 50],
            'min_samples_split': [2, 10, 20, 30],
            'min_samples_leaf': [1, 2, 4, 6]
        }
        clf = DecisionTreeClassifier()

        grid_search = GridSearchCV(clf, param_grid, cv=5, scoring='accuracy')
        grid_search.fit(self._X_train, self._y_train)

        # Get the best parameters
        self._best_params = grid_search.best_params_

    def predict_cl_tree(self, user_input, max_depth, min_samples_split, min_samples_leaf):
        classifier = self.perform_classification_tree(max_depth, min_samples_split, min_samples_leaf)
        prediction = classifier.predict(user_input)
        return prediction[0]

    def report_value(self):
        return self._report

    def best_params_value(self):
        return self._best_params

    def plot_cl_tree(self, canvas, x_columns, cl):
        canvas.axes.cla()
        plot_tree(cl, feature_names=x_columns, filled=True, rounded=True, ax=canvas.axes)
        canvas.draw()

    def plot_cl_matrix(self, canvas):
        canvas.axes.cla()
        conf_matrix = confusion_matrix(y_true=self._y_test, y_pred=self._y_pred)
        canvas.axes.matshow(conf_matrix, alpha=0.3)
        for i in range(conf_matrix.shape[0]):
            for j in range(conf_matrix.shape[1]):
                canvas.axes.text(x=j, y=i, s=conf_matrix[i, j], va='center', ha='center', size='xx-large')
        canvas.figure.suptitle('Матриця невідповідностей')
        canvas.draw()
