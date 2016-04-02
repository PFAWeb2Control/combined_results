import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets.samples_generator import make_blobs

"""
ms_algo functions runs the meanshift algorithm
Parameters: 
-X[array] is the dataset array.
-bandwith[float] optinal
"""
def ms_algo(X, bandwidth=None):
    if(bandwidth==None):
        n_samples = X.shape[0]
        bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=n_samples)

    # Apply the meanshit algorithm from sklearn library
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(X)

    # collect from the meanshift algorithm the labels and the centers of the clusters
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_


    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique) #Number of clusters

    # Print section
    print("The number of clusters is: %d" % n_clusters_)

    print("The centers are:")
    for i in range(n_clusters_):
        print i,
        print cluster_centers[i]

    return cluster_centers    
