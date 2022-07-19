from cProfile import label
from scipy import signal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
from pandas import DataFrame,Series
#file = open('C:/Users/Administrator/Desktop/语义定位手稿/gyr_synthetic_tran-2.txt')
x_deepnavi=[0, 0.25, 0.5, 0.75,   1,   1.25, 1.5,  1.75,    2]

y_inloc = [0, 0.312, 0.52, 0.64, 0.714, 0.758,  0.796, 0.812, 0.828]
y_GSPV =  [0, 0.35, 0.57, 0.67, 0.736, 0.79,  0.84, 0.872, 0.888]
y_HAIL =  [0, 0.22, 0.315, 0.418, 0.508, 0.645, 0.737,  0.769,  0.787]
y_efiloc= [0, 0.29, 0.4616, 0.592, 0.681, 0.726, 0.765, 0.79, 0.815]
y_efilocpv=[0, 0.3, 0.505, 0.627, 0.711,0.777, 0.82, 0.841, 0.859]
# for line in file:
#     if line != "\n":
#         data.append(line)
# print(len(data))
#data = file.readlines()
#画图
#figure(figsize=(16,8),dpi=200)

rcParams['font.sans-serif']=['SimHei'] #显示中文字符
rcParams['axes.unicode_minus'] = False

config = {
    "font.family":'Time New',  # 设置字体类型
    #"font.size": ,
#     "mathtext.fontset":'stix',
}
rcParams.update(config)

plt.xlabel('Distance threshold (meters)',size = 18)#横坐标命名
plt.ylabel('CDF',size = 20)
# x=np.arange(0.2,3)
plt.axis([0.2, 2, 0,1])



#plt.plot(data0_1000,'b',label='Gyroscope data')
#plt.plot(data1007_2025,'b',label='Gyroscope data')
plt.plot(x_deepnavi,y_inloc,'b',label='InLoc',linestyle='-.',marker='o')
plt.plot(x_deepnavi,y_GSPV,'y',label='GSPV',Marker='^')   #linestyle='--'
plt.plot(x_deepnavi,y_HAIL,'purple',label='HAIL',linestyle='-',Marker='s')
plt.plot(x_deepnavi,y_efiloc,'green',label='EfiLoc',Marker='v') #linestyle=':',
plt.plot(x_deepnavi,y_efilocpv,'r',label='EfiLocPV',Marker='*')

#plt.gcf().set_facecolor(np.ones(3)*240/255)   #生成画布网格大小
plt.grid()  #生成网格
plt.title("Weak texture", fontsize=16)  # 标题
plt.legend(loc='lower right',fontsize=14)#标签显示位置和大小   upper, lower
plt.subplots_adjust(top=0.936, bottom=0.111, right=0.838, left=0.251, hspace=0, wspace=0)
plt.savefig("Weak texture-LOC.png", dpi = 500)
plt.show()

# markeredgecolor 或 mec 标记边缘颜色
# markeredgewidth 或 mew 标记边缘宽度
# markerfacecolor 或 mfc 标记面颜色
# markerfacecoloralt 或 mfcalt
# markersize 或 ms 标记大小