# 元胞自动机模拟森林火灾
import numpy as np
import random
import seaborn as sbn
import matplotlib.pyplot as plt

# 森林火灾函数
#元胞空间的邻居模型为冯诺伊曼型
# 传入参数为：（1）当前的燃烧矩阵；（2）空格位 树的生长概率p；（3）正常位 树的燃烧概率f
 
# 假定：空格位 --> 0  正常位 --> 1   燃烧位 --> -1
# 总量：空格位 --> C  正常位 --> G   燃烧位 --> R
# 其中indexes数组为要处理的元胞的横坐标和纵坐标，采用先储存坐标，最后再赋值的方案
def Forest_Fire(current_matrix,p,f):
    matrix=current_matrix
 
    # （1）空位生长树木 （0 --> 1）   储存位置
    i_C_indexes = []
    j_C_indexes = []
    for i in range(area):   # 行循环
        for j in range(area):   # 列循环
            if matrix[i, j] == 0 and random.random()<p:
                i_C_indexes.append(i)
                j_C_indexes.append(j)
            else:
                pass
 
 
    # (2)周围树木燃烧 &  (1 --> -1)   储存位置，并存储上一时刻的燃烧数据
    fire_memory=np.where(matrix==-1)
    i_indexes=[]
    j_indexes=[]
 
    for i in range(area):   # 行循环
        for j in range(area):   # 列循环
            if matrix[i,j]==-1:
                try:
                    if matrix[i-1,j]==1:
                        i_indexes.append(i-1)
                        j_indexes.append(j)
                except:
                    pass
 
                try:
                    if matrix[i + 1, j] == 1:
                        i_indexes.append(i + 1)
                        j_indexes.append(j)
                except:
                    pass
 
                try:
                    if matrix[i , j-1] == 1:
                        i_indexes.append(i)
                        j_indexes.append(j-1)
                except:
                    pass
 
                try:
                    if matrix[i , j+1] == 1:
                        i_indexes.append(i)
                        j_indexes.append(j+1)
                except:
                    pass
 
            else:
                pass
 
    for k in range(len(i_indexes)):
        matrix[i_indexes[k],j_indexes[k]]=-1
 
 
    # （3）燃烧树木清除 （-1 --> 0）
    matrix[fire_memory]=0
 
 
    # （4）雷电击中正常树木 （1 --> -1）    储存位置
    i_indexes = []
    j_indexes = []
 
    for i in range(area):   # 行循环
        for j in range(area):   # 列循环
            if matrix[i, j] == 1 :
 
                # 判断最近邻居是否有树木燃烧
                try:
                    if matrix[i-1,j] ==-1:
                        continue
                    else:
                        pass
                except:
                    pass
 
                try:
                    if matrix[i+1,j] ==-1:
                        continue
                    else:
                        pass
                except:
                    pass
 
                try:
                    if matrix[i,j-1] ==-1:
                        continue
                    else:
                        pass
                except:
                    pass
 
                try:
                    if matrix[i,j+1] ==-1:
                        continue
                    else:
                        pass
                except:
                    pass
 
 
                # 树木被雷击中
                if random.random() < f:
                    i_indexes.append(i)
                    j_indexes.append(j)
                else:
                    pass
 
            else:
                pass
 
    for k in range(len(i_indexes)):
        matrix[i_indexes[k],j_indexes[k]]=-1
 
    # 完成空位生长树木的操作
    for k in range(len(i_C_indexes)):
        matrix[i_C_indexes[k],j_C_indexes[k]]=1
 
    return matrix


# 主函数
# 传入参数为：（1）方形区域的边长；（2）模拟次数N;
#（3）空格位 树的生长概率p；（4）正常位 树的燃烧概率f
 
def main(area,N,p,f):
 
    # 创建一个 area*area 的实验区域，该区域均为正常位
    matrix=np.ones([area,area]).astype("int")
 
    #matrix[random.randint(0,79),random.randint(0,79)]=-1
 
    # 开始进行森林火灾模拟 N次循环   （燃烧概率f引发森林火灾）
    for time in range(N):
        matrix=Forest_Fire(matrix,p,f)
 
        C_count.append(len(np.where(matrix==0)[0]))
        G_count.append(len(np.where(matrix == 1)[0]))
        R_count.append(len(np.where(matrix == -1)[0]))
 
        # if time<=5:
        #     plt.figure(time+1, figsize=(19.20, 9.61))
        #     sbn.heatmap(matrix,
        #                 cmap=[(239 / 255, 29 / 255, 31 / 255),
        #                      (165 / 255, 165 / 255, 165 / 255),
        #                       (28 / 255, 172 / 255, 76 / 255)], annot=True)
        #     plt.savefig('C:/Users/28692/Documents/Python works/数模/模型/{}.jpg'.format(time+1))
 
 
    plt.figure(7,figsize=(19.20, 9.61))
    T = [i for i in range(N+1)]
 
    plt.plot(T,C_count,label='Vacancy',lw=2,color=(165/255,165/255,165/255))
    plt.plot(T, G_count, label='Trees',lw=2, color=(28/255,172/255,76/255))
    plt.plot(T, R_count, label='Burning',lw=2, color=(239/255,29/255,31/255))
 
    plt.grid(linestyle=":")
    plt.legend()
 
    plt.savefig('C:/Users/28692/Documents/Python works/数模/模型')
 
    plt.show()

#执行程序
if __name__ == '__main__':
    global area
    area=100
    
    C_count=[0]
    G_count=[area**2]
    R_count=[0]
    
    
    # 传入参数为：（1）方形区域的边长；（2）模拟次数N;
    # （3）空格位 树的生长概率p；（4）正常位 树的燃烧概率f
    
    final_matrix=main(area,100,0.25,0.01)
    
    plt.figure()
    sbn.heatmap(final_matrix,
                cmap = [(239/255,29/255,31/255),
                        (165/255,165/255,165/255),
                        (28/255,172/255,76/255)], annot=True)
    plt.show()