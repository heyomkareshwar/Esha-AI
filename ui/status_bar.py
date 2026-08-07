from PySide6.QtWidgets import QStatusBar


class AIStatusBar(QStatusBar):

    def __init__(self):
        super().__init__()

        self.showMessage("AI Ready")

    def update_status(
        self,
        fps,
        running
    ):

        state = "Running" if running else "Stopped"

        self.showMessage(
            f"Camera : {state} | FPS : {fps}"
        )