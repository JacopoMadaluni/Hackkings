from Regressor import Regressor
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
class SimpleLinearRegressor(Regressor):

    def __init__(self, dataset, y_index, header=False):
        super(SimpleLinearRegressor, self).__init__(dataset, y_index)
        self.name = "Simple Linear Regressor"

    def train(self):
        from sklearn.linear_model import LinearRegression
        self.regressor = LinearRegression()
        self.regressor.fit(self.X_train, self.y_train)

    def predict_test(self):
        self.current_test = self.X_test
        self.current_result = self.regressor.predict(self.X_test)
        return self.current_result

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

    def get_plot(self):
        if len(self.current_test) == 0 or len(self.current_result) == 0:
            print("No value has been asked to predict")
            return
        print(self.current_test)
        if len(self.current_test[0]) > 1:
            print("YO, Can't plot multivariable dataset!")
            fig = Figure(figsize=(10, 10), dpi=100)
            plt = fig.add_subplot(111)
            return fig
        fig = Figure(figsize=(10, 10), dpi=100)
        plt = fig.add_subplot(111)

        plt.scatter(self.X_train, self.y_train, color = 'red')
        plt.plot(self.current_test, self.current_result, color = 'blue')
        plt.set_title("Title pls")
        plt.set_xlabel("x label pls")
        plt.set_ylabel("y label pls")
        return fig
        #plt.show()

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
