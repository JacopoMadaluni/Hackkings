# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 01:39:56 2018

@author: Jaco
"""

# Polynomial Regression
# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1 : -1].values
y = dataset.iloc[:, 2].values


# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""


# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression

linReg = LinearRegression()
linReg.fit(X, y)


# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures

polReg = PolynomialFeatures(degree = 4)
X_poly = polReg.fit_transform(X)

linReg2 = LinearRegression()
linReg2.fit(X_poly, y)

# Visualising the Linear Regression prediction
#plt.scatter(X, y, color = "red")
#plt.plot(X, linReg.predict(X), color = "blue")
#plt.title("Linear Prediction")
#plt.show()

# Visualising the Polynomial Regression prediction
X_grid = np.arange(min(X), max(X), 0.1)   # get a curve (move by 0.1 to 0.1 instead of 1 by 1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = "red")
plt.plot(X_grid, linReg2.predict(polReg.fit_transform(X_grid)), color = "blue")
plt.title("Polynomial Prediction")
#plt.show()

# Predict a new result with Lienar Regression
print(linReg.predict([[6.5]]))

# Predict a new result with Polynomial Regression
print(linReg2.predict(polReg.fit_transform([[1]])))
