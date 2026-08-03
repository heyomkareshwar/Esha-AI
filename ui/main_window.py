from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QStatusBar
)

from PySide6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("🤖 Esha AI")

        self.resize(1400, 850)

        self.build_ui()

    def build_ui(self):

        central = QWidget()

        self.setCentralWidget(central)

        root = QVBoxLayout(central)

        # ==========================
        # Title
        # ==========================

        title = QLabel("🤖 Esha AI")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            font-size:32px;
            font-weight:bold;
            padding:15px;
        """)

        root.addWidget(title)

        # ==========================
        # Camera Area
        # ==========================

        self.camera_frame = QFrame()

        self.camera_frame.setMinimumHeight(550)

        self.camera_frame.setStyleSheet("""
            background:#202020;
            border:2px solid #444;
            border-radius:10px;
        """)

        camera_layout = QVBoxLayout(self.camera_frame)

        self.camera_label = QLabel("Camera Preview")

        self.camera_label.setAlignment(Qt.AlignCenter)

        self.camera_label.setStyleSheet("""
            color:white;
            font-size:24px;
        """)

        camera_layout.addWidget(self.camera_label)

        root.addWidget(self.camera_frame)

        # ==========================
        # Buttons
        # ==========================

        buttons = QHBoxLayout()

        self.start_btn = QPushButton("▶ Start Camera")

        self.stop_btn = QPushButton("■ Stop Camera")

        self.capture_btn = QPushButton("📸 Capture")

        self.exit_btn = QPushButton("Exit")

        buttons.addWidget(self.start_btn)

        buttons.addWidget(self.stop_btn)

        buttons.addWidget(self.capture_btn)

        buttons.addStretch()

        buttons.addWidget(self.exit_btn)

        root.addLayout(buttons)

        # ==========================
        # Status Bar
        # ==========================

        status = QStatusBar()

        self.setStatusBar(status)

        status.showMessage("Ready")

        # ==========================
        # Signals
        # ==========================

        self.exit_btn.clicked.connect(self.close)