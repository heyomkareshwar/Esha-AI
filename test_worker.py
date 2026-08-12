import sys

from PySide6.QtWidgets import QApplication

from assistant.worker import IshaWorker


app = QApplication(sys.argv)

worker = IshaWorker()


def on_state(state):
    print("STATE:", state)


def on_heard(text):
    print("HEARD:", text)


def on_error(error):
    print("ERROR:", error)


worker.state_changed.connect(on_state)
worker.heard_text.connect(on_heard)
worker.error.connect(on_error)

worker.start()

exit_code = app.exec()

worker.stop()

sys.exit(exit_code)