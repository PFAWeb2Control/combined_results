# K-means clustering with 

Here, a limited number of tweets are retrieved through tweepy API, then vectorized and clusterized 
with the K-means algorithm

## run
Main file to be run. It waits for a fixed number of tweets (currently 50) and then runs the algorithms.

## k_means 
TensorFlow implementation of the algorithm. Provides the clusterize() function.

## sk_vectorize
Vectorization method using sickit learn. Provides the vectorize() function.

## tweepy_import
tweepy API for retreiving tweets
