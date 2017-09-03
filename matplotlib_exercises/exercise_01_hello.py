# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(X), np.sin(X)
    plt.plot(X, C)
    plt.plot(X, S)
    plt.show()
