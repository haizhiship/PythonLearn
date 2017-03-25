#!/user/bin/python
# coding=utf-8

"""
@author:出差在外
contact:898536955@qq.com
@file:XML_make1.py
@time:2017/3/12 21:38
"""

from xml.sax.handler import ContentHandler
from xml.sax import parse

class TestHandler(ContentHandler):
    def startElement(self, name,attrs):
        print name, attrs.keys()

parse('../docs/website.xml', TestHandler())