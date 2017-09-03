# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

# 散点图
if __name__ == "__main__":
    n = 1024
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(Y, X)  # 颜色映射

    # 画布准备
    plt.axes([0.025, 0.025, 0.95, 0.95])
    plt.xlim(-1.5, 1.5), plt.xticks([])
    plt.ylim(-1.5, 1.5), plt.yticks([])

    # 绘制散点图
    plt.scatter(X, Y, s=75, c=T, alpha=.5)

    plt.show()
