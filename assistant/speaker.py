import pyttsx3


class Speaker:

    def __init__(self):
        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 165)
        self.engine.setProperty("volume", 1.0)

        # Force Microsoft Zira female voice
        zira_id = (
            r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech"
            r"\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        )

        self.engine.setProperty("voice", zira_id)

        print("Selected voice: Microsoft Zira Desktop")

    def speak(self, text):
        print("Esha:", text)

        self.engine.stop()
        self.engine.say(text)
        self.engine.runAndWait()