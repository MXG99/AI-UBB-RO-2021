def bag_of_words(train_inputs, test_inputs):
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer()

    train_features = vectorizer.fit_transform(train_inputs)
    test_features = vectorizer.transform(test_inputs)
    print('vocab: ', vectorizer.get_feature_names()[:10])
    print('features: ', train_features.toarray()[:3][:10])

    return train_features, test_features


def tf_idf(train_inputs, test_inputs):
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer(max_features=50)

    train_features = vectorizer.fit_transform(train_inputs)
    test_features = vectorizer.transform(test_inputs)

    # vocabulary from the train data
    print('vocab: ', vectorizer.get_feature_names()[:10])
    # extracted features
    print('features: ', train_features.toarray()[:3])

    return train_features, test_features


def feature_computation(model, data):
    import numpy as np
    features = []
    phrases = [phrase.split() for phrase in data]
    for phrase in phrases:
        # compute the embeddings of all the words from a phrase (words of more than 2 characters) known by the model
        vectors = [model[word] for word in phrase if (len(word) > 2) and (word in model.vocab.keys())]
        if len(vectors) == 0:
            result = [0.0] * model.vector_size
        else:
            result = np.sum(vectors, axis=0) / len(vectors)
        features.append(result)
    return features


def word_2_vec(train_inputs, test_inputs):
    import gensim
    import os
    crt_dir = os.getcwd()
    model_path = os.path.join(crt_dir, 'models', 'GoogleNews-vectors-negative300.bin')
    word2vecModel300 = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)
    print(word2vecModel300.most_similar('support'))
    print("vec for house: ", word2vecModel300["house"])

    train_features = feature_computation(word2vecModel300, train_inputs)
    test_features = feature_computation(word2vecModel300, test_inputs)

    return train_features, test_features


