#!/usr/bin/env python
# -*-coding:utf-8 -*-



#初始化累计值
total = 0

for i in range(1, 11):
    mul = 1
    for j in range(1,i+1):
        mul *=j
    #调试信息
    print j,mul
    total +=mul

print "The result is %d: " % total

