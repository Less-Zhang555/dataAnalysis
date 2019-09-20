"""
使用matplotlib.pyplot模块绘制折线图基本步骤：
    1.导入matplotlib.pyplot模块
    2.获取横纵坐标的值
    3.通过plot()绘图
    4.savefig()保存图片
    5.show()展示图片
"""


import matplotlib.pyplot as plt
from matplotlib import font_manager

x = range(11, 31)
y1 = [2, 1, 1, 2, 3, 4, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1, 1, 1]
y2 = [1, 0, 3, 1, 2, 3, 4, 3, 1, 2, 1, 1, 1, 1, 1, 6, 8, 4, 10, 8]

my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/simkai.ttf", size=13)  # 修改matplotlib的默认字体

plt.grid(alpha=0.8)  # 绘制网格线，alpha参数设置网格线的透明度，取值范围（0-1）

plt.figure(figsize=(7, 10), dpi=80)  # 设置图片的大小，此方法要在plot()之前调用
"""
1.figsizez指定图片的宽和高，单位是英寸，1英寸=2.54厘米，A4纸是21*30cm的纸张
2.dpi指定图片的分辨率，即每英寸有多少个像素（图像元素：构成屏幕上图像的小点）
"""

plt.xlabel("年龄", fontproperties=my_font, rotation=45)  # 添加x轴信息
plt.ylabel("个数", fontproperties=my_font, rotation=45)  # 添加y轴信息
plt.title("每年交女朋友个数", fontproperties=my_font)  # 添加标题信息

x_ticks_label = ["{}岁".format(i) for i in x]  # 构造x轴刻度标签
plt.xticks(x, x_ticks_label, fontproperties=my_font, rotation=45)  # 刻画x轴刻度标签,第一个参数传入一个类列表类型数据
y_ticks_label = ["{}位".format(i) for i in range(11)]  # 构造y轴刻度标签
plt.yticks(range(11), y_ticks_label, fontproperties=my_font)  # 刻画y轴刻度标签，第一个参数传入一个类列表类型数据

plt.plot(x, y1, color="red", alpha=0.8, linestyle="--", linewidth=3, marker="o", markersize=10, label="曹操")
plt.plot(x, y2, color="green", alpha=0.8, linestyle=":", linewidth=5, marker="*", markersize=13, label="关羽")

"""
1.marker参数设置折点样式
2.label参数为每条折线的标签，设置图例时使用
"""
plt.legend(prop=my_font, loc="upper left")  # 显示图例,此方法要在plot()之后调用，
"""
1.prop设置所要显示图例的字体,只有这里的参数是prop，其余的地方都是fontproperties
2.loc设置图例显示的位置：upper right  lower right lower left   center left    upper center
"""
# plt.savefig("./line_chart.png")  # 图片格式可以保存为.svg这种矢量图格式，这种矢量图在前端网页放大是不会出现锯齿

plt.show()  # 调用show()函数后会释放figure资源，若在show()之后保存图片会得到空白的图片

