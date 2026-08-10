from assistant.speech import SpeechRecognizer
from assistant.wake_sound import WakeSound
from assistant.commands import CommandHandler
from assistant.speaker import Speaker


class IshaAssistant:

    def __init__(self):
        self.speech = SpeechRecognizer()
        self.wake_sound = WakeSound()
        self.commands = CommandHandler()
        self.speaker = Speaker()

    def run_once(self):

        print("\n👂 Waiting for wake word: Isha")

        # Wait for wake word
        while True:

            text = self.speech.listen()

            if not text:
                continue

            text = text.lower().strip()

            print("Heard:", text)

            if "isha" in text:
                break

        # Wake sound
        print("✨ Isha activated!")

        self.wake_sound.play()

        # Listen for command
        print("🎤 Listening for command...")

        command = self.speech.listen()

        if not command:

            self.speaker.speak(
                "I didn't hear a command."
            )

            return

        print("Command:", command)

        # Execute command
        response = self.commands.execute(command)

        # Speak response
        self.speaker.speak(response)

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

                print(
                    "Assistant error:",
                    error
                )