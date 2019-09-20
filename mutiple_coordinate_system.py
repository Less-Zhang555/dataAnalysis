import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1, 10)
fig = plt.figure(figsize=(7, 10), dpi=80)  # 新建figure对象

# 新建子图1
ax1 = fig.add_subplot(2, 2, 1)  # add_subplot把画布平均分为四份,最后一位参数便是指象限
ax1.plot(x, x)

# 新建子图2
ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(x, x ** 2)

# 新建子图3
ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(x, x ** 3)

# 新建子图4
ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(x, np.log(x))

plt.show()
