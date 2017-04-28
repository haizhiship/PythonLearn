#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
9. PP附件语料库是描述介词短语附着决策的语料库。
语料库中的每个实例被编码为
PP Attachment对象：
使用此子语料库，建立一个分类器，尝试预测哪些介词是用来连接一对给定的名词。
例如：给定的名词对team 和 researchers，分类器应该预测出介词 of。
更多的使用 PP 附件语料库的信息，参阅http://www.nltk.org/howto 上的语料库HOWTO。
'''
from nltk.corpus import ppattach
import nltk

ppattach.attachments('training')
inst = ppattach.attachments('training')[2]
print inst
print inst.noun1, inst.prep, inst.noun2
#根据PPAttachment的特征，将字典项作为特征项录入，将prep作为结果项，直接生成分类器所需的set
def gender_features(NounAndPrep):
    return ({'noun1': NounAndPrep.noun1,
             'noun2': NounAndPrep.noun2,
             'sent':NounAndPrep.sent,
             'verb':NounAndPrep.verb,
             'attachment':NounAndPrep.attachment
            }, NounAndPrep.prep)

print gender_features(inst)
PPAttach_set = [gender_features(inst) for inst in ppattach.attachments('training')]

#print len(PPAttach_set)  #20801  PPAttach总共有20801条
#生成开发测试验证集
PPAttach_train_set = PPAttach_set[1000:]
PPAttach_devtest_set = PPAttach_set[500:1000]
PPAttach_test_set = PPAttach_set[:500]


classifier = nltk.NaiveBayesClassifier.train(PPAttach_train_set)
print '决策树的开发测试准确率为 %s' % nltk.classify.accuracy(classifier, PPAttach_devtest_set)
print '决策树的测试准确率为 %s' % nltk.classify.accuracy(classifier, PPAttach_test_set)
print 'director %s conglomerate' % classifier.classify({'noun1':'director','noun2':'conglomerate'})
print 'team %s rearchers' % classifier.classify({'noun1':'researchers','noun2':'team'})
