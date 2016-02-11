# coding: utf-8
#corpus=['Rendez-vous au Boogie Spirit Festival ce weekend à Illkirch','Samedi 6 Février, à la ComedieFr pour voir "La Double inconstance" de Marivaux!','Toujours personne pour le 104paris ce soir ? Une pièce pleine d\'humour qui mêle théâtre et danse, ça ne vous dit pas ?','Pour les fans de réécritures de contes, ne manquez pas ‘The Forbidden Wish’ le 23 février prochain!']

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

        # Tweets from Bordeaux OR mentioning 'Paris'
        self.criterias = {
            "track": ['remaniement', 'Paris'],
            "locations": [-0.6389644,44.8111222,-0.5334955,44.9163535] 
        }
        FilteredStream.__init__(self, self.criterias, "config.json")

    def action(self, tweets_list):
        corpus = []
        for t in tweets_list:
            corpus += [t["text"]]

        print(corpus)
            
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(corpus)
        M,P=X.shape
        
        print("taille du corpus : ",M)
        print("taille du vocabulaire : ",P)
        print("Mon vocabulaire")
        print(vectorizer.vocabulary_)
        print("Mes vecteurs")
        print (X.toarray())
        
        #On peut calculer la distance euclidienne entre ces différents messages

        print("La distance euclidienne entre les diffents messages:")
        dist_corpus=euclidean_distances(X)
        print(dist_corpus)
        
        #on peut calculer la distance d'un nouveau message à ce  corpus
        print("distance dun nouveau message non evenement a ce corpus")
        msg="Luc Fortin fait son entrée au Cabinet des ministres. Il s’occupera du Loisir et du Sport"
        y=vectorizer.transform([msg])
        dist_to_y=euclidean_distances(y,X)
        print(dist_to_y)

        #on peut calculer la distance d'un nouveau message à ce  corpus
        print("distance dun nouveau message evenement a ce corpus")
        msg="Sortie ce soir"
        y=vectorizer.transform([msg])
        dist_to_y=euclidean_distances(y,X)
        print(dist_to_y)

        #on peut réduire la taille du vocabulaire
        #suppresion des mots très usuels (stop words)
        #utilisation de l'argument stop_words de la classe CountVectorizer

        stwf=stopwords.words('french')
        stwf.append('les')
        vectorizer=CountVectorizer(stop_words=stwf)
        X = vectorizer.fit_transform(corpus)
        dico=vectorizer.vocabulary_
        Ns=len(dico)
        print("taille du vocabulaire apres suppression des stop_words : ",Ns)
        print("mon nouveau dictionnaire")
        print(dico)
        print("Mes nouveaux vecteurs")
        print(X.toarray())
        dist_corpus=euclidean_distances(X)
        print("ma nouvelle matrice de distance")
        print(dist_corpus)

        print("Résultats des l'algorithme Mean Shift")
        ms_algo(X.toarray(), None)
        quit()
        
stream = MyFilteredStream()
stream.stream(10, 4)

