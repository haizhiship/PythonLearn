#!/user/bin/python
# coding=utf-8

"""
@author:出差在外
contact:898536955@qq.com
@file:SimpleBeautiFindAll.py
@time:2017/3/26 1:16

findAll的使用
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"lxml")

nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())
#get_text清除所有的标签