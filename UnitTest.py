import unittest

import pandas as pd

from Methods.KNNClassification import KNNClassification
from Methods.LeaveOneOutCrossValidation import LeaveOneOutCrossValidation
from Methods.LogisticRegression import MyLogisticRegression
from Methods.kFoldCrossValidation import KFoldCrossValidation


class MyTestCase(unittest.TestCase):
    def test_x_vector_in_kcrosvalid(self):
        data = {'x': [1, 2, 3, 4],
                'y': [5, 6, 7, 8]}
        df = pd.DataFrame(data)
        kcrosvalid = KFoldCrossValidation(df[['x']], df['y'])
        kcrosvalid.check_x(df[['x']], df['y'])
        self.assertEqual(len(kcrosvalid.x_value()), len(df[['x']].values.reshape(-1, 1)))

    def test_x_matrix_in_kcrosvalid_(self):
        data = {'x': [1, 2, 3, 4],
                't': [2, 3, 4, 5],
                'y': [5, 6, 7, 8]}
        df = pd.DataFrame(data)
        kcrosvalid = KFoldCrossValidation(df[['x', 't']], df['y'])
        kcrosvalid.check_x(df[['x', 't']], df['y'])
        self.assertEqual(len(kcrosvalid.x_value()), len(df[['x', 't']].values))

    def test_clas_in_knnclas(self):
        data = {'x': [1, 2, 3, 4],
                't': [2, 3, 4, 5],
                'y': [5, 6, 7, 8]}
        df = pd.DataFrame(data)
        knnclas = KNNClassification(df[['x']], df['y'])
        knnclas.make_classes(2)
        self.assertEqual(knnclas.bins_value()[0], 5)
        self.assertEqual(knnclas.bins_value()[1], 6.5)
        self.assertEqual(knnclas.bins_value()[2], 8)

    def test_check_x_vector_crosvalid(self):
        data = {'x': [1, 2, 3, 4],
                'y': [5, 6, 7, 8]}
        df = pd.DataFrame(data)
        crosvalid = LeaveOneOutCrossValidation(df[['x']], df['y'])
        crosvalid.check_x(df[['x']], df['y'])
        self.assertEqual(len(crosvalid.x_value()), len(df[['x']].values.reshape(-1, 1)))

    def test_x_matrix_in_crosvalid_(self):
        data = {'x': [1, 2, 3, 4],
                't': [2, 3, 4, 5],
                'y': [5, 6, 7, 8]}
        df = pd.DataFrame(data)
        crosvalid = LeaveOneOutCrossValidation(df[['x', 't']], df['y'])
        crosvalid.check_x(df[['x', 't']], df['y'])
        self.assertEqual(len(crosvalid.x_value()), len(df[['x', 't']].values))

    def test_check_x_vector_logisticreg(self):
        data = {'x': [1, 2, 3, 4],
                'y': ['T', 'F', 'F', 'F']}
        df = pd.DataFrame(data)
        logreg = MyLogisticRegression(df[['x']], df['y'])
        logreg.check_x(df[['x']], df['y'])
        self.assertEqual(len(logreg.x_value()), len(df[['x']].values.reshape(-1, 1)))

    def test_x_matrix_in_logisticreg(self):
        data = {'x': [1, 2, 3, 4],
                't': [2, 3, 4, 5],
                'y': ['T', 'F', 'T', 'T']}
        df = pd.DataFrame(data)
        logreg = MyLogisticRegression(df[['x', 't']], df['y'])
        logreg.check_x(df[['x', 't']], df['y'])
        self.assertEqual(len(logreg.x_value()), len(df[['x', 't']].values))

    def test_check_y_no_yes_logisticregr(self):
        data = {'x': [1, 2, 3, 4],
                'y': ['No', 'Yes', 'No', 'No']}
        df = pd.DataFrame(data)
        logreg = MyLogisticRegression(df[['x']], df['y'])
        self.assertEqual(logreg.y_value(), [0, 1, 0, 0])

    def test_check_y_true_false_logisticregr(self):
        data = {'x': [1, 2, 3, 4],
                'y': ['T', 'T', 'F', 'F']}
        df = pd.DataFrame(data)
        logreg = MyLogisticRegression(df[['x']], df['y'])
        self.assertEqual(logreg.y_value(), [1, 1, 0, 0])





if __name__ == '__main__':
    unittest.main()
