from data_utils import normalisation


def sklearn_log_regress(train_inputs, train_outputs, test_inputs, test_outputs):
    from sklearn import linear_model
    from sklearn.metrics import classification_report
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import confusion_matrix
    classifier = linear_model.LogisticRegression(multi_class='ovr')
    classifier.fit(train_inputs, train_outputs)
    predictions = classifier.predict(test_inputs)
    print("Predictii")
    print(predictions)

    print("Valori reale")
    print(test_outputs)
    output_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

    print(confusion_matrix(test_outputs, predictions))
    print(classification_report(test_outputs, predictions, target_names=output_names))
    print(accuracy_score(test_outputs, predictions))


def manual_log_regress(train_inputs, train_outputs, test_inputs, test_outputs):
    from log_regress import LogisticRegression
    from sklearn.metrics import classification_report
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import confusion_matrix
    classifier = LogisticRegression()
    for index in range(len(set(train_outputs))):
        train_outputs_binary = [1 if train_outputs[i] == index else 0 for i in range(len(train_outputs))]
        classifier.fit(train_inputs, train_outputs_binary)
    predictions = classifier.predict(test_inputs)
    print("Predictii")
    print(predictions)

    print("Valori reale")
    print(test_outputs)

    output_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

    print(confusion_matrix(test_outputs, predictions))
    print(classification_report(test_outputs, predictions, target_names=output_names))
    print(accuracy_score(test_outputs, predictions))

def run():
    """
    Runner method
    """
    from data_loader import load_iris_data
    import numpy as np

    inputs, outputs, feature_names = load_iris_data()

    # Splitting the data
    np.random.seed(7)
    indexes = [i for i in range(len(inputs))]
    train_sample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    test_sample = [i for i in indexes if i not in train_sample]

    train_inputs = [inputs[i] for i in train_sample]
    train_inputs = np.array(train_inputs).tolist()
    train_outputs = [outputs[i] for i in train_sample]

    test_inputs = [inputs[i] for i in test_sample]
    test_inputs = np.array(test_inputs).tolist()
    test_outputs = [outputs[i] for i in test_sample]

    # Data normalisation
    train_inputs, test_inputs = normalisation(train_inputs, test_inputs)

    print("Logistic regression cu tool:")
    # Sklearn logistic regression
    sklearn_log_regress(train_inputs, train_outputs, test_inputs, test_outputs)

    print("\nLogistic regression manual:")
    # Manual logistic regression
    manual_log_regress(train_inputs, train_outputs, test_inputs, test_outputs)


run()
