#!/user/bin/python
# coding=utf-8

"""
@author:出差在外
contact:898536955@qq.com
@file:util.py
@time:2017/3/11 16:10
"""

def lines(file):
    for line in file :
        yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield  ''.join(block).strip()
            block = []