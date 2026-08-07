import cv2

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
)

from vision.camera import Camera
from vision.detector import Detector

from ui.object_panel import ObjectPanel
from ui.controls import Controls
from ui.status_bar import AIStatusBar

from vision.fps import FPSCounter
from assistant.vision_state import VisionState


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("🤖 Esha AI")
        self.resize(1400, 800)

        self.camera = Camera()
        self.detector = Detector()

        self.fps = FPSCounter()
        self.state = VisionState()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        central = QWidget()
        self.setCentralWidget(central)

        root = QVBoxLayout(central)

        body = QHBoxLayout()
        root.addLayout(body)

        self.controls = Controls()
        root.addWidget(self.controls)

        self.object_panel = ObjectPanel()

        from PySide6.QtWidgets import QLabel
        self.view = QLabel("Camera Preview")
        self.view.setAlignment(Qt.AlignCenter)
        self.view.setMinimumSize(900, 600)

        body.addWidget(self.view, 3)
        body.addWidget(self.object_panel, 1)

        self.ai_status = AIStatusBar()
        self.setStatusBar(self.ai_status)

        self.controls.start_btn.clicked.connect(self.start_camera)
        self.controls.stop_btn.clicked.connect(self.stop_camera)

    def start_camera(self):
        if self.camera.start():
            self.timer.start(30)

    def update_frame(self):
        ok, frame = self.camera.read()
        if not ok:
            return

        detected = []

        result = self.detector.detect(frame)

        if isinstance(result, tuple):
            frame, detected = result
        else:
            frame = result

        self.state.update(detected)
        self.object_panel.update_objects(detected)

        self.fps.update()
        self.ai_status.update_status(
            self.fps.value(),
            True
        )

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        h, w, ch = rgb.shape

        image = QImage(
            rgb.data,
            w,
            h,
            ch * w,
            QImage.Format_RGB888
        )

        pixmap = QPixmap.fromImage(image)

        self.view.setPixmap(
            pixmap.scaled(
                self.view.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

    def stop_camera(self):
        self.timer.stop()
        self.camera.stop()
        self.view.clear()
        self.view.setText("Camera Preview")
        self.ai_status.update_status(0, False)

    def closeEvent(self, event):
        self.stop_camera()
        event.accept()