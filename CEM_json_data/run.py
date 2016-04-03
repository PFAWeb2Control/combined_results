# coding: utf-8

from corpusvectorizer import vectorize
from basic_CEM import clusterize
import simplejson as json
import numpy as np


def is_array_const(a):
    if len(a) == 0:
        return True
    val = a[0]
    for cur_val in a:
        if val != cur_val:
            return False

    return True

tweets = json.load(open("full_export.json", "r"))['tweets']
corpus = []
for i in range(100):
    corpus.append(tweets[i]['text'].encode('utf-8'))

#remove unused dimensions
del_index = []
batch_t = np.transpose(vectorize(corpus))
for i in range(len(batch_t)):
    if is_array_const(batch_t[i]):
        del_index.append(i)
batch_t = np.delete(batch_t, del_index, axis=0)
batch = np.reshape(np.transpose(batch_t), [len(batch_t[0]), len(batch_t), 1])

print(batch.shape)
clusterize(batch)


