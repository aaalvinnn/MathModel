'''
Reference: 
1. https://zhuanlan.zhihu.com/p/89353885
2. https://github.com/mwaskom/seaborn-data 示例中的数据集
3. https://seaborn.pydata.org/tutorial  官方guidebook
4. https://seaborn.pydata.org/examples/index.html 官方画廊

函数传参：
        data:pd.read(".csv")返回的DataFrame数据类型
        x:DataFrame结构中的列名
        y:行名

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # 图标风格设置，默认为darkgrid风格，另外四种：whitegrid,dark,white,ticks
    sns.set()   
    plt.plot()

# 散点图
def Scatter():
    sns.set_theme(style="whitegrid")
    # diamonds = sns.load_dataset("diamonds")       #调用sns.load_dataset()函数读取在线repository的文件，需联网
    # 离线下也可直接用pd.read_csv读取，返回pd.DataFrame类型供sns.scatterplot调用
    diamonds = pd.read_csv("Drawing//seaborn-data-master//seaborn-data-master//diamonds.csv")
    # Draw a scatter plot while assigning point colors and sizes to different
    # variables in the dataset
    f, ax = plt.subplots(figsize=(6.5, 6.5))
    sns.despine(f, left=True, bottom=True)
    clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
    sns.scatterplot(x="carat", y="price",
                    hue="clarity", size="depth",
                    palette="ch:r=-.2,d=.3_r",
                    hue_order=clarity_ranking,
                    sizes=(1, 8), linewidth=0,
                    data=diamonds, ax=ax)
    # plt.show()

# 单变量频数直方图
def UniVariate_Analysis():
    sns.set_style('darkgrid')
    # 生成100个成标准正态分布的随机数
    x = np.random.normal(size=100)
    # 画出频数直方图 kde为核密度估计
    sns.distplot(x,kde=True)
    # plt.show()

# 双变量散点图
def Bivariate_Analysis():
    sns.set()
    # 创建二维多正态分数的数据
    mean,cov = [0,1],[(1,.5),(.5,1)]
    data = np.random.multivariate_normal(mean,cov,200)
    # 将array结构转换为pandas的dataframe结构，添加列名x，y
    df = pd.DataFrame(data,columns=['x','y'])
    # 绘制双变量散点图
    sns.jointplot(x=df['x'],y=df['y'],data=df,size=7)
    # plt.show()

# 六角图
def Hexagonal_Chart():
    sns.set()
    mean,cov = [0,1],[(1,.5),(.5,1)]
    x,y = np.random.multivariate_normal(mean,cov,1000).T
    # 设置画布风格，（但感觉这一句可有可无， 因为后面设置了颜色了）
    with sns.axes_style('white'):
        sns.jointplot(x=x,y=y,kind='hex',color='k')  #kind='hex'画出六角图
    # plt.show()

# 热度图
def Heatmap():
    sns.set()
    uniform_data = np.random.rand(8,8)
    heatmap = sns.heatmap(uniform_data)
    # plt.show()

#具有多个变量的二元图
def Bivariate_Multiple_elements():
    sns.set_theme(style="dark")

    # Simulate data from a bivariate Gaussian
    n = 10000
    mean = [0, 0]
    cov = [(2, .4), (.4, .2)]
    rng = np.random.RandomState(0)
    x, y = rng.multivariate_normal(mean, cov, n).T

    # Draw a combo histogram and scatterplot with density contours
    f, ax = plt.subplots(figsize=(6, 6))
    sns.scatterplot(x=x, y=y, s=5, color=".15")
    sns.histplot(x=x, y=y, bins=50, pthresh=.1, cmap="mako")
    sns.kdeplot(x=x, y=y, levels=5, color="w", linewidths=1)

#带状图上的多变量回归拟合
def Regression_Strip():
    sns.set_theme()

    mpg = pd.read_csv("Drawing//seaborn-data-master//seaborn-data-master//mpg.csv")
    #带状图
    sns.catplot(
        data=mpg, x="cylinders", y="acceleration", hue="weight",
        native_scale=True, zorder=1
    )
    # 回归拟合
    sns.regplot(
        data=mpg, x="cylinders", y="acceleration",
        scatter=False, truncate=False, order=2, color=".2",
    )

if __name__ == '__main__':
    Regression_Strip()
    plt.show()