#!/usr/bin/env python
# -*-coding:utf-8 -*-

import ctypes

ArrayType = ctypes.py_object * 5
slots = ArrayType()

slots[0] = 'a'
print slots[0]