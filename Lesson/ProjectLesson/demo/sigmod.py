#!/user/bin/python
# coding=utf-8
import math



def sigmod(x):
    a = math.exp(-x)
    y = round(1/(1+a), 4)
    return y


def add(x, y):
    return x+y

