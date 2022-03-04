computedOutputs = [[3, 7, 13], [8, 16, 27], [15, 23, 35]]
realOutputs = [[3, 8, 15], [9, 16, 25], [15, 24, 35]]

mean_error = 0
for computed, real in zip(computedOutputs, realOutputs):
    k = len(computed)
    mean_element_error = sum(abs(r - c) for r, c in zip(computed, real)) / k
    mean_error += mean_element_error
mean_error /= len(computedOutputs)
print(mean_error)