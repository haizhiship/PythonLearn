#!/usr/bin/env python
# -*-coding:utf-8 -*-

import  nltk
from nltk.corpus import brown


# cfd1 = nltk.ConditionalFreqDist(
#                                (genre, word)
#                                for genre in brown.categories()
#                                for word in brown.words(categories=genre))

#显示主题和单词的配对，比如 ('romance', 'mother'), ('romance', 'hated')
genre_word = [(genre, word)
              for genre in ['news', 'romance']
              for word in brown.words(categories=genre)]
cfd = nltk.ConditionalFreqDist(genre_word)
print cfd.conditions()
