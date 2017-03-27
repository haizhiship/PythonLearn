#!/usr/bin/env python
# -*-coding:utf-8 -*-

import unittest
from  MyLesson import  Le2Sort_num
import math

class MyTestLes2(unittest.TestCase):

    def test_Sort(self):
        data = [0, 0.5, -90, 22, 45, 12, 108]
        #判断绝对值升序排序
        test1 = [0, 0.5, 12, 22, 45, 90, 108]
        self.assertEqual(Le2Sort_num.mysort(data, abs, True), test1, 'test1 failed')

        #判断绝对值降序排序
        test2 = [108, 90, 45, 22, 12, 0.5, 0]
        self.assertEqual(Le2Sort_num.mysort(data, abs, False), test2, 'test2 failed')

        #判断sin()函数升序排序
        test3 = [-0.8939966636005579, -0.5365729180004349, -0.008851309290403876,
                 0.0, 0.479425538604203, 0.8509035245341184, 0.926818505417785]
        self.assertEqual(Le2Sort_num.mysort(data, math.sin, True), test3, 'test3 failed')

if __name__ == '__main__':
    unittest.main()