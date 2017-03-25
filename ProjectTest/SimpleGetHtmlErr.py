#!/user/bin/python
# coding=utf-8

"""
@author:出差在外
contact:898536955@qq.com
@file:SimpleGetHtmlErr.py
@time:2017/3/26 0:39
爬虫获取页面，多种情况的异常
"""
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return  None
    try:
        bsObj = BeautifulSoup(html.read(),"lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return  None
    return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)

