# coding: utf-8
import string
from nltk.stem.snowball import FrenchStemmer
from preprocess import Enleve_Accents
import urllib


url = "http://www.pallier.org/ressources/dicofr/liste.de.mots.francais.frgut.txt"
file_name = "dico.txt"
print "downloading the french dictionary from http://www.pallier.org/"
urllib.urlretrieve(url, "FrenchDictionary.txt")
 
 
stemmer = FrenchStemmer()

fs = open("FrenchDictionary.txt", 'r')
fd = open("StemmedFrenchDictionary.txt", 'w')
while 1:
	txt = fs.readline()
	if txt =='':
		break
	if txt[0] != '':
	
		txt = txt.lower()
		txt = ''.join(u for u in txt if u in string.ascii_letters)
		txt = Enleve_Accents(txt)
		txt = stemmer.stem(txt) + "\n"
		fd.write(txt)
import os
script = """
(cat StemmedFrenchDictionary.txt|uniq>monfichier.tmp) &&  mv -f monfichier.tmp FinalDictionary.txt
"""
os.system("bash -c '%s'" % script)



fs.close()
fd.close()


