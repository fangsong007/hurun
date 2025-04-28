import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']    # 显示中文标签  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# 读取数据集
data = pd.read_csv(r'E:\python_datas\数据分析\期末作业\胡润中国排行榜\各年富豪情况.csv')
# 填充缺失值
data['公司总部地'] = data['公司总部地'].fillna('')
# 提取 "公司总部地" 列，
data['公司总部'] = data['公司总部地'].str.split('-').str[1]
# 按年份和公司总部进行分组，计算每个年份每个城市的富豪人数和财富值之和
industry_stats = data.groupby(['年份', '公司总部']).agg({'姓名': 'count', '财富值_人民币/亿元': 'sum'}).reset_index()
industry_stats.rename(columns={'姓名': '驻扎人数'}, inplace=True)
# 计算每个城市的热度指数，可以将驻扎人数和财富值进行加权处理
industry_stats['热度指数'] = industry_stats['驻扎人数'] * industry_stats['财富值_人民币/亿元']
# 按年份和热度指数降序排列，获得每个年份最热门的城市
top_industries = industry_stats.sort_values(['年份', '热度指数'], ascending=[True, False])
# 打印每个年份最热门的城市
for year in top_industries['年份'].unique():
    year_data = top_industries[top_industries['年份'] == year]
    print(f"年份：{year}")
    print(year_data[['公司总部', '热度指数']].reset_index(drop=True))
    print()
# 列出每年指数最高的5个城市
top_cities = industry_stats.groupby('年份').apply(lambda x: x.nlargest(5, '热度指数')).reset_index(drop=True)
# 为条形图绘制颜色
colors = sns.color_palette('Set3', n_colors=5)
# 绘制水平条形图
plt.figure(figsize=(12, 8))
sns.barplot(data=top_cities, y='公司总部', x='热度指数', hue='年份', palette=colors)
plt.xlabel('热力指数')
plt.ylabel('城市')
plt.title('每年最热门城市排名前五')
plt.legend(title='Year')
plt.tight_layout()
plt.show()