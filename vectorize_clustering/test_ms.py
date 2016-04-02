# coding: utf-8
corpus=['Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Paris capitale de la terre','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux','Le vin de Bordeaux', 'jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin','jaime pas le vin', 'jaime pas le vin', 'jaime pas le vin', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'j toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale', 'jm toutes les capitale' ]

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances
import nltk
from nltk.corpus import stopwords

np.set_printoptions(formatter={'float': '{: 0.2f}'.format})
#Apply the vectorization on the corpus.
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
M,P=X.shape
"""
#de-coment this section for further informations about the corpus, vocabulary and the vectors

print("taille du corpus : ",M)
print("taille du vocabulaire : ",P)
print("Mon vocabulaire")
print(vectorizer.vocabulary_)
print("Mes vecteurs")
print (X.toarray())
"""
#remove the french stopwords 
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

#apply the meanshift algorithm
clusters = ms_algo(X.toarray(), 1.95)

# the index of the center of the clusters
n = clusters.shape[0]
for i in range(n):
    k = np.argmax(clusters[i])
    print k

    


