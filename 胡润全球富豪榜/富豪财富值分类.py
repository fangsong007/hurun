import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']    # 显示中文标签  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# 读取数据集
data = pd.read_csv(r'E:\python_datas\数据分析\期末作业\胡润全球富豪榜\2023全球富豪榜.csv')
wealth_values = data['财富值_人民币/亿元']  # 将您的财富值数据填入此处
# 将数据转换为NumPy数组并进行reshape
X = np.array(wealth_values).reshape(-1, 1)
# 定义聚类数量
k = 4
# 创建并训练K均值模型
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X)
# 获取每个样本的所属簇
labels = kmeans.labels_
# 输出每个样本的所属簇
for i, label in enumerate(labels):
    print(f"富豪{i+1} 的财富值属于类别 {label+1}")
# 获取每个簇的质心（中心点）
centroids = kmeans.cluster_centers_
# 输出每个簇的质心（中心点）
for i, centroid in enumerate(centroids):
    print(f"类别 {i+1} 的质心（中心点）为 {centroid[0]}")
# 绘制箱线图
import seaborn as sns
data = np.concatenate([X, labels.reshape(-1, 1)], axis=1)
df = pd.DataFrame(data, columns=['财富值', '分类'])
plt.figure(figsize=(8, 6))
sns.boxplot(x='分类', y='财富值', data=df)
plt.xlabel('分类')
plt.ylabel('财富值')
plt.title('富豪财富值分类箱线图')
plt.show()
