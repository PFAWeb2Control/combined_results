#!/usr/bin/python2
# coding: utf-8
from __future__ import unicode_literals
import unicodedata
import numpy as np

# This test tries to cluster tweets with the sequential Birch algorithm.

from sklearn.feature_extraction.text import CountVectorizer
from tweepy_import import FilteredStream
from tweepy_import import TwitterUser
from nltk.corpus import stopwords
import vectorize as v
import sequential_birch as birch

config = "../../data-gathering-twitter/config.json"

# Using the FilteredStream class
class MyFilteredStream(FilteredStream):
    # Custom filtered stream, looking for tweets from Paris or mentioning
    # Paris

    def __init__(self):
        # Tweets from Paris OR mentioning 'Paris', in French
        
        self.criterias = {
            "track": ["Paris"], # Keywords filter
            "locations": [2.138472,48.774288,2.518187,48.965338], # Paris bounding box
            "lang": ["fr"] # In French
        }

        self.corpus_tot = []
        self.labels = np.asarray([])

        # Creates the classificator : threshold affect the clustering
        self.brc = birch.clf_init(threshold = 1.5)

        self.mon_fichier = open("FinalDictionary.txt", "r")

        self.vectorizer = CountVectorizer()
        X = self.vectorizer.fit_transform(self.mon_fichier)

        FilteredStream.__init__(self, self.criterias, 10, config)
        
    # We redefine the action() method, in order to treat our packs of tweets the
    # way we want.
    #
    # Here, we vectorize and cluster each pack of tweets.
    def action(self, tweets_list):

        corpus = []
        for tweet in tweets_list :
            # Deletes the accents
            tweet_str = tweet["text"].encode("utf-8")
            tweet_str = unicode(tweet_str,'utf-8')
            tweet_str = unicodedata.normalize('NFD',tweet_str).encode('ascii','ignore')
            corpus.append(tweet_str)
            self.corpus_tot.append(tweet_str)

        V = v.vectorize_(corpus)
        V = V.toarray()
        
        # Adding the new pack of tweets to the old clusters
        A = birch.clf_add_data(self.brc, V)
        self.labels = np.concatenate([self.labels,A])

        print "Nb tweets: %d" % len(self.corpus_tot)
        print "Nb clusters: %d" % len(birch.clf_cluster_centers(self.brc))

        clusters = [0]*len(birch.clf_cluster_centers(self.brc))
        for i in range(len(self.labels)):
            clusters[int(self.labels[i])] = clusters[int(self.labels[i])] + 1

        print "Clusters distribution:"
        print clusters

        C = birch.clf_cluster_centers(self.brc)

        for i in range(len(C)):
            if clusters[i] > 15:
                print "CLUSTER %d" % i
                P = CountVectorizer.inverse_transform(self.vectorizer, C[i])
                for j in range(len(P[0])):
                    print P[0][j],
                    print ",",
                print " "
        print " "


stream = MyFilteredStream()
stream.stream()
