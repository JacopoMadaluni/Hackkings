from Regressor import Regressor
from PolynomialLinearRegressor import PolynomialLinearRegressor
from SVRRegressor import SVRRegressor
from SimpleLinearRegressor import SimpleLinearRegressor
from DecisionTreeRegressor import DecisionTreeRegressor
from RandomForestRegressor import RandomForestRegressor
import sys

class Controller:

    def __init__(self):
        self.file = ""
        self.y_index = -1

    def get_all_regressors(self, dataset, y_index):
        sl = SimpleLinearRegressor(dataset, y_index)
        pl = PolynomialLinearRegressor(dataset, y_index)
        dt = DecisionTreeRegressor(dataset, y_index)
        rf = RandomForestRegressor(dataset, y_index)
        return [sl, pl, dt, rf]



    def get_choices(self, dataset):
        pass

    def get_best_regressor(self):
        if self.file == "" or self.y_index == -1:
            return None

        regressors = self.get_all_regressors(self.file, self.y_index)
        min_error = 10000000000
        current_best = None
        for regressor in regressors:
            error = regressor.get_average_error()
            if (error < min_error):
                min_error = error
                current_best = regressor
        return current_best

    def set_file(self, file):
        self.file = file
    def set_y_index(self, y_index):
        self.y_index = y_index
