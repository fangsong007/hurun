import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']    # 显示中文标签  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


# 读取数据集
data = pd.read_csv(r'E:\python_datas\数据分析\期末作业\胡润中国排行榜\各年行业情况.csv')

# 提取需要进行聚类的特征
features = ['财富值_人民币/亿元']
data_subset = data[features]

# 执行肘部法来确定聚类数量
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_subset)
    inertia.append(kmeans.inertia_)

# 绘制肘部法曲线
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('聚类数量')
plt.ylabel('Inertia')
plt.title('肘部法')
plt.show()
