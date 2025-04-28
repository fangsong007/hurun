import pandas as pd
import matplotlib.pyplot as plt
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']    # 显示中文标签  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# 读取数据集
data = pd.read_csv(r'/期末作业/胡润中国排行榜/各年富豪情况.csv', encoding='utf-8')
# 按年份和性别分组
grouped_data = data.groupby(['年份', '性别']).size().reset_index(name='counts')
# 计算每年男性的数量和总人数
male_counts = grouped_data[grouped_data['性别'] == '先生']['counts']
total_counts = grouped_data.groupby('年份')['counts'].sum()
# 保存total_counts变量的索引,等会绘图要用
years = total_counts.index
# 重置male_counts和total_counts变量的索引
male_counts = male_counts.reset_index(drop=True)
total_counts = total_counts.reset_index(drop=True)
# 计算男性的比例
male_ratios = male_counts / total_counts
# 绘制折线图
plt.plot(years, male_ratios.values)
plt.title('男性富豪占榜比例变化折线图')
plt.xlabel('年份')
plt.ylabel('男性比例')
plt.show()
