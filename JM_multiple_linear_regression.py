# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_x = LabelEncoder()
X[:, 3] = labelEncoder_x.fit_transform(X[:, 3])


oneHotEncoder = OneHotEncoder(categorical_features = [3])
X = oneHotEncoder.fit_transform(X).toarray()

# Avoid the Dummy Variable Trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""



# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# El predicto

y_pred = regressor.predict(X_test)

# Building the optional model using Backward Elimination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50, 1)).astype(int), values = X , axis = 1)    # Since the Linear regressio equation is:
                                                                            # Y = b0 + b1*X1 + ... + bn*Xn
                                                                            # and since the statsmodels libr works with:
                                                                            # Y = b0*X0 + b1*X1.. where X0 = 1 for every col
                                                                            # We need to append at the beginning of X a
                                                                            # column of ones
                                                                            # Numpy.ones(50, 1) returns a matrix with 50 rows
                                                                            # of ones (one column)

# significanceLevel = 0.05
X_optimal = X[:, [0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_optimal).fit()
print(regressor_OLS.summary())

X_optimal = X[:, [0,1,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_optimal).fit()
regressor_OLS.summary()

X_optimal = X[:, [0,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_optimal).fit()
regressor_OLS.summary()

X_optimal = X[:, [0,3,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_optimal).fit()
regressor_OLS.summary()

X_optimal = X[:, [0,3]]
regressor_OLS = sm.OLS(endog = y, exog = X_optimal).fit()
regressor_OLS.summary()


print(X_test)
test = [[1, 1, 165349.2, 136897.8, 471784.1]]
prediction = regressor.predict(X_test)
print(prediction)

#plt.scatter(X, y, color = 'red')
#plt.plot(X, regressor.predict(X_test), color = 'blue')
#plt.scatter(test[0][4], prediction, color='red')
#plt.plot(test[0][4], prediction , color = 'blue')
#plt.title('Truth or Bluff (Regression Model)')
#plt.xlabel('Position level')
#plt.ylabel('Salary')
#plt.show()
