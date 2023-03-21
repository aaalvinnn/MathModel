import geopandas
import matplotlib.pyplot as plt 
import numpy as np
# import pandas as pd

def getLng(i):#经度
    if i<0:
        return str(-i)+"°W"
    elif i==0:
        return "0°"
    else:
        return str(i)+"°E"

def getLat(i):#纬度
    if i<0:
        return str(-i)+"°S"
    elif i==0:
        return "0°"
    else:
        return str(i)+"°N"  
    
#世界地图背景图
if __name__ == '__main__':
    world=geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    ax=world.plot(facecolor="#bbbbbb",edgecolor="#f3f3f3")
    ax.set_facecolor("#f3f3f3")
    ax.set_xlim(-180,181)
    ax.set_ylim(-90,91)
    xticks=np.arange(-180,181,30)
    # xticks[0]=-175
    yticks=np.arange(-90,91,30)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    #不加这两行可以鼠标悬浮显示对应位置经纬度（虽然没有单位）
    # ax.set_xticklabels([getLng(i) for i in np.arange(-180,181,30)])
    # ax.set_yticklabels([getLat(i) for i in np.arange(-90,91,30)])

    #打点
    plt.scatter(50,  # 横坐标
                50,  # 纵坐标
                marker='.', #点的形状
                c='red',  # 点的颜色
                label='function' # 标签 即为点代表的意思
                )  

    plt.legend()  # 显示图例
    plt.show()  # 显示所绘图形