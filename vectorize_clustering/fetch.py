#!/usr/bin/python2
# coding: utf-8
from __future__ import unicode_literals

# Tweets import script

from tweepy_import import FilteredStream

SIZE = 1000 # Number of tweets saved in a file

class MyFilteredStream(FilteredStream):

    def __init__(self):

		# Search criterias
        self.criterias = {
            "track": ["Paris", "Bordeaux"],
            "locations": [-0.6389644,44.8111222,-0.5334955,44.9163535],
            "lang": ["fr"]
        }
        FilteredStream.__init__(self, self.criterias, SIZE, "../config.json")
        self.tweets = []
        self.num_export = 0

    def action(self, tweets_list):
        self.tweets += tweets_list
        # print("Missing : " + str(SIZE - len(self.tweets)))

        if len(self.tweets) >= SIZE:
            exp = []
            for i in range(0, SIZE):
                exp += [self.tweets.pop(0)]

            self.export('tweets-' + str(self.num_export) + '.json', exp)
            self.num_export += 1

stream = MyFilteredStream()
stream.stream()
