import numpy as np
from sklearn.cluster import Birch

#Initialiser le classificateur
def clf_init(b_factor = 50, threshold = 0.8):
    return Birch(branching_factor=b_factor, n_clusters=None, threshold=threshold, compute_labels=True)

#Ajouter des vecteurs a classer
#Data doit etre de dimension 2 (array ou list), meme pour ajouter un seul vecteur
#Retourne une tableau contenant le numero de clusters de chaque data
def clf_add_data(clf, data):
    if (type(data) is list):
        data = np.asarray(data)
    clf.partial_fit(np.asarray(data))
    return clf.labels_

#Retourne les centres de chaque cluster
def clf_cluster_centers(clf):
    return clf.subcluster_centers_

