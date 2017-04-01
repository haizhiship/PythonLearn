#!/usr/bin/env python
# -*-coding:utf-8 -*-
import re

def word_count(data):

    #定义一个字典
    adict = {}
    #使用正则表达式根据空格和符号来分隔词组,不是字母和数字就分隔
    list = re.findall(r"[\w']+", data)

    for word in list:
        #如果这个词在字典中有，则计数加1；否则新增一个计数
        if word in adict.keys():
            adict[word] += 1
        else:
            adict[word] = 1

    for key, value in adict.items():
         print  "单词 %s 的出现次数为 %d 次" % (key, value)

    #使用冒泡排序
    #将key值作为列表保持，以保证次序
    key_sort = []
    adict_copy = adict.copy()
    for i in range(len(adict)):
        key_str = adict.keys()[0]
        for key, value in adict.items():
            if value > adict[key_str]:
                key_str = key #保存最大的key值
        key_sort.append(key_str) #将最终的最大的key值保存
        adict.pop(key_str)   #最大的key值对弹出字典退出循环，不再考虑对其排序

    print "排序后的值为："
    for key in key_sort:
        print "单词 %s 出现的次数为 %d" %(key,adict_copy[key])
word_count('we are friends, we are bae 1 we we we are are bae bae 1')
