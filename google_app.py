import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""数据分析目的：为研发人员提供开发方向"""

# 这次只分析'App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type'
df = pd.read_csv('./googleplaystore.csv', usecols=(0, 1, 2, 3, 4, 5, 6))  # 读取应用App商店数据，此次分析前7列数据
# print(df.head())  # 查看前5行数据
# print(df.shape)  # 查看行列数量
# print(df.dtypes)  # 查看每一列的数据类型
# print(df.describe())  # 查看每一列的数据特征（例如：中位数、最大值、上四分位数）
# print(df.info())  # 查看数据概况，和属性types相似
# print(df.count())  # 查看各个列的非空数据量

"""经过查看数据前面的属性和函数，发现数据异常问题，需要清洗"""

# App处理
# print(pd.unique(df['App']).size)  # 查看有没有重复值，APP列是应用名称，不应该出现重复的值
# print(df['App'].value_counts())  # 也可以：df['App'].value_counts(),分别统计出每种App重复的次数
# 有重复值，先不着急删除重复值，为了不把其他列的异常值留下，先处理数值异常的列

# Category处理
# print(df['Category'].value_counts(dropna=False))  # 分别统计出每种Category重复的次数
# print(df[df['Category'] == '1.9'])  # 有一条异常值,获取该条异常值大概情况

# Rating处理
# print(df['Rating'].value_counts(dropna=False))
# print(df[df['Rating'] == 19.0])  # 有一条值是19的异常记录，和Category的异常是同一条记录
df['Rating'].fillna(value=df['Rating'].mean(), inplace=True)  # 用平均值填充

# Reviews清洗
# print(df['Reviews'].value_counts(dropna=False))  # 用value_counts看数据分布挺广，看起来都是数字
# print(df[df['Reviews'].str.isnumeric()])  # 查看是数值型的那些数据
# print(df[~df['Reviews'].str.isnumeric()])  # 查看非数值型的那些数据
df.drop(index=10472, inplace=True)  # 异常值和其他的一样，删除这条记录
df['Reviews'] = df['Reviews'].astype('i8')  # 转变该列的数据类型

# Size的清洗处理
df['Size'].value_counts()
df['Size'] = df['Size'].str.replace('M', 'e+6')
df['Size'] = df['Size'].str.replace('k', 'e+3')
# df['Size'] = df['Size'].astype('f8')  # 尝试转换，此时转换报错，还有字符串


# 定义一个字符串判断是否可以转换
def is_convertable(v):
    try:
        float(v)
        return True
    except ValueError:
        return False


temp = df['Size'].apply(is_convertable)
# print(df['Size'][~temp].value_counts())  # 查看不能转换的字符串分布
df['Size'] = df['Size'].str.replace('Varies with device', '0')  # 转换剩下的字符串
temp = df['Size'].apply(is_convertable)
# print(df['Size'][~temp].value_counts())  # 再看下是不是还有没转换的字符串
# e+5这种格式使用astype直接转为int有问题，如果想转成int，可以先转成f8，再转i8
# df['Size'] = df['Size'].astype('f8').astype('i8')
df['Size'] = df['Size'].astype('f8')  # 转换类型为f8
df['Size'].replace(0, df['Size'].mean(), inplace=True)  # 将Size为0的填充为平均数
# print(df.describe())

# Installs数据清洗
# print(df['Installs'].value_counts())  # 先查看分布
df['Installs'] = df['Installs'].str.replace('+', '')  # 分布比较少，直接替换
df['Installs'] = df['Installs'].str.replace(',', '')  # 分布比较少，直接替换
df['Installs'] = df['Installs'].astype('i8')  # 转换
# print(df.describe())

# Type处理
# df.info()查看到有na值，这里需要dropna参数
df['Type'].value_counts(dropna=False)
# print(df[df['Type'].isnull()])
df.drop(index=9148, inplace=True)  # 删除这条数据

df.drop_duplicates('App', inplace=True)  # 删除App重复的行

# df.describe()  # 数据清洗完毕，查看整体情况就开始数据分析

# 分析Category的数据
# print(df.Category.unique().size)  # 分类的个数
# print(df.groupby('Category').count().sort_values('App', ascending=False))  # 每个分类的App数量，排序，可以得出哪些分类的app最受开发者欢迎
# print(df.groupby('Category').mean().sort_values('Installs', ascending=False))  # 分类的安装量排序：娱乐社交类最被用户所需要
# print(df.groupby('Category').mean().sort_values('Reviews', ascending=False))  # 分类的评论数据：社交游戏视频评论多
# print(df.groupby('Category').mean().sort_values('Rating', ascending=False))  # 分类的打分数据，和其他数据不太一致，需要进一步分析

# 分析Type数据
# print(df.groupby('Type').count())  # 免费占比大，付费占比小，免费仍然是主流
# print(df.groupby('Type').sum().sort_values('Installs', ascending=False))  # 只有两个类型，且数据量差别很大，没必要继续对比了

# Category和Type一起分析
# print(df.groupby(['Type', 'Category']).mean().sort_values('Reviews', ascending=False))


g = df.groupby(['Type', 'Category']).mean()
# print((g['Reviews'] / g['Installs']).sort_values(ascending=False))  # 评论安装比,收费的app评论比率更高


# 相关性：评论数和安装数强相关，其他的连0.1都不到，可以认为是不相关的（0.5以上可以认为是相关的，0.3以上可以认为是弱相关）
print(df.corr())
