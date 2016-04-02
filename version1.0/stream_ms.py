# coding: utf-8

import time
from tweepy_import import FilteredStream

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances

import nltk
from nltk.corpus import stopwords

from meanshift import ms_algo

np.set_printoptions(formatter={'float': '{: 0.2f}'.format})

class MyFilteredStream(FilteredStream):
    def __init__(self):

        self.criterias = {
            #You can choose some key words to look for by chaging the track's content
            "track": ['remaniement', 'Paris'],
            "locations": [-0.6389644,44.8111222,-0.5334955,44.9163535],
            "lang": [*]
        }
        FilteredStream.__init__(self, self.criterias, 10, "config.json")

    def action(self, tweets_list):
        corpus = []
        for t in tweets_list:
            corpus += [t["text"]]
            
        self.export('test.json',tweets_list)
        print(corpus)

        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(corpus)
        M,P=X.shape
        """
        #De-comment this section for further informations about the corpus, and the dictionnary
        print("taille du corpus : ",M)
        print("taille du vocabulaire : ",P)
        print("Mon vocabulaire")
        print(vectorizer.vocabulary_)
        print("Mes vecteurs")
        print (X.toarray())
        """
        """
        #We can calculate the euclidian distance between the different messages
        print("La distance euclidienne entre les diffents messages:")
        dist_corpus=euclidean_distances(X)
        print(dist_corpus)
        """
        #Suppression of french stopwords
        stwf=stopwords.words('french')
        stwf.append('les')
        vectorizer=CountVectorizer(stop_words=stwf)
        X = vectorizer.fit_transform(corpus)
        dico=vectorizer.vocabulary_
        Ns=len(dico)
        
        """
        #De-coment this section for further information about the dictionnar, the new array and the euclidian distance. 
        print("taille du vocabulaire apres suppression des stop_words : ",Ns)
        print("mon nouveau dictionnaire")
        print(dico)
        print("Mes nouveaux vecteurs")
        print(X.toarray())
        dist_corpus=euclidean_distances(X)
        print("ma nouvelle matrice de distance")
        print(dist_corpus)
        """
        #Apply the mean_shift algorithm on our new X after the suppression of the stopwords
        print("Résultats des l'algorithme Mean Shift")
        ms_algo(X.toarray(), None)
        quit()
#Call the method define previously with the meanshift algorithm with the current stream of tweets
stream = MyFilteredStream()
stream.stream()
