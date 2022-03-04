import numpy as np


def dist(p1, p2):
    d = (sum((p1 - p2) ** 2)) ** 0.5
    return d


def kmeans(X, n_clusters, rseed=2):
    # 1. Randomly choose clusters
    rng = np.random.RandomState(rseed)
    i = rng.permutation(X.shape[0])[:n_clusters]
    centers = X[i]
    while True:
        # Labeluri in functie de distanta
        labels = []
        for data in X:
            distance = []
            for i in range(len(centers)):
                dis = dist(data, centers[i])
                distance.append(dis)
            labels.append(np.argmin(distance))
        labels = np.asarray(labels)

        # Recalcularea centroizilor in functie de medie
        new_centers = np.array([X[labels == i].mean(axis=0)
                                for i in range(n_clusters)])
        # Test Convergenta
        if np.all(centers == new_centers):
            break
        centers = new_centers

    return centers, labels
