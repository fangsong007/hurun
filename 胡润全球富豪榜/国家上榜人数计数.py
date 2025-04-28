import pandas as pd
# 读取 CSV 文件
df = pd.read_csv("2023全球富豪榜.csv")
# 提取 "公司总部地" 列，并获取国家名（假设国家名是总部地名称的第一部分）
df['国家'] = df['公司总部地'].str.split('-').str[0]
# 对 "国家" 列进行统计
result = df['国家'].value_counts().reset_index()
# 重命名列名称
result.columns = ['国家', '次数']
# 将结果保存为新的 CSV 文件
result.to_csv("country_counts.csv", index=False)