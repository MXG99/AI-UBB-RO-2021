def normalisation(trainData, testData):
    from sklearn.preprocessing import StandardScaler
    # z = (x - u) / s ( u - medie, s - deviatia standard
    scaler = StandardScaler()
    scaler.fit(trainData)
    normalised_train_data = scaler.transform(trainData)
    normalised_test_data = scaler.transform(testData)
    return normalised_train_data, normalised_test_data
