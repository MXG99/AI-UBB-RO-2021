def load_iris_data():
    from sklearn.datasets import load_iris
    data = load_iris()
    inputs = data['data']
    outputs = data['target']
    output_names = data['target_names']
    feature_names = list(data['feature_names'])
    sepal_lengths = [feat[feature_names.index('sepal length (cm)')] for feat in inputs]
    sepal_widths = [feat[feature_names.index('sepal width (cm)')] for feat in inputs]
    petal_lengths = [feat[feature_names.index('petal length (cm)')] for feat in inputs]
    petal_widths = [feat[feature_names.index('petal width (cm)')] for feat in inputs]
    return inputs, outputs, feature_names
