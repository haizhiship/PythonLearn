#!/usr/bin/env python
# -*-coding:utf-8 -*-

import  nltk
from nltk.corpus import brown
from nltk.book import text1, text2
from nltk.corpus import wordnet as wn

#2. 使用语料库模块处理austen-persuasion.txt。这本书中有多少词标识符？多少词类型？词标示符
# >>> aus = nltk.corpus.gutenberg.words('austen-persuasion.txt')
# >>> len(aus)
# 98171
# 词类型
# >>> len(set(aus))
# 6132
#练习ConditionalFreqDist
# cfd1 = nltk.ConditionalFreqDist(
#                                (genre, word)
#                                for genre in brown.categories()
#                                for word in brown.words(categories=genre))

#显示主题和单词的配对，比如 ('romance', 'mother'), ('romance', 'hated')
# genre_word = [(genre, word)
#               for genre in ['news', 'romance']
#               for word in brown.words(categories=genre)]
# cfd = nltk.ConditionalFreqDist(genre_word)
# print cfd.conditions()

'''
# 8、在名字语料库上定义一个条件频率分布，显示哪个首字母在男性名字中比在女性名字中更常用。

names = nltk.corpus.names

cfd = nltk.ConditionalFreqDist(
    (fileid, name[0])
    for fileid in names.fileids()
    for name in names.words(fileid))
cfd.plot()

FirstNum = []

for i in list(cfd['female.txt']):
    print '%r 在male中的个数为 %r，在female中的个数为 %r'\
          % (i, cfd['male.txt'][i], cfd['female.txt'][i])
    if cfd['male.txt'][i] > cfd ['female.txt'][i]:
           FirstNum.append(i)
    else:
        pass

print '首字母在男性名字中比在女性名字中更常用:%r' % FirstNum
'''
# 9. 挑选两个文本，研究它们之间在词汇、词汇丰富性、文体等方面的差异。
# 你能找出几个在这两个文本中词意相当不同的词吗？例如：在《白鲸记》与《理智与情感》中的 monstrous。

from nltk.corpus import wordnet as wn
wn.synsets('monstrous')  #获取包含'monstrous'的所有同义词集
wn.synset('monstrous.s.01').lemma_names  #获取词集内的所有词
text1.concordance("monstrous")
text2.concordance("affection")
print '文本名称为 %r 的词汇数为 %r，词汇丰富性为 %r' \
      % (text1.name, len(text1), len(text1)/len(set(text1)))
print '文本名称为 %r 的词汇数为 %r，词汇丰富性为 %r' \
      % (text2.name, len(text2), len(text2)/len(set(text2)))

modals = ['can', 'could', 'may', 'might', 'must', 'will']
genres = [text1,text2]
fdist = nltk.FreqDist([w.lower() for w in text1])
print '在text1中的的情态动词频数为：'
for m in modals:
    print m +':',fdist[m]
print '在text2中的的情态动词频数为：'
fdist = nltk.FreqDist([w.lower() for w in text2])
for m in modals:
    print m +':',fdist[m]

print 'monstrous在text1中的相似词为：'
text1.similar('monstrous')
print 'monstrous在text2中的相似词为：'
text2.similar('monstrous')
print '\n'

#15. 写一个程序，找出所有在布朗语料库中出现至少3次的词
from nltk.corpus import brown

all_word = [w.lower() for w in brown.words() if w.isalpha()]
fdist = nltk.FreqDist(all_word)
freqList = list(fdist.items())
word = []
print  '所有在布朗语料库中出现至少3次的词有：'
for w in freqList:
    if w[1] > 3:
        word.append(w[0])
print (word)
print '\n'

#17. 写一个函数，找出一个文本中最常出现的50 个词，停用词除外。 95574
from nltk.corpus import stopwords
def text_stopword(text):
    stopwords = nltk.corpus.stopwords.words('english')
    word = [w for w in text if w.isalpha() and w.lower() not in stopwords]
    fdist = nltk.FreqDist(word)
    sorter_word = fdist.keys()
    for i in range(50):
        print sorter_word[i]
print '文本中最常出现的50 个词，停用词除外:'
text_stopword(text1)







