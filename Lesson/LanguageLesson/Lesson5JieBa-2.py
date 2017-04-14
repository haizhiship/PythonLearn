#!/usr/bin/env python
# -*-coding:utf-8 -*-

from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import jieba
import jieba.analyse

#分析网页，提取正文
soup = BeautifulSoup(open('E:/data/article-9776-1.html'),"html.parser")
html_text = soup.text
start = html_text.rfind('你一定听过Google Brain')
end = html_text.find('“这个领域大有可为”。')
text_find = html_text[start:end+11]
print("取词结果：", text_find)

#对正文进行分词
jieba.load_userdict("E:\\data\\jieba.txt")
html_text_split = jieba.cut(text_find)
print ("分词结果：" + "/".join(html_text_split))
#计算关键词
html_text_key = jieba.analyse.extract_tags(text_find, topK = 10, withWeight = False, allowPOS = ())
print("关键词是：", html_text_key)