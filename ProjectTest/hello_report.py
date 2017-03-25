#!/user/bin/python
# coding=utf-8

"""
@author:出差在外
contact:898536955@qq.com
@file:hello_report.py
@time:2017/3/12 11:54
"""

from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(100,100)
s = String(50, 50, 'Hello, World!', textAnchor='middle')

d.add(s)

renderPDF.drawToFile(d, '../docs/hello.pdf', 'A simple PDF file')