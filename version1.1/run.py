# coding: utf-8

from sk_vectorize import vectorize
from k_means import clusterize
from tweepy_import import FilteredStream



class OneBatchStream(FilteredStream):
    def __init__(self):

        # Tweets from Bordeaux OR mentioning 'Paris'
        self.criterias = {
            "track": ['remaniement', 'Paris'],
            "locations": [-0.6389644,44.8111222,-0.5334955,44.9163535] 
        }
        FilteredStream.__init__(self, self.criterias, "config.json")

    def action(self, tweets_list):
        [centroids, affectations] = clusterize(vectorize(tweets_list))
        print "Centroids:"
        print centroids
        print "Affectations:"
        print affectations

        quit()
        
OneBatchStream().stream(50)
