# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 01:30:48 2018

@author: Jaco
"""

# Decision Tree Regression
# Disclaimer: this regression model is using a two dimension dataset.
# An optimal use case for this template is a at least three dimension datasets.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd

from Reader import Reader


class Regressor:

    def __init__(self, dataset, y_index, header=False):
        # position Position_Salaries
        self.dataset = pd.read_csv(dataset)
        self.X = self.dataset.iloc[:, 0 :].values
        self.X = np.delete(self.X, y_index, 1)

        """reader = Reader(dataset)
        self.dataset = reader.dataset
        reader.set_Y(y_index)
        self.X = reader.get_x_matrix()"""
        self.reader = Reader(dataset)
        self.encode()



        self.y = self.dataset.iloc[:, y_index].values
        #self.y = reader.get_y_matrix()
        #print("this is self.y{}".format(self.y))
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size = 0.2, random_state = 0)
        self.regressor = None

    def remove_variable(self, index):
        self.X = np.delete(self.X, index, 1)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size = 0.2, random_state = 0)
        self.regressor = None
        self.update()

    def update(self):
        pass
    def encode(self):
        toEncode = []
        for i, var in enumerate(self.X[1]):
            if isinstance(var, str):
                toEncode.append(i)

        from sklearn.preprocessing import LabelEncoder, OneHotEncoder
        labelEncoder_x = LabelEncoder()
        for i in toEncode:
            self.X[:, i] = labelEncoder_x.fit_transform(self.X[:, i])

    def print_x_train(self):
        print(self.X_train)
    def print_y_train(self):
        print(self.y_train)
    def print_x_test(self):
        for e in self.X_test:
            print(e)
    def print_y_test(self):
        print(self.y_test)
    def print_X(self):
        print(self.X)

    def print_test_mapping(self):
        for i, col in enumerate(self.X_test):
            print("{} --> {}".format(col, self.y_test[i]))

    def print_cols(self):
        for col in self.X_train:
            print(col)



# Feature Scaling
    def feature_scale(self):
        from sklearn.preprocessing import StandardScaler
        sc_X = StandardScaler()
        self.X_train = sc_X.fit_transform(self.X_train)
        self.X_test = sc_X.transform(self.X_test)
        self.sc_y = StandardScaler()
        self.y_train = sc_y.fit_transform(self.y_train)


# Fitting Decision Tree Regression  to the dataset


    def plot(self):

        X_grid = np.arange(min(self.X), max(self.X), 0.01)
        X_grid = X_grid.reshape(len(X_grid), 1)
        print( self.regressor.predict(X_grid))
        plt.scatter(self.X, self.y, color = "red")
        plt.plot(X_grid, self.regressor.predict(X_grid), color = "blue")
        plt.title("Decision Tree Prediction")
        plt.show()

# Predict a new result
#y_pred = regressor.predict(6.5)


# Visualising the Decision Tree Regression prediction (higher resolution and smoother curve)
#X_grid = np.arange(min(X), max(X), 0.01)
#X_grid = X_grid.reshape(len(X_grid), 1)

#plt.scatter(X, y, color = "red")
#plt.plot(X_grid, regressor.predict(X_grid), color = "blue")
#plt.title("Decision Tree Prediction")
#plt.show()
