

import cv2
import os
os.environ["QT_QPA_PLATFORM"] = "xcb"

capture = cv2.VideoCapture(0)

while True:
    _, frame = capture.read()
    cv2.imshow("output", frame)

    if cv2.waitKey(10) == ord("q"):
        break

capture.release()
cv2.destroyWindow()
