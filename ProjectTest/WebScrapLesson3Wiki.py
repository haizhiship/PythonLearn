#!/user/bin/python
# coding=utf-8

"""
@file:WebScrapLesson3Wiki.py
@time:2017/3/26 11:38
从Wiki网站获取采集词条链接
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, random, datetime


random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
    bsObj = BeautifulSoup(html)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                                                            href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    #在列表中用随机数取一个词条链接
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)