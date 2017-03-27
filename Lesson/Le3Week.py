#!/usr/bin/env python
# -*-coding:utf-8 -*-

#判断是否闰年
def isLeapYear(year):
    return (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0)

def whichWeekDay(year, date):

    days = [31,28,31,30,31,30,31,31,30,31,30,31]

    sumDay = 0
    for y in range(1900, year): #将整年的时间累计
        if isLeapYear(y):
            days[1] = 29
        else:
            days[1] = 28
        for day1 in days:
            sumDay += day1

    for day2 in range(date) :#将月的时间累计
        if isLeapYear(year):
            days[1] = 29
        else:
            days[1] = 28
        sumDay += days[day2]

    weekDay = sumDay % 7 #求取星期几的数据
    return weekDay

if __name__ == '__main__':
    str = raw_input("input year and month:")
    year, date = str.split()
    print whichWeekDay(int(year), int(date))






