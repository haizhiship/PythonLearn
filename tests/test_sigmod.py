#!/user/bin/python
# coding=utf-8

import unittest
import Lesson.Lesson1.demo.sigmod as sg


class MyTestCase(unittest.TestCase):
    def test_sigmod(self):
   # x 为正常值
        x = 4
        y = sg.sigmod(x)
        self.assertEqual(y, 0.982,'methond  test failed')
   # x过大
        x = 10
        y = sg.sigmod.sigmod(x)
        self.assertEqual(y, 1, 'test failed')
  # x过小
        x = -10
        y = sg.sigmod.sigmod(x)
        self.assertEqual(y, 0, 'test failed')


if __name__ == '__main__':
    unittest.main()
