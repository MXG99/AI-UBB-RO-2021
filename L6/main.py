import numpy as np

from data_utils import minMaxScaling


def readData(input1, input2, output):
    import os
    from datareader import loadData
    crtDir = os.getcwd()
    filepath = os.path.join(crtDir, 'data', 'world-happiness-report-2017.csv')
    return loadData(filepath, input1, input2, output)


def tool_compute_error(testOutput, computedValidationOutputs):
    from sklearn.metrics import mean_squared_error
    mse = mean_squared_error(testOutput, computedValidationOutputs)
    print("Eroarea prezisa de tool: ", mse)


def sklearnBGDBivariate(trainInputs, trainOutputs, testInputs, testOutputs, epochs, learning_rate):
    from sklearn import linear_model
    regressor = linear_model.SGDRegressor(alpha=learning_rate, max_iter=epochs, average=True)
    for _ in range(epochs):
        # Partial fit nu tine cont de max_iter, numarul de epoci e setat la 1
        regressor.partial_fit(trainInputs, trainOutputs)
    w0, w1, w2 = regressor.intercept_[0], regressor.coef_[0], regressor.coef_[1]
    print("Model invatat cu tool bivariat: f(x) = ", w0, ' + ', w1, ' * x1', ' + ', w2, '* x2')
    computedValidationOutputs = regressor.predict(testInputs)
    tool_compute_error(testOutputs, computedValidationOutputs)


def sklearnBGDUnivariate(trainInputs, trainOutputs, testInputs, testOutputs, epochs, learning_rate):
    from sklearn import linear_model
    regressor = linear_model.SGDRegressor(alpha=learning_rate, max_iter=epochs, average=True)
    univariateTrainInputs = [[trainInputs[index][0]] for index in range(len(trainInputs))]
    for _ in range(epochs):
        # Partial fit nu tine cont de max_iter, numarul de epoci e setat la 1
        regressor.partial_fit(univariateTrainInputs, trainOutputs)
    w0, w1 = regressor.intercept_[0], regressor.coef_[0]
    print('Modelul invatat cu tool univariat: f(x) = ', w0, ' + ', w1, ' * x1')
    univariateTestInputs = [[testInputs[index][0]] for index in range(len(testInputs))]
    computedValidationOutputs = regressor.predict(univariateTestInputs)
    tool_compute_error(testOutputs, computedValidationOutputs)


def compute(row, intercept, w1, w2):
    f = float(intercept)
    f += row[0] * w1
    f += row[1] * w2
    return f


def manualBGDBivariate(trainInputs, trainOutputs, testInputs, testOutputs, epochs, learning_rate):
    from data_utils import compute_error
    i = 0
    intercept, w1, w2 = 0, 0, 0
    while i < epochs:
        errorSum = 0
        sum1 = 0
        sum2 = 0
        for index in range(len(trainInputs)):
            y_comp = intercept + w1 * trainInputs[index][0] + w2 * trainInputs[index][1]
            error = y_comp - trainOutputs[index]
            errorSum += error
            product1 = error * trainInputs[index][0]
            sum1 += product1
            product2 = error * trainInputs[index][1]
            sum2 += product2

        errorSum /= len(trainInputs)
        avg1 = sum1 / len(trainInputs)
        avg2 = sum2 / len(trainInputs)
        intercept -= learning_rate * errorSum
        w1 -= learning_rate * avg1
        w2 -= learning_rate * avg2
        i += 1

    print('Modelul invatat manual pentru batch bivariat: f(x) = ', intercept, ' + ', w1, ' * x1 + ', w2, ' * x2')
    computedValidationOutputs = [compute(row, intercept, w1, w2) for row in testInputs]
    mse = compute_error(computedValidationOutputs, testOutputs)
    print("Eroare manuala: ", mse)


def manualBDGUnivariate(trainInputs, trainOutputs, testInputs, testOutputs, epochs, learning_rate):
    from data_utils import compute_error
    i = 0
    intercept, w1, w2 = 0, 0, 0
    while i < epochs:
        partialProductSum = 0
        errorSum = 0
        for index in range(len(trainInputs)):
            y_comp = intercept + w1 * trainInputs[index][0]
            error = y_comp - trainOutputs[index]
            errorSum += error
            partialProduct = error * trainInputs[index][0]
            partialProductSum += partialProduct

        errorSum /= len(trainInputs)
        avg = partialProductSum / len(trainInputs)
        intercept -= learning_rate * errorSum
        w1 -= learning_rate * avg
        i += 1

    print('Modelul invatat manual pentru batch univariat: f(x) = ', intercept, ' + ', w1, ' * x1')
    computedValidationOutputs = [compute(row, intercept, w1, w2) for row in testInputs]
    mse = compute_error(computedValidationOutputs, testOutputs)
    print("Eroare manuala univariat: ", mse)





def run():
    """
    Runner method
    """
    inputs, outputs = readData('Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score')
    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    testSample = [i for i in indexes if i not in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]

    testInputs = [inputs[i] for i in testSample]
    testOutputs = [outputs[i] for i in testSample]

    # SKLearn BGD Univariate
    sklearnBGDUnivariate(trainInputs, trainOutputs, testInputs, testOutputs, 10000, 0.01)

    # Manual BGD univariate
    manualBDGUnivariate(trainInputs, trainOutputs, testInputs, testOutputs, 10000, 0.01)

    # Sklearn BGD Bivariate
    sklearnBGDBivariate(trainInputs, trainOutputs, testInputs, testOutputs, 10000, 0.01)

    # Manual BGD Bivariate
    manualBGDBivariate(trainInputs, trainOutputs, testInputs, testOutputs, 10000, 0.01)

    # Data normalization
    print("\nAfter data normalization")
    first_feature = [trainInputs[index][0] for index in range(len(trainInputs))]
    second_feature = [trainInputs[index][1] for index in range(len(trainInputs))]
    min, max, ff_scaled = minMaxScaling(first_feature)
    sf_scaled = minMaxScaling(second_feature)
    scaledTrainInputs = [[ff_scaled[index], sf_scaled[index]] for index in range(len(trainInputs))]

    first_feature_test = [testInputs[index][0] for index in range(len(testInputs))]
    second_feature_test = [testInputs[index][1] for index in range(len(testInputs))]
    ff_scaled_test = minMaxScaling2(first_feature_test, min, max)
    ss_scaled_test = minMaxScaling2(second_feature_test, min, max)
    scaledTestInputs = [[ff_scaled_test[index], ss_scaled_test[index]] for index in range(len(testInputs))]

    sklearnBGDUnivariate(scaledTrainInputs, trainOutputs, scaledTestInputs, testOutputs, 10000, 0.01)
    manualBDGUnivariate(scaledTrainInputs, trainOutputs, scaledTestInputs, testOutputs, 10000, 0.01)

    sklearnBGDBivariate(scaledTrainInputs, trainOutputs, scaledTestInputs, testOutputs, 10000, 0.01)
    manualBGDBivariate(scaledTrainInputs, trainOutputs, scaledTestInputs, testOutputs, 10000, 0.01)

    import matplotlib.pyplot as plt
    # plt.plot(first_feature, second_feature, 'ro', label='raw data')
    # plt.plot(ff_scaled, sf_scaled, 'b^', label='0-1 normalized')
    # plt.legend()
    # plt.xlabel("Economy")
    # plt.ylabel("Freedom")
    # plt.show()


run()
