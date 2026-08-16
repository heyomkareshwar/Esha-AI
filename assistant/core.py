from assistant.state import AssistantState
from assistant.speech import SpeechRecognizer
from assistant.wake_sound import WakeSound
from assistant.speaker import Speaker
from assistant.brain import IshaBrain


class IshaCore:

    def __init__(self):
        self.state = AssistantState.IDLE

        self.speech = SpeechRecognizer()
        self.wake_sound = WakeSound()
        self.speaker = Speaker()
        self.brain = IshaBrain()

    def set_state(self, state):
        self.state = state

        print(
            f"[ISHA] State: {state.value.upper()}"
        )

    def wait_for_wake_word(self):

        self.set_state(
            AssistantState.IDLE
        )

        while True:

            text = self.speech.listen()

            if not text:
                continue

            text = text.lower().strip()

            print(
                f"[ISHA] Heard: {text}"
            )

            if "isha" not in text:
                continue

            self.set_state(
                AssistantState.WAKE
            )

            self.wake_sound.play()

            command = text.replace(
                "isha",
                "",
                1
            ).strip()

            if command:
                print(
                    f"[ISHA] Direct command: {command}"
                )
                return command

            return None

    def listen_for_command(self):

        self.set_state(
            AssistantState.LISTENING
        )

        command = self.speech.listen()

        return command

    def process_command(self, command):

        self.set_state(
            AssistantState.THINKING
        )

        result = self.brain.think(command)

        response = result["response"]

        print(
            f"[ISHA] Intent: {result['type']}"
        )

        self.speak(response)

    def speak(self, text):

        self.set_state(
            AssistantState.SPEAKING
        )

        self.speaker.speak(text)

        self.set_state(
            AssistantState.IDLE
        )

    def run_once(self):

        command = self.wait_for_wake_word()

        if command:
            self.process_command(command)
            return

        command = self.listen_for_command()
        self.process_command(command)

    def run(self):

        print("\n🤖 Isha is ready.")
        print("Say 'Isha' to wake me up.")

        while True:

            try:

                self.run_once()

            except KeyboardInterrupt:

                print("\n🛑 Isha stopped.")

                break

            except Exception as error:

                print(
                    "[ISHA ERROR]",
                    error
                )