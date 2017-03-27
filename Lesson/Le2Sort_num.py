#!/usr/bin/env python
# -*-coding:utf-8 -*-



def mysort(data, key, reveresed):

#先用自定义函数计算值
    calculate= []
    calculate = [key(i) for i in data]

#用冒泡法进行排序
    for i in range(len(calculate)):
         for j in range(i+1):
            if reveresed:
                if calculate[i] < calculate[j]:
                    calculate[i], calculate[j] = calculate[j], calculate[i]
            else:
                if calculate[i] > calculate[j]:
                    calculate[i], calculate[j] = calculate[j], calculate[i]
    return calculate







