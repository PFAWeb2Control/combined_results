# coding: utf-8

#A set of sentences incorporating the corpse of our data.
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

print("The size of the corpus: ",M)
print("The size of the vocabulary : ",P)
print("My vocabulary")
print(vectorizer.vocabulary_)
print("My vectors")
print (X.toarray())
"""
#remove the french stopwords 
stwf=stopwords.words('french')
stwf.append('les')
vectorizer=CountVectorizer(stop_words=stwf)
X = vectorizer.fit_transform(corpus)
dico=vectorizer.vocabulary_
Ns=len(dico)

print("The size of our vocabulary after the suppression of the french stopwords: ",Ns)
print("My new dictionnary:")
print(dico)
print("My new vectors:")
print(X.toarray())

#apply the meanshift algorithm
clusters = ms_algo(X.toarray(), 1.95)

# the index of the center of the clusters
n = clusters.shape[0]
for i in range(n):
    k = np.argmax(clusters[i])
    print k

    


