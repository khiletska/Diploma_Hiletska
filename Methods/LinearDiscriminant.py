import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix


class LinearDiscriminant:
    def __init__(self, x, y):
        self._X = x.values
        self._y = y.values
        self._report = 0
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(self._X)
        self._X_train, self._X_test, self._y_train, self._y_test = train_test_split(X_scaled, self._y, test_size=0.2,
                                                                                    random_state=42)
        self._y_predict = None
        self._y_predict_best = None
        self._best_params = None
        self._accuracy = 0

    def perform_lda(self):
        lda = LDA()
        lda.fit(self._X_train, self._y_train)
        self._y_predict = lda.predict(self._X_test)
        self._accuracy = accuracy_score(self._y_test, self._y_predict)
        return lda

    def predict_lda(self, user_input):
        lda = self.perform_lda()
        prediction = lda.predict(user_input)
        print(prediction)
        return prediction[0]

    def report_value(self):
        return self._report

    def accuracy_value(self):
        return self._accuracy

    def get_params_value(self):
        n_components = min(len(np.unique(self._y)) - 1, self._X_train.shape[1])
        return n_components

    def plot_lda(self, canvas):
        canvas.axes.cla()
        if self.get_params_value() == 2:
            X_lda = self.perform_lda().transform(self._X_test)

            for i, target_name in enumerate(np.unique(self._y)):
                canvas.axes.scatter(X_lda[self._y_test == target_name, 0], X_lda[self._y_test == target_name, 1],
                                    label=f"Class {target_name}")
            canvas.axes.set_title('LDA Projection')
            canvas.axes.set_xlabel('LD1')
            canvas.axes.set_ylabel('LD2')
            canvas.axes.set_legend(loc='best')
            canvas.draw()

        if self.get_params_value() == 3:
            X_lda = self.perform_lda().transform(self._X_test)

            for i, target_name in enumerate(np.unique(self._y)):
                canvas.axes.scatter(X_lda[self._y_test == target_name, 0],
                                    X_lda[self._y_test == target_name, 1],
                                    X_lda[self._y_test == target_name, 2],
                                    label=f"Class {target_name}")
            canvas.axes.set_title('LDA Projection')
            canvas.axes.set_xlabel('LD1')
            canvas.axes.set_ylabel('LD2')
            canvas.axes.set_zlabel('LD3')
            canvas.axes.legend(loc='best')
            canvas.draw()

    def plot_lda_matrix(self, canvas):
        canvas.axes.cla()
        conf_matrix = confusion_matrix(y_true=self._y_test, y_pred=self._y_predict)
        canvas.axes.matshow(conf_matrix, alpha=0.3)
        for i in range(conf_matrix.shape[0]):
            for j in range(conf_matrix.shape[1]):
                canvas.axes.text(x=j, y=i, s=conf_matrix[i, j], va='center', ha='center', size='xx-large')
        canvas.figure.suptitle('Матриця невідповідностей')
        canvas.axes.set_xlabel('Predicted Label')
        canvas.axes.set_ylabel('True Label')
        canvas.draw()
