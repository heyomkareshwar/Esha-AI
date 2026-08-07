from ultralytics import YOLO


class Detector:

    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def detect(self, frame):

        results = self.model(
            frame,
            verbose=False
        )

        annotated = results[0].plot()

        detected = []

        for box in results[0].boxes:

            cls = int(box.cls)

            name = self.model.names[cls]

            confidence = float(box.conf)

            detected.append(
                (
                    name,
                    confidence
                )
            )

        return annotated, detected