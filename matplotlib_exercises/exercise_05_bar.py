# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

# 条形图
if __name__ == "__main__":
    n = 12
    X = np.arange(n)
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    print Y1

    plt.axes([0.025, 0.025, 0.95, 0.95])
    plt.xlim(-.5, n), plt.xticks([])
    plt.ylim(-1.25, +1.25), plt.yticks([])

    # 画条形
    plt.bar(X, Y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

    # 画文字
    for x, y in zip(X, Y1):
        plt.text(x, y + 0.05, '%.2f' % y, ha='center', va='bottom')
    for x, y in zip(X, Y2):
        plt.text(x, -y - 0.05, '%.2f' % y, ha='center', va='top')

    plt.show()
