import cv2
import numpy as np


def draw_circle(event, x, y, flags, param):
    global drawing, lastX, lastY, img

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        lastX, lastY = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img = cv2.line(img, (lastX, lastY), (x, y), (0, 0, 255))
            lastX, lastY = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        lastX, lastY = -1, -1


# Create a black image, a window and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

drawing = False
lastX, lastY = -1, -1

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:  # ESC
        break
cv2.destroyAllWindows()
