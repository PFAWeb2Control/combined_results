#!/usr/bin/python2
# coding: utf-8
from __future__ import unicode_literals
import unicodedata
import numpy as np

# This example script shows how to use the tweepy_import wrapper written for
# the project

from sklearn.feature_extraction.text import CountVectorizer
from tweepy_import import FilteredStream
from tweepy_import import TwitterUser
from nltk.corpus import stopwords
import vectorize as v
import birch

config = "../../data-gathering-twitter/config.json"

# An example using the TwitterUser class
user = TwitterUser('interior', config)

tweets = []
for t in user.tweets(5):
    tweets += [t.text]

# Prints a list of five tweets
for t in tweets:
    print t

# Another example, with the FilteredStream class
class MyFilteredStream(FilteredStream):
    # Custom filtered stream, looking for tweets from Bordeaux or mentioning
    # Paris, and printing them in a formatted way

    def __init__(self):
        # Tweets from Bordeaux OR mentioning 'Paris', in ANY language
        
        self.criterias = {
            "track": ["Paris"], # Keywords filter
            "locations": [2.138472,48.774288,2.518187,48.965338], # Paris bounding box
            "lang": ["fr"] # In French
        }

        self.corpus_tot = []
        self.labels = np.asarray([])
        self.brc = birch.clf_init(threshold = 1)

        self.mon_fichier = open("FinalDictionary.txt", "r")
        #stwf=stopwords.words('french')
        #stwf.append('les')
        #stwf.append("rt")
        self.vectorizer = CountVectorizer()
        X = self.vectorizer.fit_transform(self.mon_fichier)

        FilteredStream.__init__(self, self.criterias, 10, config)

    # We redefine the action() method, in order to treat our packs of tweets the
    # way we want.
    #
    # Here, we print them in a special way.
    def action(self, tweets_list):

        corpus = []
        for tweet in tweets_list :
            # Formatted printing
            tweet_str = tweet["text"].encode("utf-8")
            tweet_str = unicode(tweet_str,'utf-8')
            tweet_str = unicodedata.normalize('NFD',tweet_str).encode('ascii','ignore')
            corpus.append(tweet_str)
            self.corpus_tot.append(tweet_str)

        #print(corpus)
        V = v.vectorize_(corpus)
        V = V.toarray()
        
        #for i in range(len(V)):
        #    print max(V[i])
            
        A = birch.clf_add_data(self.brc, V)
        self.labels = np.concatenate([self.labels,A])

        #print self.labels
        print len(self.corpus_tot)
        print len(birch.clf_cluster_centers(self.brc))

        clusters = [0]*len(birch.clf_cluster_centers(self.brc))
        for i in range(len(self.labels)):
            clusters[int(self.labels[i])] = clusters[int(self.labels[i])] + 1

        print clusters

        #for i in range(len(self.labels)):
        #    if np.argmax(clusters) == self.labels[i]:
        #        print self.corpus_tot[i]

        #print "Centre:"
        C = birch.clf_cluster_centers(self.brc)

        for i in range(len(clusters)):
            if clusters[i] > 4:
                print "CLUSTER %d" % i
                P = CountVectorizer.inverse_transform(self.vectorizer, C[i])
                print P
                print "C[i]"
                print C[i]
                print max(C[i])
                print np.argmax(C[i])
                print "P_max"
                P_max = [0]*len(C[i])
                P_max[np.argmax(C[i])] = 10
                P_max = CountVectorizer.inverse_transform(self.vectorizer, P_max)
                print "Pmax :"
                print P_max
                print "TWEET"
                for j in range(len(self.labels)):
                    if self.labels[j] == i:
                        print self.corpus_tot[j]

        #print C
        #for i in range(len(C)):
            #print max(C[i])
        #print np.argmax(clusters)
        #print "CENTRE:"
        #print CountVectorizer.inverse_transform(self.vectorizer, C[np.argmax(clusters)])
        #print "Max: %f" % max(C[np.argmax(clusters)])
        #print "Indice max: %d" % np.argmax(C[np.argmax(clusters)])


stream = MyFilteredStream()
stream.stream()
