#!/usr/bin/env python
# -*-coding:utf-8 -*-

'''
2. 使用任何本章所述的三种分类器之一，以及你能想到的特征，
尽量好的建立一个名字性别分类器。从将名字语料库分成 3个子集开始：
500 个词为测试集，500个词为开发测试集，剩余6900个词为训练集。
然后从示例的名字性别分类器开始，逐步改善。使用开发测试集检查你的进展。
一旦你对你的分类器感到满意，在测试集上检查它的最终性能。
相比在开发测试集上的性能，它在测试集上的性能如何？这是你期待的吗？
'''
import nltk
from nltk.corpus import names
import random

def gender_features(word):
    return {'suffix1': word[-1:],
             'suffix2': word[-2:],
            'len':len(word)}

names = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)

train_names = names[1000:]
devtest_names = names[500:1000]
test_names = names[:500]
train_set = [(gender_features(n), g) for (n,g) in train_names]
devtest_set = [(gender_features(n), g) for (n,g) in devtest_names]
test_set = [(gender_features(n), g) for (n,g) in test_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print '朴素贝叶斯的开发测试准确率为 %s' % nltk.classify.accuracy(classifier, devtest_set)
print '朴素贝叶斯的测试准确率为 %s' % nltk.classify.accuracy(classifier, test_set)
#显示总共有多少个名字判断错误
# errors = []
# for (name, tag) in devtest_names:
#     guess = classifier.classify(gender_features(name))
#     if guess != tag:
#         errors.append( (tag, guess, name) )
# for (tag, guess, name) in sorted(errors): # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
#     print 'correct=%-8s guess=%-8s name=%-30s' % (tag, guess, name)


