#!/user/bin/python
# coding=utf-8
import pandas as pd

#读入数据
data = pd.read_excel(r'E:/data/fly.xls')



###数据探索###
import matplotlib.pyplot as plt
data.describe()

pd.value_counts(data['GENDER'])
pd.value_counts(data['WORK_CITY'])


for col in data.columns:
    if not col in [u'GENDER',u'WORK_CITY']:
        fig = plt.figure()
        ax=fig.add_subplot(1,1,1)
        data[col].hist(bins=20)
        ax.set_title(col)
        fig.show()
###模型建立###
#数据整理
cols = data.columns.diff([u'age',u'GENDER',u'WORK_CITY'])
cols
data_zs = 1.0*(data[cols] - data[cols].mean())/data[cols].std() #数据标准化
#dumies=pd.get_dummies(data[[u'Tariff',u'Handset']]) #获取虚拟变量
##合并数据
#data_zs = data_zs.merge(dumies,left_index=True,right_index=True)

#聚类数目
from scipy.cluster.hierarchy import linkage,dendrogram

Z = linkage(data_zs, method = 'ward', metric = 'euclidean') #谱系聚类图
P = dendrogram(Z, 0) #画谱系聚类图
plt.show()