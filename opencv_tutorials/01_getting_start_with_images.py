# coding=utf-8
import cv2
from matplotlib import pyplot as plt

if __name__ == "__main__":
    # read image
    imgColor = cv2.imread('liushishi.jpg', cv2.IMREAD_COLOR)
    cv2.imshow('imgColor', imgColor)  # create window and show image

    imgGray = cv2.imread('liushishi.jpg', cv2.IMREAD_GRAYSCALE)  # Gray Mode
    cv2.namedWindow('imgColor', cv2.WINDOW_NORMAL)  # create a window
    cv2.imshow('imgColor', imgColor)  # show image in special window

    # wait for any key
    key = cv2.waitKey(0)

    if key == ord('s'):  # wait for s to exit
        # save the image in PNG format in the working directory
        cv2.imwrite('liushishi_gray.png', imgGray)
    cv2.destroyAllWindows()  # close

    plt.imshow(imgGray, cmap='gray', interpolation='bicubic')
    # plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()
