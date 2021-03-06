# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
    plt.figure(figsize=(8, 6), dpi=80)

    # 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
    plt.subplot(1, 1, 1)

    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(X), np.sin(X)

    # 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
    plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cos")

    # 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
    plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="sin")

    plt.legend(loc='upper left')

    # 设置横轴的上下限
    plt.xlim(X.min() * 1.1, X.max() * 1.1)

    # 设置横轴记号
    # xticks(np.linspace(-4, 4, 9, endpoint=True))
    # xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
    plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

    # 设置纵轴的上下限
    plt.ylim(C.min() * 1.1, C.max() * 1.1)

    # 设置纵轴记号
    # yticks(np.linspace(-1, 1, 5, endpoint=True))
    # yticks([-1, 0, +1])
    plt.yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])

    # 移动脊柱
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=1))

    # 给特殊点做注释
    t = 2 * np.pi / 3
    plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2, linestyle="--")  # 纵线
    plt.scatter([t, ], [np.cos(t), ], 50, color='blue')  # 打1个点

    plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',  # 公式标注
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    plt.plot([t, t], [0, np.sin(t)], color='red', linewidth=2, linestyle="--")
    plt.scatter([t, ], [np.sin(t), ], 50, color='red')

    plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    # 以分辨率 72 来保存图片
    # savefig("exercice_2.png", dpi=72)

    # 在屏幕上显示
    plt.show()
