# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

# 普通图
if __name__ == "__main__":
    n = 256
    X = np.linspace(-np.pi, np.pi, n, endpoint=True)
    Y = np.sin(2 * X)

    plt.subplot(2, 1, 1)
    plt.plot(X, Y, color='blue', alpha=.5)
    plt.fill_between(X, 0, Y, color='blue', alpha=.25)  # 填充
    plt.xlim(-np.pi, np.pi), plt.xticks([])  # 清除x轴标尺
    plt.ylim(-1, 1), plt.yticks([])  # 清除y轴标尺

    plt.subplot(2, 1, 2)
    plt.plot(X, Y, color='blue', alpha=.5)
    plt.fill_between(X, 0, Y, color='red', alpha=.25)  # 填充
    plt.xlim(-np.pi, np.pi), plt.xticks([])
    plt.ylim(-1, 1), plt.yticks([])

    plt.show()
