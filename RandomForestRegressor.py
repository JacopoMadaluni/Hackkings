from Regressor import Regressor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class RandomForestRegressor(Regressor):

    def __init__(self, database, y_index, header=False):
        super(RandomForestRegressor, self).__init__(database, y_index, header)
        self.name = "Random Forest Regressor"

    def train(self):
        from sklearn.ensemble import RandomForestRegressor
        self.regressor = RandomForestRegressor( n_estimators = 300, random_state = 42)
        self.regressor.fit(self.X_train,self.y_train)

    def predict(self, *args, **kwargs):
        self.current_test = args
        self.current_result = self.regressor.predict(args)
        return self.current_result

    def get_average_error(self):
        self.train()
        error = 0
        count = 0
        for i, e in enumerate(self.X_test):
            prediction = self.predict([*e])
            error += abs(prediction - self.y_test[i])
            count += 1
        return error/count

    def plot(self):
        if len(self.current_test) == 0 or len(self.current_result) == 0:
            print("No value has been asked to predict")
            return
        print(self.current_test)
        if len(self.current_test[0]) > 1:
            print("YO, Can't plot multivariable dataset!")
            return
        fig = Figure(figsize=(10, 10), dpi=100)
        plt = fig.add_subplot(111)

        plt.scatter(self.X_train, self.y_train, color = 'red')
        plt.plot(self.current_test, self.current_result, color = 'blue')
        plt.set_title("Title pls")
        plt.set_xlabel("x label pls")
        plt.set_ylabel("y label pls")
        return fig
        #plt.show()

    def plot2(self):
        X_grid = np.arange(min(self.current_test), max(self.current_test), 0.01)
        X_grid = X_grid.reshape(len(X_grid), 1)

        plt.scatter(self.X, self.y, color = "red")
        plt.plot(X_grid, self.regressor.predict(X_grid), color = "blue")
        plt.title("Random forest Prediction")
        plt.show()
