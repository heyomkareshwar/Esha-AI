import pyttsx3


class Speaker:

    def __init__(self):
        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 165)
        self.engine.setProperty("volume", 1.0)

        # Set female voice
        voices = self.engine.getProperty("voices")
        
        # Try to find Zira (female voice)
        female_voice = None
        for voice in voices:
            if "zira" in voice.name.lower():
                female_voice = voice.id
                break
        
        # If Zira not found, use first female voice available
        if female_voice is None:
            for voice in voices:
                if voice.gender.lower() == "female":
                    female_voice = voice.id
                    break
        
        # Fallback: use voice at index 1 (usually female on Windows)
        if female_voice is None and len(voices) > 1:
            female_voice = voices[1].id
        
        if female_voice:
            self.engine.setProperty("voice", female_voice)
            print(f"Selected voice: {voices[0].name if not female_voice else 'Female voice'}")
        else:
            print("No female voice available")

    def speak(self, text):
        print("Isha:", text)

        self.engine.stop()
        self.engine.say(text)
        self.engine.runAndWait()