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

        # Continuous conversation settings
        self.conversation_mode = False

    def set_state(self, state):
        self.state = state

        print(
            f"[ISHA] State: {state.value.upper()}"
        )

    # ==========================================
    # WAIT FOR WAKE WORD
    # ==========================================

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

            # Remove wake word
            command = text.replace(
                "isha",
                "",
                1
            ).strip()

            # ------------------------------------------
            # "Isha, open YouTube"
            # ------------------------------------------

            if command:

                print(
                    f"[ISHA] Direct command: {command}"
                )

                return command

            # ------------------------------------------
            # Just "Isha"
            # ------------------------------------------

            return None

    # ==========================================
    # LISTEN FOR COMMAND
    # ==========================================

    def listen_for_command(self):

        self.set_state(
            AssistantState.LISTENING
        )

        command = self.speech.listen()

        if command:
            command = command.lower().strip()

        return command

    # ==========================================
    # PROCESS COMMAND
    # ==========================================

    def process_command(self, command):

        if not command:
            return

        self.set_state(
            AssistantState.THINKING
        )

        result = self.brain.think(
            command
        )

        response = result["response"]

        print(
            f"[ISHA] Intent: {result['type']}"
        )

        self.speak(response)

    # ==========================================
    # SPEAK
    # ==========================================

    def speak(self, text):

        self.set_state(
            AssistantState.SPEAKING
        )

        self.speaker.speak(text)

        self.set_state(
            AssistantState.IDLE
        )

    # ==========================================
    # CONTINUOUS CONVERSATION
    # ==========================================

    def conversation_loop(self):

        self.conversation_mode = True

        print(
            "[ISHA] Conversation mode ON."
        )

        while self.conversation_mode:

            command = self.listen_for_command()

            # ------------------------------------------
            # Silence / no speech
            # ------------------------------------------

            if not command:

                print(
                    "[ISHA] No follow-up detected."
                )

                self.conversation_mode = False

                self.set_state(
                    AssistantState.IDLE
                )

                break

            print(
                f"[ISHA] Follow-up: {command}"
            )

            # ------------------------------------------
            # Exit conversation
            # ------------------------------------------

            if any(
                phrase in command
                for phrase in [
                    "stop listening",
                    "go to sleep",
                    "sleep",
                    "that's all",
                    "thats all",
                    "goodbye"
                ]
            ):

                self.speak(
                    "Alright. I'll be here when you need me."
                )

                self.conversation_mode = False

                break

            # ------------------------------------------
            # Process follow-up
            # ------------------------------------------

            self.process_command(
                command
            )

    # ==========================================
    # ONE COMPLETE CYCLE
    # ==========================================

    def run_once(self):

        # ------------------------------------------
        # Wait for "Isha"
        # ------------------------------------------

        command = self.wait_for_wake_word()

        # ------------------------------------------
        # Direct command:
        #
        # "Isha, open YouTube"
        # ------------------------------------------

        if command:

            self.process_command(
                command
            )

        # ------------------------------------------
        # Wake only:
        #
        # "Isha"
        # ------------------------------------------

        else:

            command = self.listen_for_command()

            if not command:
                return

            self.process_command(
                command
            )

        # ------------------------------------------
        # Enter conversation mode
        # ------------------------------------------

        self.conversation_loop()

    # ==========================================
    # MAIN LOOP
    # ==========================================

    def run(self):

        print("\n🤖 Isha is ready.")
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

                break

            except Exception as error:

                print(
                    "[ISHA ERROR]",
                    error
                )