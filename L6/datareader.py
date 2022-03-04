import csv


def loadData(fileName, inputVariable1, inputVariable2, outputVariable):
    data = []
    dataNames = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                data.append(row)
            line_count += 1
    selectedVariable1 = dataNames.index(inputVariable1)
    selectedVariable2 = dataNames.index(inputVariable2)
    inputs = [[float(data[i][selectedVariable1]), float(data[i][selectedVariable2])] for i in range(len(data))]
    selectedOutput = dataNames.index(outputVariable)
    outputs = [float(data[i][selectedOutput]) for i in range(len(data))]
    return inputs, outputs
