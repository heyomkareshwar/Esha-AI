import time


class FPSCounter:
    def __init__(self):
        self.previous = time.time()
        self.fps = 0

    def update(self):
        current = time.time()

        diff = current - self.previous

        if diff > 0:
            self.fps = 1 / diff

        self.previous = current

    def value(self):
        return round(self.fps, 1)