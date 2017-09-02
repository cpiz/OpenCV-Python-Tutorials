# coding=utf-8
from pylab import *

if __name__ == "__main__":
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(X), np.sin(X)
    plot(X, C)
    plot(X, S)
    show()
