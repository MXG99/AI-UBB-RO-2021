from statistics import mean
import numpy
import matrixcalculations as mc


class LeastSquares:
    def __init__(self):
        self.ws = None

    def fit(self, x, y):
        for i in range(len(x)):
            x[i].insert(0, 1.0)
        xt = mc.transpusa(x)
        toInverse = mc.matrixMultiplication(xt, x)
        inverse = mc.getMatrixInverse(toInverse)
        betas = mc.matrixMultiplication(mc.matrixMultiplication(inverse, xt), [[el] for el in y])
        self.ws = betas[0][0], betas[1][0], betas[2][0]

    def function(self):
        print("Model invatat manual: f(x) = ", self.ws[0], " + ", self.ws[1], "* x1", " + ", self.ws[2], " * x2")

    def computeRow(self, row):
        """
        Compute f(x), de exemplu: w0 + suma(xi*wi), i=1,n x=linia
        :param row:
        """
        f = float(self.ws[0])
        for i in range(len(row)):
            f += (row[i] * self.ws[i + 1])
        return f

    def mse(self, y_prezis, y):
        errors = []
        for i in range(len(y)):
            errors.append((y[i] - y_prezis[i]) ** 2)
        return mean(errors)
