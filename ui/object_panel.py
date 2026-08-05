from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QListWidget

class ObjectPanel(QWidget):
    def __init__(self):
        super().__init__()
        l=QVBoxLayout(self)
        l.addWidget(QLabel("Detected Objects"))
        self.list=QListWidget()
        l.addWidget(self.list)
        self.count=QLabel("Objects: 0")
        l.addWidget(self.count)

    def update_objects(self,objects):
        self.list.clear()
        for n,c in objects:
            self.list.addItem(f"{n} ({c*100:.1f}%)")
        self.count.setText(f"Objects: {len(objects)}")
