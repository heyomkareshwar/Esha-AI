from assistant.state import AssistantState
from assistant.speech import SpeechRecognizer
from assistant.wake_sound import WakeSound
from assistant.commands import CommandHandler
from assistant.speaker import Speaker


class IshaCore:

    def __init__(self):
        self.state = AssistantState.IDLE

        self.speech = SpeechRecognizer()
        self.wake_sound = WakeSound()
        self.commands = CommandHandler()
        self.speaker = Speaker()

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

            if "isha" in text:
                self.set_state(
                    AssistantState.WAKE
                )

                self.wake_sound.play()

                return True

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

        if not command:

            response = (
                "I didn't hear a command."
            )

            self.speak(response)

            return

        response = self.commands.execute(
            command
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

        self.wait_for_wake_word()

        command = self.listen_for_command()

        self.process_command(command)

    def run(self):

        print(
            "\n🤖 Isha is ready."
        )

        print(
            "Say 'Isha' to wake me up."
        )

        while True:

            try:

                self.run_once()

            except KeyboardInterrupt:

                print(
                    "\n🛑 Isha stopped."
                )

                self.set_state(
                    AssistantState.IDLE
                )

                break

            except Exception as error:

                print(
                    "[ISHA ERROR]",
                    error
                )