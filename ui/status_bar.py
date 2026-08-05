from PySide6.QtWidgets import QStatusBar

class AIStatusBar(QStatusBar):
    def __init__(self):
        super().__init__()
        self.showMessage("AI Ready")
