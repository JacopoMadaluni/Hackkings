from Regressor import Regressor
import numpy as np
class SVRRegressor(Regressor):

    def __init__(self, dataset, y_index, header=False):
        super(SVRRegressor, self).__init__(dataset, y_index)
        self.y = self.y.reshape(len(self.y), 1)
        self.update()


    def update(self):
        from sklearn.preprocessing import StandardScaler
        self.sc_X = StandardScaler()
        self.X = self.sc_X.fit_transform(self.X)
        #X_test = sc_X.transform(X_test)
        self.sc_y = StandardScaler()
        try:
            self.y = self.sc_y.fit_transform(self.y)
        except:
            try:
                self.y = self.sc_y.fit_transform(self.y.reshape(-1,1))
            except:
                self.y = self.sc_y.fit_transform(self.y.reshape(1,-1))

    def train(self):
        from sklearn.svm import SVR
        self.regressor = SVR(kernel = 'rbf')
        self.regressor.fit(self.X_train, self.y_train)

    def predict(self, *args, **kwargs):
        self.current_test = args
        #y_pred = self.sc_y.inverse_transform(self.regressor.predict(self.sc_X.transform(np.array([args]))))
        self.current_result = self.sc_y.inverse_transform(self.regressor.predict(args))
        #y_pred = self.regressor.predict(self.sc_X.transform([args]))
        #return self.sc_y.inverse_transform(y_pred)
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
