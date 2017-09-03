import cv2
import numpy as np

if __name__ == '__main__':
    # Create a blank image
    img = np.zeros((512, 512, 3), np.uint8)

    # Draw a diagonal blue line with thickness of 5px
    img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

    #
    img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

    img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

    img = cv2.ellipse(img, (256, 256), (100, 50), 90, 0, 180, 255, -1)

    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    # pts = pts.reshape((-1, 1, 2))
    img = cv2.polylines(img, [pts], True, (0, 255, 255))

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'OpenCV', (10, 500), font, 2, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('draw', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
