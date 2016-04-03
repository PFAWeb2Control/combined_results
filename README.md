# combined_results

Contains tests of combining different modules to get tweets, vectorize them, and cluster them.
 
## sequential_birch_stream

Uses the sequential version of Birch algorithm to cluster tweets.

## vectorize_stream_ms

Use the MeanShift algorithme on the tweet stream after the vectorization using sklearn - that we later improoved.

## vectorize_clustering

Vectorization then clustering of a predefined corps chosen so that we can guess its number of clusters.

## k_means_tweepy_input

K-means clustering with tweeter input, to test actual use of TensorFlow code

## CEM_json_data

CEM clustering with tweets under JSON format, used to test the algorithm under different kinds of input.
