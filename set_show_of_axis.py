import matplotlib.pyplot as plt


x = [-3, -2, -1, 0, 1, 2, 3]
y = range(0, 14, 2)

# plt.figure(figsize=(7, 10), dpi=80)  # 设置画布规格

ax = plt.gca()  # 获取当前画布上的图像

# 设置图像的包围线
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('red')
ax.spines['left'].set_color('green')

#  设置底边的移动范围，data:所要移动轴到交叉轴的坐标
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))  # 0意味着y轴在x=0的位置

plt.plot(x, y)
plt.show()

