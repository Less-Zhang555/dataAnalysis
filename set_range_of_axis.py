import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-10, 11, 1)
y = x ** 2
plt.plot(x, y)

# 设置x轴的显示范围，同理可得y轴
# plt.xlim([-5, 5])  # 可以调x轴的左右两边
# plt.xlim(xmin=-4)  # 只调一边
# plt.xlim(xmax=4)  # 只调一边

plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.show()
