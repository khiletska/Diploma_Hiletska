from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import f1_score


class KNNClassification:
    def __init__(self, x, y):
        self._X = x.values
        self._y = y.values
        self._res = 0
        self._y_predict = 0
        self._y_predict_best = 0
        self._best_res = 0
        self._X_train, self._X_test, self._y_train, self._y_test = train_test_split(self._X, self._y, test_size=0.2,
                                                                                    random_state=45)
        self._bins = []

    def make_classes(self, number):
        new_y = pd.qcut(self._y, number, retbins=False, labels=range(1, number + 1))
        a, bins = pd.qcut(self._y.tolist(), number, retbins=True)
        self._bins = bins
        self._y = new_y
        self._X_train, self._X_test, self._y_train, self._y_test = train_test_split(self._X, self._y, test_size=0.2,
                                                                                    random_state=45)
        res = ""
        res = res + f"[{np.round(bins[0], 4)};{np.round(bins[1], 4)}]клас 1 "
        for i in range(1, len(bins) - 1):
            res = res + f"({np.round(bins[i], 4)};{np.round(bins[i + 1], 4)}]-клас {i + 1} "
        return res

    def knn_classification(self, k):
        classifier = KNeighborsClassifier(k)
        classifier.fit(self._X_train, self._y_train)
        y_predict = classifier.predict(self._X_test)
        self._y_predict = y_predict
        self._res = classification_report(self._y_test, y_predict)
        return classifier

    def predict(self, arr, k):
        result = self.knn_classification(k).predict(arr)
        return result

    def analyze_num_neigh(self, min_val, max_val):
        f1s = []
        for i in range(min_val, max_val + 1):
            knn = KNeighborsClassifier(n_neighbors=i)
            knn.fit(self._X_train, self._y_train)
            predict_i = knn.predict(self._X_test)
            f1s.append(f1_score(self._y_test, predict_i, average='weighted'))
        return f1s

    def plot_knn_clas(self, min_val, max_val, canvas_knn_clas_k):
        f1 = self.analyze_num_neigh(min_val, max_val)
        canvas_knn_clas_k.axes.cla()
        canvas_knn_clas_k.axes.plot(range(min_val, max_val + 1), f1, color='red',
                                    linestyle='dashed', marker='o',
                                    markerfacecolor='blue', markersize=10)
        canvas_knn_clas_k.figure.suptitle('Залежність міри F1 від k')
        canvas_knn_clas_k.draw()

    def find_best_k(self, min_val, max_val):
        f1s = self.analyze_num_neigh(min_val, max_val)
        max_f1 = max(f1s)
        best_k = np.array(f1s).argmax() + min_val
        return max_f1, best_k

    def find_best_values(self, min_val, max_val):
        max_f1, k_best = self.find_best_k(min_val, max_val)
        classifier15 = KNeighborsClassifier(n_neighbors=k_best)
        classifier15.fit(self._X_train, self._y_train)
        self._y_predict_best = classifier15.predict(self._X_test)
        self._best_res = classification_report(self._y_test, self._y_predict_best)

    def plot_matrix(self, canvas_knn_clas):
        canvas_knn_clas.axes.cla()
        conf_matrix = confusion_matrix(y_true=self._y_test, y_pred=self._y_predict)

        canvas_knn_clas.axes.matshow(conf_matrix, alpha=0.3)
        for i in range(conf_matrix.shape[0]):
            for j in range(conf_matrix.shape[1]):
                canvas_knn_clas.axes.text(x=j, y=i, s=conf_matrix[i, j], va='center', ha='center', size='xx-large')
        canvas_knn_clas.figure.suptitle('Матриця невідповідностей')
        canvas_knn_clas.draw()

    def plot_best_matrix(self, canvas_knn_clas_best):
        canvas_knn_clas_best.axes.cla()
        conf_matrix = confusion_matrix(y_true=self._y_test, y_pred=self._y_predict_best)
        canvas_knn_clas_best.axes.matshow(conf_matrix, alpha=0.3)
        for i in range(conf_matrix.shape[0]):
            for j in range(conf_matrix.shape[1]):
                canvas_knn_clas_best.axes.text(x=j, y=i, s=conf_matrix[i, j], va='center', ha='center', size='xx-large')
        canvas_knn_clas_best.figure.suptitle('Матриця невідповідностей')
        canvas_knn_clas_best.draw()

    def res_value(self):
        return self._res

    def best_res_value(self):
        return self._best_res

    def bins_value(self):
        return self._bins
