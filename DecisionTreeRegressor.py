from Regressor import Regressor
import matplotlib.pyplot as plt
class DecisionTreeRegressor(Regressor):

    def __init__(self, dataset, y_index, header=False):
        super(DecisionTreeRegressor, self).__init__(dataset, y_index)

    def train(self):
        from sklearn.tree import DecisionTreeRegressor as DTR
        self.regressor = DTR( splitter = "best", random_state = 42)
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
        plt.scatter(self.X, self.y, color = 'red')
        plt.plot(self.current_test, self.current_result, color = 'blue')
        plt.title("Title pls")
        plt.xlabel("x label pls")
        plt.ylabel("y label pls")
        plt.show()
