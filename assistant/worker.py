from PySide6.QtCore import QThread, Signal

from assistant.core import IshaCore


class IshaWorker(QThread):

    state_changed = Signal(str)
    heard_text = Signal(str)
    response_text = Signal(str)
    error = Signal(str)

    def __init__(self):
        super().__init__()

        self.running = True
        self.isha = IshaCore()

    def run(self):

        while self.running:

            try:

                self.isha.wait_for_wake_word()

                if not self.running:
                    break

                self.state_changed.emit("wake")

                command = self.isha.listen_for_command()

                if not self.running:
                    break

                if command:
                    self.heard_text.emit(command)

                self.isha.process_command(command)

                self.state_changed.emit("idle")

            except Exception as error:

                self.error.emit(str(error))

                break

    def stop(self):

        self.running = False