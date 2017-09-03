# coding=utf-8
import cv2


def record():
    cap = cv2.VideoCapture(0)  # from camera index 0

    # Define the codec and create VideoWriter object
    # fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D') # 无法工作
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    out = cv2.VideoWriter('output.avi', fourcc, 20, (640, 480))

    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # frame = cv2.flip(frame, 0)
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('frame', frame)

        if cv2.waitKey(40) & 0xFF == 27:  # 通过waitKey实现了帧率控制
            break

    # When everything done, release the capture
    out.release()
    cap.release()
    cv2.destroyAllWindows()


def replay():
    cap = cv2.VideoCapture(r'output.avi')

    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', gray)

        if cv2.waitKey(40) & 0xFF == 27:  # 通过waitKey实现了帧率控制
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    record()
    replay()
