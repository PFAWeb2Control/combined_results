# coding: utf-8

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances

import nltk
from nltk.corpus import stopwords


def vectorize(tweets_list):
    corpus = []
    for t in tweets_list:
        corpus += [t["text"]]

    stwf=stopwords.words('french')
    stwf.append('les')
    vectorizer=CountVectorizer(stop_words=stwf)
    X = vectorizer.fit_transform(corpus)
    return X.toarray()

