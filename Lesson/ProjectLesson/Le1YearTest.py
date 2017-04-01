#!/usr/bin/env python
# -*-coding:utf-8 -*-

#对闰年的判断
def IsLeapYear(year):
    if int(year) % 4 == 0:
        return True
    else:
        return False

#合法性校验
def judge_input(input_year):
    if len(input_year) != 4:
        return  False
    elif not input_year.isdigit():
        return  False
    else:
        return True

#主函数
def start():
    input_year = raw_input("Please input year: ")
    while judge_input(input_year) == False:
        print "Wrong input, pleas input again"
        input_year = raw_input("Please input year again: ")
    if IsLeapYear(input_year) == True:
        print "Yes,it's leap year!"
    else:
        print "No,it's not leap year!"

#调用主函数
start()


