import random
import urllib.request

import pandas as pd
import requests
import json
from time import sleep
# all_data = {}
for page in range(1, 17):
    sleep_seconds = random.uniform(1, 2)
    offset = (page - 1) * 200
    url = "https://www.hurun.net/zh-CN/Rank/HsRankDetailsList?num=GJD3W34B&search=&offset={}&limit=200".format(offset)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36',
    }
    r = requests.get(url,headers= headers)
    print(r.status_code)
    json_data = r.json()
    Fullname_Cn_list = []  # 全名_中文
    Age_list = []  # 年龄
    BirthPlace_Cn_list = []  # 出生地_中文
    Gender_list = []  # 性别
    ComName_Cn_list = []  # 公司名称_中文
    ComHeadquarters_Cn_list = []  # 公司总部地_中文
    Industry_Cn_list = []  # 所在行业_中文
    Ranking_list = []  # 排名
    Ranking_Change_list = []  # 排名变化
    Wealth_list = []  # 财富值_人民币_亿
    Wealth_Change_list = []  # 财富值变化
    Education_Cn_list = []    # 学历
    print("开始解析json数据")
    item_list = json_data["rows"]
    for item in item_list:
        print(item["hs_Character"][0]["hs_Character_Fullname_Cn"])
        # 姓名
        Fullname_Cn_list.append(item["hs_Character"][0]["hs_Character_Fullname_Cn"])
        # 性别
        Gender_list.append(item["hs_Character"][0]["hs_Character_Gender_Lang"])
        # 年龄
        Age_list.append(item["hs_Character"][0]["hs_Character_Age"])
        # 出生所在地
        BirthPlace_Cn_list.append(item["hs_Character"][0]["hs_Character_BirthPlace_Cn"])
        # 学历
        Education_Cn_list.append(item["hs_Character"][0]["hs_Character_Education_Cn"])
        # 公司名
        ComName_Cn_list.append(item["hs_Rank_Global_ComName_Cn"])
        # 公司所在地
        ComHeadquarters_Cn_list.append(item["hs_Rank_Global_ComHeadquarters_Cn"])
        # 所在行业
        Industry_Cn_list.append(item["hs_Rank_Global_Industry_Cn"])
        # 排名
        Ranking_list.append(item["hs_Rank_Global_Ranking"])
        # 排名变化
        Ranking_Change_list.append(item["hs_Rank_Global_Ranking_Change"])
        # 财富
        Wealth_list.append(item["hs_Rank_Global_Wealth"])
        # 财富变化
        Wealth_Change_list.append(item["hs_Rank_Global_Wealth_Change"])
    df = pd.DataFrame(  # 拼装爬取到的数据为DataFrame
        {
            '姓名': Fullname_Cn_list,
            '性别': Gender_list,
            '年龄': Age_list,
            '出生地': BirthPlace_Cn_list,
            '学历': Education_Cn_list,
            '公司名称': ComName_Cn_list,
            '公司总部地': ComHeadquarters_Cn_list,
            '所在行业': Industry_Cn_list,
            '排名': Ranking_list,
            '排名变化': Ranking_Change_list,
            '财富值_人民币/亿元': Wealth_list,
            '财富值变化': Wealth_Change_list,
        }
    )
    if page == 1:
        header = True
    else:
        header = False
    df.to_csv('2024全球富豪榜.xls',mode = 'a+',index = False,header=header,encoding='utf8')
    print("第{}页爬取结束".format(page))
