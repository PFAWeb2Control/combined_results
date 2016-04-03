from itertools import cycle
from time import time
import numpy as np

from sklearn.cluster import Birch
   
    
def birch_algo(X, threshold=1.7, clustering=None):
        birch = Birch(threshold=threshold, n_clusters=clustering)
        t = time()
        birch.fit(X)
        time_ = time() - t
        labels = birch.labels_
        centroids = birch.subcluster_centers_
        n_clusters = np.unique(labels).size
        print(" The number of clusters is : %d" % n_clusters)
