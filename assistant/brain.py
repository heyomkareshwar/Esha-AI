from assistant.commands import CommandHandler


class IshaBrain:

    def __init__(self):
        self.commands = CommandHandler()

    def think(self, text):
        text = text.lower().strip()

        if not text:
            return {
                "type": "conversation",
                "response": "I didn't hear anything."
            }

        # Remove wake word if it reaches the brain
        text = text.replace("isha", "").strip()

        # Desktop actions
        action_words = (
            "open ",
            "launch ",
            "start ",
            "run "
        )

        if text.startswith(action_words):
            response = self.commands.execute(text)

            return {
                "type": "action",
                "response": response
            }

        # Greetings
        if any(word in text for word in (
            "hello",
            "hi",
            "hey"
        )):
            return {
                "type": "conversation",
                "response": "Hello. I'm Isha. How can I help you?"
            }

        # Identity
        if "who are you" in text or "what are you" in text:
            return {
                "type": "conversation",
                "response": (
                    "I'm Isha, your desktop AI assistant."
                )
            }

        # Help
        if "what can you do" in text:
            return {
                "type": "conversation",
                "response": (
                    "I can control supported desktop applications, "
                    "open websites, use your camera vision system, "
                    "and assist you with commands."
                )
            }

        return {
            "type": "unknown",
            "response": (
                "I don't know how to do that yet."
            )
        }