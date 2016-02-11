import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets.samples_generator import make_blobs

def ms_algo(X, bandwidth=None):
    if(bandwidth==None):
        n_samples = X.shape[0]
        bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=n_samples)

    # Application de l'algorithme MeanShift
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(X)

    # Recuperation des etiquettes de chaque point et du centre de chaque regroupement
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_


    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique) # Nombre de regroupements

    # Affichage
    print("Nombre de regroupement(s): %d" % n_clusters_)

    print("Centre(s):")
    for i in range(n_clusters_):
        print i,
        print cluster_centers[i]

    return cluster_centers    
