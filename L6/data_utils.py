def calculate_avg(trainInputs):
    sum1 = 0
    sum2 = 0
    for i in range(len(trainInputs)):
        sum1 += trainInputs[i][0]
        sum2 += trainInputs[i][1]
    return sum1 / len(trainInputs), sum2 / len(trainInputs)


def compute_error(y_prezis, y):
    from statistics import mean
    errors = []
    for i in range(len(y)):
        errors.append((y[i] - y_prezis[i]) ** 2)
    return mean(errors)



def minMaxScaling2(inputs, minInput, maxInput):
    return [(x - minInput) / (maxInput - minInput) for x in inputs]


def minMaxScaling(inputs):
    minInput = min(inputs)
    maxInput = max(inputs)
    return minInput, maxInput, [(x - minInput) / (maxInput - minInput) for x in inputs]
