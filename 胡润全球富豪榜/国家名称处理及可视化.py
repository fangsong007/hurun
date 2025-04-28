import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
# 使用 pandas 读取 CSV 文件
data = pd.read_csv("country_counts.csv")
# # 创建一个字典，包含需要翻译的国家名称及其对应的英文名称
country_dict = {
    '中国': "China",
    '丹麦': "Denmark",
    '乌克兰': 'Ukraine',
    '亚美尼亚': 'Armenia',
    '以色列': 'Israel',
    '俄罗斯': 'Russia',
    '保加利亚': 'Bulgaria',
    '列支敦士登': 'Liechtenstein',
    '加拿大': 'Canada',
    '匈牙利': 'Hungary',
    '南非': 'South Africa',
    '南韩': 'South Korea',
    '卡塔尔': 'Qatar',
    '印度': 'India',
    '印度尼西亚': 'Indonesia',
    '哈萨克斯坦': 'Kazakhstan',
    '哥伦比亚': 'Colombia',
    '土耳其': 'Turkey',
    '坦桑尼亚': 'Tanzania',
    '埃及': 'Egypt',
    '塞舌尔': 'Seychelles',
    '墨西哥': 'Mexico',
    '奥地利': 'Austria',
    '委内瑞拉': 'Venezuela',
    '尼日利亚': 'Nigeria',
    '尼泊尔': 'Nepal',
    '巴哈马': 'Bahamas',
    '巴西': 'Brazil',
    '希腊': 'Greece',
    '德国': 'Germany',
    '意大利': 'Italy',
    '挪威': 'Norway',
    '捷克共和国': 'Czech Republic',
    '摩洛哥': 'Moloch',
    '摩纳哥': 'Monaco',
    '斯洛伐克': 'Slovakia',
    '新加坡': 'Singapore',
    '新西兰': 'New Zealand',
    '日本': 'Japan',
    '智利': 'Chile',
    '格鲁吉亚': 'Georgia',
    '比利时': 'Belgium',
    '沙特阿拉伯': 'Saudi Arabia',
    '法国': 'France',
    '波兰': 'Poland',
    '泰国': 'Thailand',
    '澳大利亚': 'Australia',
    '爱尔兰': 'Ireland',
    '瑞典': 'Sweden',
    '瑞士': 'Switzerland',
    '科威特': 'Kuwait',
    '秘鲁': 'Peru',
    '罗马尼亚': 'Romania',
    '美国': 'United States',
    '芬兰': 'Finland',
    '英国': 'United Kingdom',
    '荷兰': 'Netherlands',
    '菲律宾': 'Philippines',
    '葡萄牙': 'Portugal',
    '西班牙': 'Spain',
    '越南': 'Vietnam',
    '阿尔及利亚': 'Algeria',
    '阿拉伯联合酋长国': 'United Arab Emirates',
    '阿曼': 'Oman',
    '阿根廷': 'Argentina',
    '阿联酋': 'UAE',
    '韩国': 'Korea',
    '马来西亚': 'Malaysia',
    '黎巴嫩': 'Lebanon'
}
# 使用 map 函数将国家列的值替换为其对应的英文名称
data['国家'] = data['国家'].map(country_dict)
data_list = [(country, count) for country, count in zip(data['国家'], data['次数'])]
c = (
    Map()
    .add("次数", data_list, "world")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-世界地图"),
        visualmap_opts=opts.VisualMapOpts(max_=200),
    )
    .render("map_world.html")
)
