import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 读取数据集
data = pd.read_csv(r'E:\python_datas\数据分析\期末作业\胡润中国排行榜\各年富豪情况.csv')
# 拆分多个行业为单个行业
expanded_data = data.assign(所在行业=data['所在行业'].str.split('、')).explode('所在行业')
# 统计每个行业的出现次数
top_industries = expanded_data.groupby(['年份', '所在行业']).size().reset_index(name='Count')
# 获取每年的前5个热门行业
top_industries = top_industries.groupby('年份').apply(lambda x: x.nlargest(5, 'Count')).reset_index(drop=True)
# 根据行业数量按升序排序
top_industries = top_industries.sort_values(by=['年份', 'Count'], ascending=[True, True])
# 为3D条形图准备数据
years = top_industries['年份'].unique()
industries = top_industries['所在行业'].unique()
#创建一个年份和行业的网格
X, Y = np.meshgrid(years, industries)
# 创建一个空数组来存储每个行业和年份的计数
counts = np.zeros((len(industries), len(years)))
# 遍历行业并填充计数数组
for i, industry in enumerate(industries):
    industry_data = top_industries[top_industries['所在行业'] == industry]
    for j, year in enumerate(years):
        count = industry_data[industry_data['年份'] == year]['Count']
        if count.empty:
            counts[i, j] = 0
        else:
            counts[i, j] = count.values[0]
# 为图像设置图形和轴
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
# 调整图形的大小和条形条的宽度
fig.set_size_inches(14, 10)
bar_width = 0.8 / len(years)
bar_spacing = 0.05
# 创建3D条形图
colors = plt.cm.tab20(np.linspace(0, 1, len(industries)))
bars = []
for i in range(len(industries)):
    x = np.arange(len(years)) + i * bar_width + i * bar_spacing
    bars.append(ax.bar(x, counts[i], zs=i, zdir='y', alpha=0.8, width=bar_width, color=colors[i]))
# 设置标签
ax.view_init(azim=60, elev=20)
ax.set_xlabel('Year')
ax.set_ylabel('Industry', labelpad=20)
ax.set_zlabel('Count')
ax.set_title('每年从事最多行业Top5变化趋势3D图')
x_ticks = np.arange(len(years)) + (len(industries) / 2) * bar_width + (len(industries) / 2) * bar_spacing
ax.set_xticks(x_ticks)
ax.set_xticklabels(years)
y_ticks = np.arange(len(industries))
ax.set_yticks(y_ticks)
ax.set_yticklabels(industries, rotation=30, ha='right')
ax.set_ylabel('Industry')
ax.yaxis.set_label_coords(-0.15, 0.5)
legend_labels = top_industries['所在行业'].unique()
legend_colors = colors[:len(legend_labels)]
ax.legend(bars, legend_labels, loc='upper right')
plt.tight_layout()
plt.show()
