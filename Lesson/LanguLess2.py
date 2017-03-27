#!/usr/bin/env python
# -*-coding:utf-8 -*-
from nltk.book import *

#计算一个给定的词在文本中出现的频率，结果以百分比表示
def percent(word, text):
    fdist = FreqDist(text)
    return fdist.freq(word)

print percent('walk', text5)
words = ['ab','dd','ab','cd','ff']
print percent('ab',words)
