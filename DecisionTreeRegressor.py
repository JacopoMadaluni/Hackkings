from Regressor import Regressor
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
class DecisionTreeRegressor(Regressor):

    def __init__(self, dataset, y_index, header=False):
        super(DecisionTreeRegressor, self).__init__(dataset, y_index)

    def train(self):
        from sklearn.tree import DecisionTreeRegressor as DTR
        self.regressor = DTR( splitter = "best", random_state = 42)
        self.regressor.fit(self.X_train,self.y_train)
        self.name = "Decision Tree Regressor"


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

        plt.scatter(self.X, self.y, color = 'red')
        plt.plot(self.current_test, self.current_result, color = 'blue')
        plt.set_title(self.name)
        plt.set_xlabel("Independet Variable")
        plt.set_ylabel("Dependent Variable")
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

        plt.scatter(self.X, self.y, color = 'red')
        plt.plot(self.current_test, self.current_result, color = 'blue')
        plt.title("Decision Tree Regressor")
        plt.xlabel("Independet Variable")
        plt.ylabel("Dependent Variable")
        plt.show()

    def scatter_tests(self):
        if len(self.current_test) == 0 or len(self.current_result) == 0:
            print("No value has been asked to predict")
            return
        print(self.current_test)
        if len(self.current_test[0]) > 1:
            print("YO, Can't plot multivariable dataset!")
            return

        plt.scatter(self.X_train, self.y_train, color = 'red')
        plt.title("Scatter Plot")
        plt.xlabel("Independet Variable")
        plt.ylabel("Dependent Variable")
        plt.show()
