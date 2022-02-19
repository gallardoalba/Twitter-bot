#!/usr/bin/python

import pickle

tags = ["#hastag1","#hashtag2"]

hashtags = {"username": tags}


with open("hashtags.pickle","wb") as handle:
	pickle.dump(hashtags,handle)
