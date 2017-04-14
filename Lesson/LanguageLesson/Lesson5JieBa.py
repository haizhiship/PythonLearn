#!/usr/bin/env python
# -*-coding:utf-8 -*-

import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print "Full Mode: " +  "/".join(seg_list)

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print "Precise Mode: " +  "/".join(seg_list)

seg_list = jieba.cut("他来到网易杭研大厦。")
print "Default Mode:" + "/".join(seg_list)

#s搜索引擎模式
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
print "Search Mode:" + "/".join(seg_list)

# ##Part 2. 添加自定义词典

# ###载入词典
# 开发者可以指定自己自定义的词典，以便包含 jieba 词库里没有的词。虽然 jieba 有新词识别能力，但是自行添加新词可以保证更高的正确率。
# 用法： jieba.load_userdict(file_name) # file_name 为自定义词典的路径。
# 词典格式和dict.txt一样，一个词占一行；每一行分三部分，一部分为词语，另一部分为词频（可省略），最后为词性（可省略），用空格隔开。
# 词频可省略，使用计算出的能保证分出该词的词频。
# 更改分词器的 tmp_dir 和 cache_file 属性，可指定缓存文件位置，用于受限的文件系统。
##自定义词典
seg_list = jieba.cut("李小福是创新办主任也是云计算方面的专家")
print ("Origin:" + "/".join(seg_list))

jieba.load_userdict("E:\\data\\jieba.txt")
seg_list = jieba.cut("李小福是创新办主任也是云计算方面的专家")
print ("Revise:" + "/".join(seg_list))

# ###调整词典

# 使用 add_word(word, freq=None, tag=None) 和 del_word(word) 可在程序中动态修改词典。
# 使用 suggest_freq(segment, tune=True) 可调节单个词语的词频，使其能（或不能）被分出来。
# 注意：自动计算的词频在使用 HMM 新词发现功能时可能无效。
print ("/".join(jieba.cut("如果放到pos中将出错", HMM = False)))
#利用调节词频使用“中”和“将”都能分离出来
jieba.suggest_freq(("中","将"), tune = True)
print ("/".join(jieba.cut("如果放到pos中将出错", HMM = False)))

Original = "/".join(jieba.cut("江州市长江大桥参加了长江大桥的通车仪式。", HMM = False))
print "Original: " + Original

jieba.add_word("江大桥", freq = 20000, tag = None)
print "/".join(jieba.cut("江州市长江大桥参加了长江大桥的通车仪式。"))

#或者采用词典方式
jieba.load_userdict("E:\\data\\jieba.txt")
print "/".join(jieba.cut("江州市长江大桥参加了长江大桥的通车仪式。"))

# ##Part 3. 词性标注

# jieba.posseg.POSTokenizer(tokenizer=None) 新建自定义分词器，tokenizer 参数可指定内部使用的 jieba.Tokenizer 分词器。jieba.posseg.dt 为默认词性标注分词器。
# 标注句子分词后每个词的词性，采用和 ictclas 兼容的标记法。
import jieba.posseg as pseg
words = pseg.cut("我爱北京天安门。")
for w in words:
    print ("%s %s" %(w.word, w.flag))

# ##Part 4. 关键词提取

# ###基于 TF-IDF 算法的关键词提取

# import jieba.analyse
# jieba.analyse.extract_tags(sentence, topK = 20, withWeight = False, allowPOS = ())
# sentence:待提取的文本。
# topK:返回几个 TF/IDF 权重最大的关键词，默认值为20。
# withWeight:是否一并返回关键词权重值，默认值为False。
# allowPOS:仅包括指定词性的词，默认值为空，即不进行筛选。
# jieba.analyse.TFIDF(idf_path=None) 新建 TFIDF 实例，idf_path 为 IDF 频率文件。

# optparse模块OptionParser学习
#  optparse是专门在命令行添加选项的一个模块。

from optparse import OptionParser
MSG_USAGE = "myprog [-f ][-s ] arg1[,arg2..]"bus
optParser = OptionParser(MSG_USAGE)
#以上，产生一个OptionParser的物件optParser。传入的值MSG_USAGE可被调用打印命令时显示出来。
optParser.add_option("-f","--file",action = "store",type="string", dest = "fileName")
optParser.add_option("-v","--vision",action="store_false",dest="verbose",default="gggggg",
                     help="make lots of noise [default]")
#调用OptionParser.add_option()添加选项，add_option()参数说明：
#action:存储方式，分为三种store, store_false, store_true
#type:类型
#dest:存储的变量
#default:默认值
#help:帮助信息
fakeArgs = ['-f','file.txt','-v','good luck to you', 'arg2', 'arge']
options, args = optParser.parse_args(fakeArgs)
print options.fileName
print options.verbose
print options
print args
