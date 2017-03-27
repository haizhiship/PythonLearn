#!/usr/bin/env python
# -*-coding:utf-8 -*-

import unittest
from  MyLesson import  Le3Week


class MyTestLesson3(unittest.TestCase):

    def testWeek(self):
        year = 2017
        date = 3
        self.assertEqual(Le3Week.whichWeekDay(year, date), 5, 'Test 1 fail.')

        year = 2017
        date = 4
        self.assertEqual(Le3Week.whichWeekDay(year, date), 0, 'Test 2 fail.')

if __name__ == '__main__':
    unittest.main()