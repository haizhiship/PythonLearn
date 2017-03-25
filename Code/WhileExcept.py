#!/user/bin/python
# coding=utf-8

"""
@author:出差在外
contact:898536955@qq.com
@file:WhileExcept.py
@time:2017/3/5 22:05
用循环来判断是否有异常，提示用户不停输入正确的数字，直到输入正确才能退出循环
"""

while True:
  try:
     x= input('Enter the first number: ')
     y= input('Enter the second number: ')
     value= x/y
     print 'x/y is', value
  except:
     print 'Invalid input.Please try again'
  else:
     break