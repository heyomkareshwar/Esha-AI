from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout
)


class Controls(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)

        self.start_btn = QPushButton("▶ Start")

        self.stop_btn = QPushButton("■ Stop")

        self.capture_btn = QPushButton("📸 Capture")

        self.voice_btn = QPushButton("🎤 Talk to Esha")

        layout.addWidget(self.start_btn)

        layout.addWidget(self.stop_btn)

        layout.addWidget(self.capture_btn)

        layout.addWidget(self.voice_btn)

        layout.addStretch()