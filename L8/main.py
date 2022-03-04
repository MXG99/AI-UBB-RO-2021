from feature_extractors import tf_idf, word_2_vec


def kmeans_iris():
    from kmeans import kmeans
    import matplotlib.pyplot as plt
    from sklearn.datasets import load_iris
    iris = load_iris()
    data = iris.data[:, :2]
    centers, labels = kmeans(data, 3)
    plt.scatter(data[:, 0], data[:, 1], c=labels,
                s=50, cmap='viridis')
    plt.show()


def run():
    import numpy as np
    from data_reader import data_reader
    from feature_extractors import bag_of_words
    import os
    crtDir = os.getcwd()
    fileName = os.path.join(crtDir, 'data', 'reviews_mixed.csv')
    data = data_reader(fileName)
    inputs = [data[i][0] for i in range(len(data))]
    outputs = [data[i][1] for i in range(len(data))]
    labelNames = list(set(outputs))

    # Splitting the data
    np.random.seed(7)

    no_samples = len(inputs)
    indexes = [i for i in range(no_samples)]
    train_sample = np.random.choice(indexes, int(0.8 * no_samples), replace=False)
    test_sample = [i for i in indexes if i not in train_sample]

    train_inputs = [inputs[i] for i in train_sample]
    train_outputs = [outputs[i] for i in train_sample]
    test_inputs = [inputs[i] for i in test_sample]
    test_outputs = [outputs[i] for i in test_sample]

    kmeans_iris()

    print("-BAG OF WORDS-")
    # Bag of words
    train_features_bw, test_features_bw = bag_of_words(train_inputs, test_inputs)

    print("\n\n\n-TF-IDF-")
    # TF-IDF
    train_features_tf_idf, test_features_tf_idf = tf_idf(train_inputs, test_inputs)

    print("\n\n\n-w2v-")
    # Word2vec
    # train_features_w2v, test_features_w2v = word_2_vec(train_inputs, test_inputs)

    # Kmeans on Iris data

    bag_of_words_classifier(labelNames, test_features_bw, test_outputs, train_features_bw)

    tf_ids_classifier(labelNames, test_features_tf_idf, test_outputs, train_features_tf_idf)

    # w2v_classifier(labelNames, test_features_w2v, test_outputs, train_features_w2v)

    print("END")


def w2v_classifier(labelNames, test_features_w2v, test_outputs, train_features_w2v):
    from sklearn.cluster import KMeans
    unsupervised_classifier = KMeans(n_clusters=2, random_state=0)
    unsupervised_classifier.fit(train_features_w2v)
    computed_test_indexes = unsupervised_classifier.predict(test_features_w2v)
    computed_test_outputs = [labelNames[value] for value in computed_test_indexes]
    from sklearn.metrics import accuracy_score
    print("Accuracy W2V: ", accuracy_score(test_outputs, computed_test_outputs))


def tf_ids_classifier(labelNames, test_features_tf_idf, test_outputs, train_features_tf_idf):
    from sklearn.cluster import KMeans
    unsupervised_classifier = KMeans(n_clusters=2, random_state=0)
    unsupervised_classifier.fit(train_features_tf_idf)
    computed_test_indexes = unsupervised_classifier.predict(test_features_tf_idf)
    computed_test_outputs = [labelNames[value] for value in computed_test_indexes]
    from sklearn.metrics import accuracy_score
    print("Accuracy TF-IDF: ", accuracy_score(test_outputs, computed_test_outputs))
    print(test_outputs)
    print(computed_test_outputs)


def bag_of_words_classifier(labelNames, test_features_bw, test_outputs, train_features_bw):
    from sklearn.cluster import KMeans
    from sklearn.metrics import accuracy_score
    unsupervised_classifier = KMeans(n_clusters=2, random_state=0)
    unsupervised_classifier.fit(train_features_bw)
    computed_test_indexes = unsupervised_classifier.predict(test_features_bw)
    computed_test_outputs = [labelNames[value] for value in computed_test_indexes]
    print("Accuracy BW: ", accuracy_score(test_outputs, computed_test_outputs))


run()
