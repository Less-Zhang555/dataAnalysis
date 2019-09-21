import matplotlib.pyplot as plt
from matplotlib import font_manager


my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/simkai.ttf", size=15)  # 修改matplotlib的默认字体

size = [30, 15, 10, 45]  # 各部分大小
label_list = ["Hogs", "Frogs", "Logs", "Dogs"]  # 各部分标签
color = ["orange", "blue", "red", "green"]  # 各部分颜色
explode = [0.05, 0, 0, 0]  # 各部分突出值
"""
绘制饼图
explode：设置各部分突出
label:设置各部分标签
labeldistance:设置标签文本距圆心位置，1.1表示1.1倍半径
autopct：设置圆里面文本
shadow：设置是否有阴影
counterclock:设置是否逆时针
startangle：起始角度，默认从0开始逆时针转
pctdistance：设置圆内文本距圆心距离,0.5表示0.5倍半径
返回值:
patches : matplotlib.patches.Wedge列表(扇形实例)
l_text：label matplotlib.text.Text列表(标签实例)
p_text：label matplotlib.text.Text列表(百分比标签实例)
"""
plt.figure(figsize=(7, 10), dpi=80)
plt.title("各个部分占比", fontproperties=my_font)
patches, l_text, p_text = plt.pie(size,
                                  explode=explode,
                                  colors=color,
                                  labels=label_list,
                                  labeldistance=1.1,
                                  autopct="%.1f%%",
                                  shadow=True,
                                  startangle=270,
                                  counterclock=False,
                                  pctdistance=0.6)

for t in l_text:
    t.set_fontproperties(my_font)

for t in p_text:
    t.set_size(18)

# for i in patches:
#     i.set_color('pink')
#     break

plt.legend(prop=my_font)
plt.show()
