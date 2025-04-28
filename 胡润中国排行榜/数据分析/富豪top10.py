import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']    # 显示中文标签  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# 读取数据集
data = pd.read_csv(r'E:\python_datas\数据分析\期末作业\胡润中国排行榜\各年富豪情况.csv', encoding='utf-8')
# 按年份升序和财富值降序排列
sorted_data = data.sort_values(['年份', '财富值_人民币/亿元'], ascending=[True, False])
# 提取每年富豪榜前10名富豪的信息
top_10_rich = sorted_data.groupby('年份').head(10)
# 创建动态效果图
fig = px.bar(top_10_rich, x='姓名', y='财富值_人民币/亿元', animation_frame='年份',
             range_y=[0, top_10_rich['财富值_人民币/亿元'].max() + 100],
             title="富豪榜Top10变化图")
fig.update_layout(xaxis_tickangle=-45)
# 设置播放速度为1秒
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000
# 保存为HTML文件
fig.write_html("富豪榜TOP10.html")
fig.show()
