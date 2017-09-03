# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


# 等高线
if __name__ == "__main__":
    n = 10
    x = np.linspace(-3, 3, 3.5 * n)
    y = np.linspace(-3, 3, 3.0 * n)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    plt.axes([0.025, 0.025, 0.95, 0.95])
    plt.imshow(Z, interpolation='nearest', cmap='bone', origin='lower')
    plt.colorbar(shrink=.92)

    plt.xticks([]), plt.yticks([])
    # savefig('../figures/imshow_ex.png', dpi=48)
    plt.show()
