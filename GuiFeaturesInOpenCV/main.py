import numpy as np
import cv2

if __name__ == "__main__":
    # read image
    imgColor = cv2.imread('liushishi.jpg', cv2.IMREAD_COLOR)
    cv2.imshow('imgColor', imgColor)  # create window and show image

    imgGray = cv2.imread('liushishi.jpg', cv2.IMREAD_GRAYSCALE)  # Gray Mode
    cv2.namedWindow('imgColor', cv2.WINDOW_NORMAL)  # create a window
    cv2.imshow('imgColor', imgColor)  # show image in special window

    # wait for any key
    cv2.waitKey(0)

    # close
    cv2.destroyAllWindows()

    # save the image in PNG format in the working directory
    cv2.imwrite('liushishi_gray.png', imgGray)
