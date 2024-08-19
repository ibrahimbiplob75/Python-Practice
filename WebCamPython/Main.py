import cv2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QTimer


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Window measurements
        self.window_Width = 650
        self.window_height = 450

        # Image measurements (if needed for future use)
        self.image_Width = 650
        self.image_height = 450

        self.setWindowTitle("Ibrahim Web Cam")
        self.setGeometry(100, 100, self.window_Width, self.window_height)
        self.setFixedSize(self.window_Width, self.window_height)

        # Timer setup
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)  # Corrected the connection

        self.ui()

    def ui(self):
        self.image_label = QLabel(self)
        self.image_label.setGeometry(50, 50, self.image_Width - 100, self.image_height - 100)  # Adjusted the label size
        if not self.timer.isActive():
            self.capture=cv2.VideoCapture(0)
            self.timer.start(20)
        self.show()



    def update_frame(self):
        # This method should contain the logic to update the frame from the webcam
        pass

    def save_image(self):
        # Logic to save the current image/frame
        pass

    def record(self):
        # Logic to record the webcam video
        pass

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
