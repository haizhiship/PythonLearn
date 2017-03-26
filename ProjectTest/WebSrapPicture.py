#!/user/bin/python
# coding=utf-8

"""
@file:WebSrapPicture.py
@time:2017/3/26 21:12
"""
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://bbs.voc.com.cn/topic-7721088-1-1.html")
bsObj = BeautifulSoup(html,"lxml")
#找到所有开头是"http："结尾是"jpg"的图片
imageLocation = bsObj.findAll("img",{"src":re.compile("^http:.*jpg$")})

file_num = 0
for i in imageLocation:
    #获取最后一个'/'出现的位置，然后从文件末尾切片获取文件名
    file_name = i.attrs['src'][i.attrs['src'].rfind('/') + 1:]
    if file_name.find('-') > 0:
        print(file_name)
        urlretrieve(i.attrs['src'], "G://scrappicture//" + file_name)
        file_num += 1

#3.0的print新写法
print('共保存了 %r 个文件' % file_num)