import cv2
from PySide6.QtCore import Qt,QTimer
from PySide6.QtGui import QImage,QPixmap
from PySide6.QtWidgets import QMainWindow,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QPushButton,QStatusBar
from vision.camera import Camera

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Esha AI")
        self.resize(1200,800)
        self.camera=Camera()
        self.timer=QTimer()
        self.timer.timeout.connect(self.update_frame)
        c=QWidget();self.setCentralWidget(c);l=QVBoxLayout(c)
        t=QLabel("Esha AI");t.setAlignment(Qt.AlignCenter);l.addWidget(t)
        self.camera_label=QLabel("Camera Preview");self.camera_label.setAlignment(Qt.AlignCenter);self.camera_label.setMinimumHeight(550);l.addWidget(self.camera_label)
        r=QHBoxLayout();b1=QPushButton("Start Camera");b2=QPushButton("Stop Camera");r.addWidget(b1);r.addWidget(b2);l.addLayout(r)
        self.setStatusBar(QStatusBar());self.statusBar().showMessage("Ready");b1.clicked.connect(self.start_camera);b2.clicked.connect(self.stop_camera)
    def start_camera(self):
        if self.camera.start(): self.timer.start(30)
    def update_frame(self):
        ok,f=self.camera.read();
        if not ok:return
        f=cv2.cvtColor(f,cv2.COLOR_BGR2RGB);h,w,ch=f.shape
        img=QImage(f.data,w,h,ch*w,QImage.Format_RGB888)
        self.camera_label.setPixmap(QPixmap.fromImage(img).scaled(self.camera_label.size(),Qt.KeepAspectRatio))
    def stop_camera(self):
        self.timer.stop();self.camera.stop();self.camera_label.setText("Camera Preview");self.camera_label.setPixmap(QPixmap())
    def closeEvent(self,e):
        self.stop_camera();e.accept()
