# coding=utf-8
import matplotlib.pyplot as plt

# 多重网格
if __name__ == "__main__":
    fig = plt.figure()
    fig.subplots_adjust(bottom=0.025, left=0.025, top=0.975, right=0.975)

    plt.subplot(2, 1, 1)
    plt.xticks([]), plt.yticks([])

    plt.subplot(2, 3, 4)
    plt.xticks([]), plt.yticks([])

    plt.subplot(2, 3, 5)
    plt.xticks([]), plt.yticks([])

    plt.subplot(2, 3, 6)
    plt.xticks([]), plt.yticks([])

    # plt.savefig('../figures/multiplot_ex.png',dpi=48)
    plt.show()
