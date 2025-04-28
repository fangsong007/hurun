import pandas as pd

data = pd.read_csv(r"E:\python_datas\数据分析\期末作业\胡润中国排行榜\20152023全球富豪榜.csv", encoding='utf8')

# 处理年龄未知项
unknown_age_rows = data[data['年龄'] == '未知']
data.drop(unknown_age_rows.index, inplace=True)
# print(data)


# 删除公司总部地为美国的行
data.drop(data[data['公司总部地'] == '美国'].index, inplace=True)

# 删除出生地列
data.drop('出生地', axis=1, inplace=True)
print(data)
