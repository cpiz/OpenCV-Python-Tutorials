# coding=utf-8
from pylab import *

if __name__ == "__main__":
    n = 256
    X = np.linspace(-np.pi, np.pi, n, endpoint=True)
    Y = np.sin(2 * X)

    subplot(2, 1, 1)
    # plot(X, Y + 1, color='blue', alpha=1.00)
    plt.fill_between(X, 0, Y, color='blue', alpha=.25)
    plt.xlim(-np.pi, np.pi), plt.xticks([])  # 清除x轴标尺
    plt.ylim(-1, 1), plt.yticks([])  # 清除y轴标尺

    subplot(2, 1, 2)
    # plot(X, Y - 1, color='blue', alpha=1.00)
    plt.fill_between(X, 0, Y, color='red', alpha=.25)
    plt.xlim(-np.pi, np.pi), plt.xticks([])
    plt.ylim(-1, 1), plt.yticks([])

    show()
