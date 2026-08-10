import math
import wave
import struct
import tempfile
import os

import winsound


class WakeSound:

    def __init__(self):
        self.sample_rate = 44100

    def _create_tone(self, frequency, duration):
        samples = int(self.sample_rate * duration)

        data = bytearray()

        for i in range(samples):
            value = int(
                16000 *
                math.sin(
                    2 * math.pi *
                    frequency *
                    i /
                    self.sample_rate
                )
            )

            data.extend(
                struct.pack(
                    "<h",
                    value
                )
            )

        return bytes(data)

    def _create_wav(self):
        # Short assistant-style two-tone chime
        tone1 = self._create_tone(
            880,
            0.10
        )

        tone2 = self._create_tone(
            1320,
            0.14
        )

        silence = bytes(
            int(self.sample_rate * 0.025) * 2
        )

        audio = (
            tone1 +
            silence +
            tone2
        )

        file = tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        )

        path = file.name
        file.close()

        with wave.open(path, "wb") as wav:

            wav.setnchannels(1)
            wav.setsampwidth(2)
            wav.setframerate(
                self.sample_rate
            )

            wav.writeframes(audio)

        return path

    def play(self):

        path = self._create_wav()

        try:
            winsound.PlaySound(
                path,
                winsound.SND_FILENAME
            )

        finally:

            if os.path.exists(path):
                os.remove(path)

    def run(self):

        print("\n🤖 Isha is ready.")
        print("Say 'Isha' to wake me up.")

        while True:

            try:
                self.run_once()

            except KeyboardInterrupt:
                print("\nIsha stopped.")
                break

            except Exception as error:
                print("Assistant error:", error)