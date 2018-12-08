from Regressor import Regressor
import numpy as np
import matplotlib.pyplot as plt


class RandomForestRegressor(Regressor):

    def __init__(self, database, y_index, header=False):
        super(RandomForestRegressor, self).__init__(database, y_index, header)


    def train(self):
        from sklearn.ensemble import RandomForestRegressor
        self.regressor = RandomForestRegressor( n_estimators = 300, random_state = 42)
        self.regressor.fit(self.X_train,self.y_train)

    def predict(self, *args, **kwargs):
        self.current_test = args
        self.current_result = self.regressor.predict(args)
        return self.current_result

    def plot(self):
        if len(self.current_test) == 0 or len(self.current_result) == 0:
            print("No value has been asked to predict")
            return
        print(self.current_test)
        if len(self.current_test[0]) > 1:
            print("YO, Can't plot multivariable dataset!")
            return
        plt.scatter(self.X_train, self.y_train, color = 'red')
        plt.plot(self.current_test, self.current_result, color = 'blue')
        plt.title("Title pls")
        plt.xlabel("x label pls")
        plt.ylabel("y label pls")
        plt.show()

    def plot2(self):
        X_grid = np.arange(min(self.current_test), max(self.current_test), 0.01)
        X_grid = X_grid.reshape(len(X_grid), 1)

        plt.scatter(self.X, self.y, color = "red")
        plt.plot(X_grid, self.regressor.predict(X_grid), color = "blue")
        plt.title("Random forest Prediction")
        plt.show()
