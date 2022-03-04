import os
from data_loader import loadData
from leastsquares import LeastSquares

from matplotlib import pyplot as plt
from ploters import plotDataHistogram
import numpy as np

crtDir = os.getcwd()
filePath = os.path.join(crtDir, 'data', 'world-happiness-report-2017.csv')

inputs, outputs = loadData(filePath, 'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score')


def tool_compute_error(validOutput, computedValidationOutputs):
    from sklearn.metrics import mean_squared_error
    mse = mean_squared_error(validOutput, computedValidationOutputs)
    print("Eroarea prezisa de tool: ", mse)


def tool_compute_model(trainInputs, trainOutputs, validInputs, validOutput):
    from sklearn import linear_model
    xx = [[el[0], el[1]] for el in trainInputs]
    regressor = linear_model.LinearRegression()
    regressor.fit(xx, trainOutputs)
    w0, w1, w2 = regressor.intercept_, regressor.coef_[0], regressor.coef_[1]
    print('Modelul invatat: f(x) = ', w0, ' + ', w1, ' * x1 + ', w2, ' * x2')
    computedValidationOutputs = regressor.predict([[el[0], el[1]] for el in validInputs])

    tool_compute_error(validOutput, computedValidationOutputs)


def manual_compute_model(trainInputs, trainOutputs, validInputs, validOutput):

    ls = LeastSquares()
    ls.fit(trainInputs, trainOutputs)
    ls.function()
    computedValidationOutputs = [ls.computeRow(row) for row in validInputs]
    mse = ls.mse(computedValidationOutputs, validOutput)
    print("Eroare manuala: ", mse)


def run():
    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    validSample = [i for i in indexes if i not in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]

    validInputs = [inputs[i] for i in validSample]
    validOutput = [outputs[i] for i in validSample]

    tool_compute_model(trainInputs, trainOutputs, validInputs, validOutput)
    manual_compute_model(trainInputs, trainOutputs, validInputs, validOutput)


run()
