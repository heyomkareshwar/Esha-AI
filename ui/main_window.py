import cv2
from PySide6.QtCore import Qt,QTimer
from PySide6.QtGui import QImage,QPixmap
from PySide6.QtWidgets import QMainWindow,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QPushButton,QStatusBar

from vision.camera import Camera
from vision.detector import Detector

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Esha AI")
        self.resize(1200,800)
        self.camera=Camera()
        self.detector=Detector()
        self.timer=QTimer()
        self.timer.timeout.connect(self.update_frame)

        c=QWidget()
        self.setCentralWidget(c)
        l=QVBoxLayout(c)

        t=QLabel("🤖 Esha AI - Commit 4")
        t.setAlignment(Qt.AlignCenter)
        l.addWidget(t)

        self.view=QLabel("Camera Preview")
        self.view.setAlignment(Qt.AlignCenter)
        self.view.setMinimumHeight(600)
        l.addWidget(self.view)

        row=QHBoxLayout()
        s=QPushButton("Start")
        x=QPushButton("Stop")
        row.addWidget(s)
        row.addWidget(x)
        l.addLayout(row)

        self.setStatusBar(QStatusBar())
        self.statusBar().showMessage("Ready")

        s.clicked.connect(self.start_camera)
        x.clicked.connect(self.stop_camera)

    def start_camera(self):
        if self.camera.start():
            self.timer.start(30)

    def update_frame(self):
        ok,frame=self.camera.read()
        if not ok:return
        frame=self.detector.detect(frame)
        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        h,w,ch=rgb.shape
        img=QImage(rgb.data,w,h,ch*w,QImage.Format_RGB888)
        self.view.setPixmap(QPixmap.fromImage(img).scaled(self.view.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))

    def stop_camera(self):
        self.timer.stop()
        self.camera.stop()
        self.view.clear()
        self.view.setText("Camera Preview")

    def closeEvent(self,e):
        self.stop_camera()
        e.accept()
