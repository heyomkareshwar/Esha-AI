class VisionState:
    def __init__(self):
        self.objects = []

    def update(self, objects):
        self.objects = objects

    def get_objects(self):
        return self.objects

    def clear(self):
        self.objects = []