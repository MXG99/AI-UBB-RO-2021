import numpy as np


def sigmoid(x):
    from math import exp
    return 1 / (1 + exp(-x))


class LogisticRegression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []
        self.betas_ = []

    def fit(self, train_inputs, train_outputs, learning_rate=0.001, epochs=3000):
        self.coef_ = [0.0 for _ in range(1 + len(train_inputs[0]))]
        epoch = 0
        while epoch < epochs:
            for i in range(len(train_inputs)):
                y_comp = sigmoid(self.evaluate(train_inputs[i], self.coef_))
                error = y_comp - train_outputs[i]
                for j in range(0, len(train_inputs[0])):
                    self.coef_[j + 1] -= learning_rate * error * train_inputs[i][j]
                self.coef_[0] -= learning_rate * error
            epoch += 1

        self.intercept_ = self.coef_[0]
        self.coef_ = self.coef_[1:]
        # Adaugam coeficientii pentru fiecare model
        self.betas_.append([self.intercept_, self.coef_[0], self.coef_[1], self.coef_[2], self.coef_[3]])

    def evaluate(self, train_input, coef):
        yi = coef[0]
        for j in range(len(train_input)):
            yi += coef[j + 1] * train_input[j]
        return yi

    def predict_one_sample(self, test_input, coef):
        return sigmoid(self.evaluate(test_input, coef))

    def predict(self, test_inputs):
        from scipy.special import softmax
        predictions = []
        for i in range(len(test_inputs)):
            predicted_samples = []
            for j in range(len(self.betas_)):
                predicted_samples.append(self.predict_one_sample(test_inputs[i], self.betas_[j]))
            predictions.append(np.argmax(softmax(predicted_samples)))
        return predictions
