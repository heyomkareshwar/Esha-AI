from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget
)


class ObjectPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Detected Objects")
        title.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        self.object_list = QListWidget()
        layout.addWidget(self.object_list)

        self.count_label = QLabel("Objects : 0")
        layout.addWidget(self.count_label)

    def update_objects(self, objects):

        self.object_list.clear()

        for name, confidence in objects:

            self.object_list.addItem(
                f"{name} ({confidence * 100:.1f}%)"
            )

        self.count_label.setText(
            f"Objects : {len(objects)}"
        )