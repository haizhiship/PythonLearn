#!/user/bin/python
# coding=utf-8

"""
@author:出差在外
contact:898536955@qq.com
@file:Less4Regular.py
@time:2017/4/8 9:34
"""
'''
2. 我们可以使用切片符号删除词汇形态上的结尾。例如：'dogs'[:-1]删除了 dogs的 最后一个字符，
留下 dog。使用切片符号删除下面这些词的词缀（我们插入了一个连 字符指示词缀的边界，请在你的字符串中省略掉连字符）：
dish-es, run-ning, nation-ality, un-do, pre-heat
'''
print 'dogs'[:-1]
print 'dishes'[:-2]
print 'running'[:3]
print 'nationality'[:-5]
print 'undo'[:-2]
print 'preheat'[3:]
'''
6. 说明以下的正则表达式匹配的字符串类：
a. [a-zA-Z]+ 匹配一个或多个大小写字母的字符串
b. [A-Z][a-z]* 匹配零个或多个以大写字母和小写字母组合的字符串
c. p[aeiou]{,2}t 匹配p加至多重复2次的元音字母加t的字符串
d. \d+(\.\d+)? 匹配一个数字加零个或一个小数点加多个数字的字符串
e. ([^aeiou][aeiou][^aeiou])* 匹配零个或多个非元音加元音加非元
                                音组成的字符串
f. \w+|[^\w\s]+ 匹配字符或一个或多个非字符加非空白
使用nltk.re_show()测试你的答案
'''
import nltk, re
nltk.re_show(r"[a-zA-Z]+",'fd3ffdadZdd')
nltk.re_show(r"[A-Z][a-z]*",'fd3ffdadZdd ab')
nltk.re_show(r"p[aeiou]{,2}t",'fd3paatdZdd ab')
nltk.re_show(r"\d+(\.\d+)?",'abd12.32')
nltk.re_show(r"[^aeiou][aeiou][^aeiou]",'aefadaea be')
nltk.re_show(r"\w+|[^\w\s]+",', aefadaea be')
'''
17. 格式化字符串%6s 与%-6s 用来显示长度大于6个字符的字符串时，
会发生什么
'''
fdist = nltk.FreqDist(['dogrrrrr', 'cat', 'dog', 'cat', 'dog',
                       'snake1', 'dog', 'cat'])
for word in fdist:
    print '%6s' % word  #右对齐，超出部分向右延伸

for word in fdist:
    print '%-6s' % word #全部左对齐
'''
24.尝试编写代码将文本转换成hAck3r，使用正则表达式和替换，
其中 e→3，i→1，o→ 0，l→|，s→5，.→5w33t!，ate→8。
在转换之前将文本规范化为小写。自己添加更多的替换。
现在尝试将 s 映射到两个不同的值：词开头的s 映射为$，
词内部的 s 映射为5
'''
def replaceStr(str):
    strRe = re.sub(r'ate', '8', str)
    strRe = re.sub(r'e', '3', strRe)
    strRe = re.sub(r'i', '1', strRe)
    strRe = re.sub(r'o', '0', strRe)
    strRe = re.sub(r'l', '|', strRe)
    strRe = re.sub(r'^s', '$', strRe)
    strRe = re.sub(r's', '5', strRe)
    strRe = re.sub(r'\.', '5w33t!', strRe)
    return strRe

str ='She is abde.sbe atebd obed lsiebab'
str = str.lower()
print str
str = replaceStr(str)
print str