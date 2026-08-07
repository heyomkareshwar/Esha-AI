import pyttsx3


class Speaker:

    def __init__(self):
        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 170)

    def speak(self, text):
        self.engine.stop()
        self.engine.say(text)
        self.engine.runAndWait()