from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis as QDA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix


class QuadraticDiscriminant:
    def __init__(self, x, y):
        self._X = x.values
        self._y = y.values
        self._report = 0
        scaler = StandardScaler()
        x_scaled = scaler.fit_transform(self._X)
        self._X_train, self._X_test, self._y_train, self._y_test = train_test_split(x_scaled, self._y, test_size=0.2,
                                                                                    random_state=42)
        self._y_predict = None
        self._y_predict_best = None
        self._best_params = None
        self._accuracy = 0

    def perform_qda(self):
        qda = QDA()
        qda.fit(self._X_train, self._y_train)
        self._y_predict = qda.predict(self._X_test)
        self._accuracy = accuracy_score(self._y_test, self._y_predict)
        return qda

    def predict_qda(self, user_input):
        qda = self.perform_qda()
        prediction = qda.predict(user_input)
        return prediction[0]

    def report_value(self):
        return self._report

    def accuracy_value(self):
        return self._accuracy

    def plot_qda_matrix(self, canvas):
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
