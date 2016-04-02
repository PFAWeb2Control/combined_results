# coding: utf-8
import nltk
import string
from nltk.corpus import stopwords
from itertools import chain
from nltk.stem import *
from nltk.stem.porter import *
from nltk.stem.snowball import FrenchStemmer

def tokinizer(sentence):
	return  (nltk.word_tokenize(sentence))


def WordList_to_sentence(wordlist):
	sentence=""
	for word in wordlist:
		sentence =sentence+ " " + word
	return sentence


def http (text):
	stopwords=[]
	stopwords.append([w for w in text if 'https' and 'http' in w ])
	mynewtext = [w for w in text if w not in stopwords[0]]
	return mynewtext

def stop (text):
	stop_words = stopwords.words('french')
	stop_words.append('les')
	stop_words.append('ceci')
	text =tokinizer(text)
	mynewtext = [w for w in text if w not in stop_words]
	return mynewtext

def punc (text):
	text = text.translate(None,string.punctuation)
	return text 

def remove (text):
	text=punc(text)
	base=tokinizer(text)
	ttp=http(base)
	sentence=WordList_to_sentence(ttp)
	stop_words=stop(sentence)
	sentence=(WordList_to_sentence(stop_words))
	return sentence

def tokinizer(sentence):
	return  (nltk.word_tokenize(sentence))


#base1=tokinizer(sentence)
#print base1 

def stemm(word):
	stemmer = FrenchStemmer()
	return stemmer.stem(word)

#stemmed1 = [stemm(s) for s in base1]
#print stemmed1


def WordList_to_sentence(wordlist):
	sentence=""
	for word in wordlist:
		sentence =sentence+ " " + word
	return sentence

#wordList = stemmed1	
#print WordList_to_sentence(wordList)

def sentence_stemmed(sentence):
	base=tokinizer(sentence)
	stemmed_=[stemm(s) for s in base]
	result=WordList_to_sentence(stemmed_)
	return result

def corpus_stemmed(corpus):
	corpus_stemmed=[]
	for sentence in corpus:
		corpus_stemmed.append(sentence_stemmed(sentence))
	return corpus_stemmed

def Remove_Arobase(sentence):
	stopwords=[]
	base = tokinizer(sentence)
	stopwords.append([w for w in base if w.startswith('@')])
	mynewtext = [w for w in base if w not in stopwords[0]]
	return WordList_to_sentence(mynewtext)

def Find_Hashtag(sentence):
	finded=[]
	finded_=[]
	words = sentence.split()
	finded=[w for w in words if w[0] in '#']
	for word in finded:
		finded_.append(word[1:])
	return finded_

def remove_hashtag(sentence):
	stopwords=[]
	base = tokinizer(sentence)
	stopwords.append([w for w in base if w.startswith('#')])
	mynewtext = [w for w in base if w not in stopwords[0]]
	return WordList_to_sentence(mynewtext)

def append_n(sentence,word,n):
	mynewtext=[]
	for i in range (n):
		mynewtext.append(word)
		bloc=(WordList_to_sentence(mynewtext))
	return  " "+bloc


def hashtag_transformation(sentence):
	result=sentence
	finded=Find_Hashtag(sentence)
	for w in finded :
		tmp=append_n(sentence,w,10)
		result=result+tmp
	return result
		
def set_sentence(sentence):
	sentence=hashtag_transformation(sentence)
	sentence=remove(sentence)
	sentence=sentence_stemmed(sentence)
	return sentence
	

	

if __name__ == '__main__':
	sentence="un test de suppression des mots non signifiant, ce test contient des liens, des hashtag et des arobase, https://google.fr @AROBASE #HASHTAG #ALORS #FINI"
	print "origin:"
	print sentence
	print "set:"
	print set_sentence(sentence)
