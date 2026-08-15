import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
import tempfile
import os


class SpeechRecognizer:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.recognizer.energy_threshold = 500
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.dynamic_energy_adjustment_damping = 0.15
        self.recognizer.pause_threshold = 0.8
        self.recognizer.phrase_threshold = 0.3
        self.recognizer.non_speaking_duration = 0.5

        self.sample_rate = 16000
        self.channels = 1
        # Realtek laptop microphone
        self.device = 2
        self.record_seconds = 4

    def _find_input_device(self):
        try:
            devices = sd.query_devices()
            if not isinstance(devices, (list, tuple)):
                return None

            for index, device in enumerate(devices):
                name = str(device[0]).lower()
                if "microphone" in name or "mic" in name:
                    if "output" not in name and "speaker" not in name:
                        return index

            return None
        except Exception:
            return None

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
                dtype="int16",
                device=self.device
            )
            sd.wait()

        except Exception as error:
            print("Microphone error:", error)
            return ""

        if abs(audio_data).max() < 100:
            print("No voice detected.")
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
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.record(source, duration=self.record_seconds)

            text = self.recognizer.recognize_google(audio)

            print("You:", text)
            return text.lower().strip()

        except sr.UnknownValueError:
            print("Could not understand.")
            return ""

        except sr.RequestError as error:
            print("Speech recognition error:", error)
            return ""

        finally:
            if temp_file and os.path.exists(temp_file):
                os.remove(temp_file)