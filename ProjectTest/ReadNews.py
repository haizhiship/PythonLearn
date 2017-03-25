#!/user/bin/python
# coding=utf-8

"""
@author:出差在外
contact:898536955@qq.com
@file:ReadNews.py
@time:2017/3/25 20:32
"""
#从新闻接口获取新闻内容
#使用NNTP协议
from nntplib import *

s = NNTP('web.aioe.org')

(resp, count, first, last, name) = s.group('comp.lang.python')
(resp, subs) = s.xhdr('subject', (str(first)+'-'+str(last)))

for subject in subs[-10:]:
    print(subject)

number = raw_input('Which article do you want to read? ')
(reply, num, id, list) = s.body(str(number))

for line in list:
    print(line)
