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
        print("The size of the corpus: ",M)
        print("The size of the vocabulary: ",P)
        print("My vocabulary")
        print(vectorizer.vocabulary_)
        print("My vectors")
        print (X.toarray())
        """
        """
        #We can calculate the euclidian distance between the different messages
        print("The euclidean distance between the different messages:")
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
        print("The size of the vocabulary after the suppression of the stopwords : ",Ns)
        print("My new dictionnary")
        print(dico)
        print("My new vectors")
        print(X.toarray())
        dist_corpus=euclidean_distances(X)
        print("My new matrix of distance")
        print(dist_corpus)
        """
        #Apply the mean_shift algorithm on our new X after the suppression of the stopwords
        print("The results of the Mean Shift algorithm \n")
        ms_algo(X.toarray(), None)
        quit()
#Call the method define previously with the meanshift algorithm with the current stream of tweets
stream = MyFilteredStream()
stream.stream()
