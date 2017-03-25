#!/user/bin/python
# coding=utf-8

"""
@author:出差在外
contact:898536955@qq.com
@file:setup.py.py
@time:2017/3/11 12:06
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'description':'Project test',
    'author':'zhang xiang',
    'url':'URL to get it at.',
    'download_url':'Where to download it.',
    'author_email':'My email',
    'version':'0.1',
    'install_requires':['unittest'],
    'packages':['NAME'],
    'scripts':[],
    'name':'projectname'
}

setup(**config)
