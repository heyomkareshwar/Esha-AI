import time


class SpeechCooldown:

    def __init__(self, seconds=5):
        self.seconds = seconds
        self.last_spoken = 0

    def can_speak(self):
        current_time = time.time()

        if current_time - self.last_spoken >= self.seconds:
            return True

        return False

    def reset(self):
        self.last_spoken = time.time()