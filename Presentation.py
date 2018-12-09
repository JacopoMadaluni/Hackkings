from Regressor import Regressor
from PolynomialLinearRegressor import PolynomialLinearRegressor
from SVRRegressor import SVRRegressor
from SimpleLinearRegressor import SimpleLinearRegressor
from DecisionTreeRegressor import DecisionTreeRegressor
from RandomForestRegressor import RandomForestRegressor
from Controller import Controller

def test_simple_linear():
    simpleR = SimpleLinearRegressor("Salary_Data.csv", 1)
    #simpleR.remove_variable(0)
    simpleR.train()
    simpleR.predict([1],[2],[3],[4],[5],[6],[7],[8],[9], [10])
    simpleR.plot()

    simpleR = SimpleLinearRegressor("Position_Salaries.csv", 2)
    simpleR.remove_variable(0)
    simpleR.train()
    simpleR.predict([1],[2],[3],[4],[5],[6],[7],[8],[9], [10])
    simpleR.plot()


def test_polinomial_linear():
    regressor = PolynomialLinearRegressor("Salary_Data.csv", 1)
    regressor.train()
    regressor.predict([1],[2],[3],[4],[5],[6],[7],[8],[9])
    regressor.plot()

    regressor = PolynomialLinearRegressor("Position_Salaries.csv", 2)
    regressor.remove_variable(0)
    regressor.train()
    regressor.predict([1],[2],[3],[4],[5],[6],[7],[8],[9])
    regressor.plot()


def test_svr():
    regressor = SVRRegressor("Salary_Data.csv", 1)
    print(regressor.get_average_error())
    regressor.train()
    regressor.predict([1],[2],[3],[4],[5],[6],[7],[8],[9])
    regressor.plot()


    regressor = SVRRegressor("Position_Salaries.csv", 2)
    regressor.remove_variable(0)
    print(regressor.get_average_error())
    regressor.train()
    regressor.predict([1],[2],[3],[4],[5],[6],[7],[8],[9])
    regressor.plot()


    regressor = SVRRegressor("50_Startups.csv", 4)
    print(regressor.get_average_error())
    regressor.train()
    regressor.predict([1,3, 400, 3])
    regressor.plot()


def test_decision_t():
    regressor = DecisionTreeRegressor("Salary_Data.csv", 1)
    regressor.train()
    regressor.predict([1],[2],[3],[4],[5],[6],[7],[8],[9], [10])
    regressor.plot()

    regressor = DecisionTreeRegressor("Position_Salaries.csv", 2)
    regressor.remove_variable(0)
    regressor.train()
    regressor.predict([1],[2],[3],[4],[5],[6],[7],[8],[9], [10])
    regressor.plot()


def test_random_forest():
    regressor = RandomForestRegressor("Salary_Data.csv", 1)
    regressor.train()
    regressor.predict([1],[2],[3],[4],[5],[6],[7],[8],[9], [10])
    regressor.plot()

    regressor = RandomForestRegressor("Position_Salaries.csv", 2)
    regressor.remove_variable(0)
    regressor.train()
    regressor.predict([1],[2],[3],[4],[5],[6],[7],[8],[9], [10])
    regressor.plot()



def start_presentation():
    test_simple_linear()
    test_polinomial_linear()
    #test_svr()
    test_decision_t()
    test_random_forest()

if __name__ == "__main__":
    start_presentation()
