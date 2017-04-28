#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
5. 选择一个本章所描述的分类任务，如名字性别检测、文档分类、词性标注或对话行为分类。
使用相同的训练和测试数据，相同的特征提取器，建立该任务的两个分类器：决策树、朴素贝叶斯分类器。
比较你所选任务上这三个分类器的性能。
你如何看待如果你使用了不同的特征提取器，你的结果可能会不同？
'''
import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import brown
from nltk.corpus import names

# documents = [(list(movie_reviews.words(fileid)), category)
#     for category in movie_reviews.categories()
#     for fileid in movie_reviews.fileids(category)]
# random.shuffle(documents)
#
# all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
# word_features = all_words.keys()[:2000]
# def document_features(document):
#     document_words = set(document)
#     features = {}
#     for word in word_features:
#         features['contains(%s)' % word] = (word in document_words)
#     return features
#
# print document_features(movie_reviews.words('pos/cv957_8737.txt'))
# featuresets = [(document_features(d), c) for (d,c) in documents]
# train_set, test_set = featuresets[100:], featuresets[:100]
# classifier = nltk.NaiveBayesClassifier.train(train_set)

# suffix_fdist = nltk.FreqDist()
# for word in brown.words():
#     word = word.lower()
#     suffix_fdist.inc(word[-1:])
#     suffix_fdist.inc(word[-2:])
#     suffix_fdist.inc(word[-3:])
# common_suffixes = suffix_fdist.keys()[:100]
#
#
# def pos_features(word):
#     features = {}
#     for suffix in common_suffixes:
#         features['endswith(%s)' % suffix] = word.lower().endswith(suffix)
#     return features
#
#
# tagged_words = brown.tagged_words(categories='news')
# featuresets = [(pos_features(n), g) for (n,g) in tagged_words]
# size = int(len(featuresets) * 0.1)
# train_set, test_set = featuresets[size:], featuresets[:size]
# classifier = nltk.DecisionTreeClassifier.train(train_set)
# nltk.classify.accuracy(classifier, test_set)

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

classifier_tree = nltk.DecisionTreeClassifier.train(train_set)
print '决策树的开发测试准确率为 %s' % nltk.classify.accuracy(classifier_tree, devtest_set)
print '决策树的测试准确率为 %s' % nltk.classify.accuracy(classifier_tree, test_set)

