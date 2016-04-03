# coding: utf-8
#corpus=['Rendez-vous au Boogie Spirit Festival ce weekend à Illkirch','Samedi 6 Février, à la ComedieFr pour voir "La Double inconstance" de Marivaux!','Toujours personne pour le 104paris ce soir ? Une pièce pleine d\'humour qui mêle théâtre et danse, ça ne vous dit pas ?','Pour les fans de réécritures de contes, ne manquez pas ‘The Forbidden Wish’ le 23 février prochain!']

from __future__ import unicode_literals
import time
from tweepy_import import FilteredStream

import numpy as np
import threading
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances


import nltk
from nltk.corpus import stopwords

from birch import birch_algo

np.set_printoptions(formatter={'float': '{: 0.2f}'.format})

class MyFilteredStream(FilteredStream):
    def __init__(self):

        self.criterias = {
            "track": ['Khomri', 'Paris', 'Travail', 'Myriam', 'ElKhomri'],
            "locations": [2.138472,48.774288,2.518187,48.965338],
            "lang": ["fr"]
        }
        FilteredStream.__init__(self, self.criterias, 10, "config.json")

    def action(self, tweets_list):
        corpus = []
        for tweet in tweets_list:
            #corpus += [t["text"]]
            tweet_str = tweet["text"].encode("utf-8")
            tweet_str = unicode(tweet_str,'utf-8')
            corpus.append(tweet_str)

        print(corpus)

        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(corpus)
        M,P=X.shape


        dist_corpus=euclidean_distances(X)

        stwf=stopwords.words('french')
        stwf.append('les')
        vectorizer=CountVectorizer(stop_words=stwf)
        X = vectorizer.fit_transform(corpus)
        dico=vectorizer.vocabulary_
        
        #Tous les print regroupés ici
        
        print("Results of Birch algorithm")

        clusters = birch_algo(X.toarray(), None)
        quit()

stream = MyFilteredStream()
stream.stream()
