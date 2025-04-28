import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 显示中文标签  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# 读取数据
data = pd.read_csv('2023全球富豪榜.csv', encoding='utf8')
df_Wealth = data['财富值_人民币/亿元']


def paint_industries():
    # 统计所在行业的富豪数量并选出TOP20
    df_Industry = data['所在行业'].value_counts().nlargest(n=20)
    # 绘图
    fig, ax = plt.subplots(figsize=(18, 6))
    # 绘制柱形图
    df_Industry.plot.bar(ax=ax,
                         color='lightblue',
                         edgecolor='black',
                         alpha=0.7)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    # 添加标题和标签
    ax.set_title('行业分布TOP20-柱形图', fontsize=18, fontweight='bold')
    ax.set_xlabel('所在行业', fontsize=14)
    ax.set_ylabel('富豪数量', fontsize=14)
    # 设置y轴刻度范围和刻度间隔
    ax.set_ylim([0, df_Industry.max() + 100])
    ax.set_yticks(range(0, df_Industry.max() + 100, 50))
    # 去掉图形上方和右侧的边框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # 在柱形图上显示数值信息
    for i, v in enumerate(df_Industry.values):
        ax.text(i, v + 5, str(v), ha='center', fontsize=12)
    # 显示图形
    plt.show()


def paint_age():
    # 剔除未知
    df_Age = data[data.年龄 != '未知']
    # 数据切割，8个分段
    df_Age_cut = pd.cut(df_Age.年龄.astype(float), bins=[20, 30, 40, 50, 60, 70, 80, 90])
    # 统计各年龄段人数
    age_counts = df_Age_cut.value_counts()
    # 画饼图
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(age_counts, labels=age_counts.index, autopct='%1.1f%%', startangle=90, counterclock=False, labeldistance=1.1,
           textprops={'fontsize': 12})
    ax.axis('equal')
    ax.set_title('年龄分布-饼图', fontsize=18, fontweight='bold')
    ax.legend(labels=df_Age_cut.value_counts().index, loc='upper right', bbox_to_anchor=(1.1, 1))
    plt.show()


def paint_sex():
    df_sex = data[data['性别'] != '未知']
    male_count = df_sex[df_sex['性别'] == '先生'].shape[0]
    female_count = df_sex[df_sex['性别'] == '女士'].shape[0]
    labels = ['男士', '女士']
    sizes = [male_count, female_count]
    colors = ['#1f77b4', '#ff7f0e']
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%')
    plt.title('全球富豪男女比例饼图')
    plt.legend()
    plt.show()


def cloud():
    # 构造字典
    word_counts = {}
    for index, row in data.iterrows():
        company_name = row['公司名称']
        wealth = row['财富值_人民币/亿元']
        word_counts[company_name] = wealth
    # 生成词云
    wordcloud = WordCloud(scale=3,  # 清晰度
                          font_path="simsun.ttc",
                          width=800, height=400,
                          background_color="white"
                          ).generate_from_frequencies(word_counts)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


paint_industries()
paint_age()
paint_sex()
cloud()
