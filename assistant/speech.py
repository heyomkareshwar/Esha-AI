import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
import tempfile
import os


class SpeechRecognizer:

    def __init__(self):
        self.recognizer = sr.Recognizer()

        self.sample_rate = 16000
        self.channels = 1
        self.record_seconds = 5

    def listen(self):

        print("\n🎤 Listening...")

        try:
            audio_data = sd.rec(
                int(
                    self.record_seconds *
                    self.sample_rate
                ),
                samplerate=self.sample_rate,
                channels=self.channels,
                dtype="int16"
            )

            sd.wait()

        except Exception as error:
            print("Microphone error:", error)
            return ""

        temp_file = None

        try:
            with tempfile.NamedTemporaryFile(
                suffix=".wav",
                delete=False
            ) as file:

                temp_file = file.name

            sf.write(
                temp_file,
                audio_data,
                self.sample_rate
            )

            with sr.AudioFile(temp_file) as source:

                audio = self.recognizer.record(
                    source
                )

            text = self.recognizer.recognize_google(
                audio
            )

            print("You:", text)

            return text.lower()

        except sr.UnknownValueError:

            print("Could not understand.")
            return ""

        except sr.RequestError as error:

            print(
                "Speech recognition error:",
                error
            )

            return ""

        finally:

            if temp_file and os.path.exists(
                temp_file
            ):
                os.remove(temp_file)