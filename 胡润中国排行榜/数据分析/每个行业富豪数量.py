import pandas as pd
# 读取数据集
df = pd.read_csv('../各年富豪情况.csv')
# 将行业数据拆分为多个列
df['行业'] = df['所在行业'].str.split('、')
# 创建一个新的数据帧，每个行业作为一行数据
industry_df = pd.DataFrame({
    '富豪姓名': df['姓名'],
    '公司总部地': df['公司总部地'],
    '财富值': df['财富值_人民币/亿元']
})
# 遍历每一行，将每个富豪的每个行业拆分为多行数据
rows = []
for _, row in df.iterrows():
    industries = row['行业']
    for industry in industries:
        new_row = {
            '富豪姓名': row['姓名'],
            '公司总部地': row['公司总部地'],
            '财富值': row['财富值_人民币/亿元'],
            '行业': industry
        }
        rows.append(new_row)
# 创建包含拆分后行业数据的新数据帧
expanded_industry_df = pd.DataFrame(rows)
# 统计每个行业的富豪数量
industry_counts = expanded_industry_df['行业'].value_counts()
# 打印行业和对应的富豪数量
print(industry_counts)

