import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
data = pd.read_csv(r'E:\python_datas\数据分析\期末作业\胡润全球富豪榜\2023全球富豪榜.csv')
wealth_values = data['财富值_人民币/亿元']  # 将您的财富值数据填入此处
# 将数据转换为NumPy数组并进行reshape
X = np.array(wealth_values).reshape(-1, 1)
# 定义K值的范围即聚类的数量
k_values = range(2, 11)  # 设置聚类数量为2到11
# 计算每个K值对应的模型评分（inertia）和轮廓系数
inertias = []
silhouette_scores = []
for k in k_values:
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)
    labels = kmeans.labels_
    silhouette_scores.append(silhouette_score(X, labels))
# 绘图
fig, ax1 = plt.subplots()
# 绘制手肘法图
ax1.plot(k_values, inertias, 'bx-', label='手肘法')
ax1.set_xlabel('K值')
ax1.set_ylabel('模型评分（inertia）')
ax1.set_title('聚类评估')
# 创建轮廓系数图的副坐标轴
ax2 = ax1.twinx()
ax2.plot(k_values, silhouette_scores, 'ro-', label='轮廓系数')
ax2.set_ylabel('轮廓系数')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.tight_layout()
plt.show()
