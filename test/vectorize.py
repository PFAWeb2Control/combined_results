# coding: utf-8
from preprocess import set_sentence
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer



mon_fichier = open("FinalDictionary.txt", "r")

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(mon_fichier)
M,P=X.shape





def vectorize_(corpus):
	corpus_=[]
	for sentence in corpus:
		sentence=set_sentence(sentence)
		corpus_.append(sentence)
	return vectorizer.transform(corpus_)

if __name__ == '__main__':


	msg=("une phrase ", "un deuxieme phrase")
	print vectorize_(msg).toarray()	
