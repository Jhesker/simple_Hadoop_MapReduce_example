#!/usr/bin/env python
import sys
import string
# importing the sklearn stopwords
from sklearn.feature_extraction import stop_words

stops = set(stop_words.ENGLISH_STOP_WORDS)

# addition of code to remove puctuation from the mapped words
exclude = set(string.punctuation)

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace jhesker added lowercase
    line = line.strip().lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format edited by jhesker to ensure that stop words were removed
    for word in words:
	if word not in stops:
		if word not in exclude:
       			 print '%s\t%s' % (word, "1")
