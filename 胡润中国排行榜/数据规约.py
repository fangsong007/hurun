import os
import re
import pandas as pd
data_dir = 'E:\python_datas\数据分析\期末作业\胡润中国排行榜\数据集'  # 数据集所在目录的路径，根据实际情况进行修改
# 获取数据集文件列表
file_list = os.listdir(data_dir)
data_frames = []

# 遍历每个数据集文件
for filename in file_list:
    if filename.endswith('.csv'):
        # 解析文件名获取年份信息
        year = re.search(r'(\d{4})年', filename).group(1)

        file_path = os.path.join(data_dir, filename)
        data = pd.read_csv(file_path)
        data['年份'] = year  # 添加年份列
        data = data[['年份','姓名', '性别','年龄','公司总部地','所在行业','排名','财富值_人民币/亿元']]  # 保留年份和所在行业两列
        data_frames.append(data)

# 合并所有数据集
merged_data = pd.concat(data_frames, ignore_index=True)

merged_data.to_csv('各年富豪情况.csv', index=False)
#打印合并后的数据集
print(merged_data)


