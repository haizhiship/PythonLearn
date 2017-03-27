#!/usr/bin/env python
# -*-coding:utf-8 -*-

#数字合法性检验
def judge_num(lst):

    #先判断是否为三个值
    if not len(lst) == 3:
       return "The length is not three"

    #判断是否全部为数字
    for i in lst:
        if not i.isdigit():
            return "Not digit"
        else:
            continue

    return "OK"

#对列表进行排序
def sort_int(lst):
    l = []
    lst = map(int, lst)
    lst.sort()
    l = [int(item) for item in lst]
    return l

#主函数
def input_int():
    lst = []
    input_str = raw_input("Please input 3 number:")
    lst = input_str.split(",")

    judge_str=judge_num(lst)
    if  judge_str != "OK":
        print judge_str
        return
    else:
        print "The number list is %s" % sort_int(lst)

#调用主函数
input_int()


