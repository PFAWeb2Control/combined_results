# CEM clustering with tweets under JSON format

Here, a limited number of tweets are retrieved through tweepy API, then vectorized and clusterized 
with the K-means algorithm

## run
Main file to be run. It reads a fixed number of tweets (currently 100) from the json file, and then runs the algorithms.

## basic_CEM
TensorFlow implementation of the  CEM algorithm. Provides the clusterize() function.

## corpusvectorizer
simple vectorization method using sickit learn. Provides the vectorize() function.

