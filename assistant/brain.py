from assistant.commands import CommandHandler
from assistant.memory import Memory
from assistant.llm_brain import LLMBrain
from assistant.gemini_vision import GeminiVision
from assistant.screen_vision import ScreenVision


class IshaBrain:

    def __init__(self):
        self.commands = CommandHandler()
        self.memory = Memory()
        self.llm = LLMBrain()
        self.screen = ScreenVision()
        self.vision = GeminiVision()

    # ==========================================
    # MEMORY RESPONSE HELPER
    # ==========================================

    def _response(self, response, response_type):

        self.memory.add(
            "assistant",
            response
        )

        return {
            "type": response_type,
            "response": response
        }

    # ==========================================
    # MAIN THINK FUNCTION
    # ==========================================

    def think(self, text):

        if not text:
            return self._response(
                "I didn't hear anything.",
                "conversation"
            )

        text = text.lower().strip()

        # Save user message
        self.memory.add(
            "user",
            text
        )

        # Remove wake word
        text = text.replace(
            "isha",
            "",
            1
        ).strip()

        # ==========================================
        # EMPTY REQUEST
        # ==========================================

        if not text:
            return self._response(
                "Yes? I'm listening.",
                "conversation"
            )

        # ==========================================
        # GREETINGS
        # ==========================================

        if any(
            word in text
            for word in [
                "hello",
                "hi",
                "hey",
                "hii"
            ]
        ):

            return self._response(
                "Hello. I'm Isha. How can I help you?",
                "conversation"
            )

        # ==========================================
        # IDENTITY
        # ==========================================

        if (
            "who are you" in text
            or "what are you" in text
            or "tell me about yourself" in text
        ):

            return self._response(
                "I'm Isha, your desktop AI assistant.",
                "conversation"
            )

        # ==========================================
        # CAPABILITIES
        # ==========================================

        if (
            "what can you do" in text
            or "what do you do" in text
            or "your capabilities" in text
        ):

            return self._response(
                "I can control supported desktop applications, "
                "open websites, use my vision system, remember "
                "our recent conversation, and help you with tasks.",
                "conversation"
            )

        # ==========================================
        # STATUS
        # ==========================================

        if (
            "are you there" in text
            or "are you listening" in text
            or "you there" in text
        ):

            return self._response(
                "Yes. I'm here.",
                "conversation"
            )

        # ==========================================
        # THANK YOU
        # ==========================================

        if (
            "thank you" in text
            or "thanks" in text
            or "thankyou" in text
        ):

            return self._response(
                "You're welcome.",
                "conversation"
            )

        # ==========================================
        # GOODBYE
        # ==========================================

        if any(
            word in text
            for word in [
                "goodbye",
                "bye",
                "good night"
            ]
        ):

            return self._response(
                "Alright. I'll be here when you need me.",
                "conversation"
            )

        # ==========================================
        # MEMORY — LAST USER MESSAGE
        # ==========================================

        if (
            "what did i say" in text
            or "what was my last message" in text
        ):

            previous = self.memory.last_user_message()

            if previous:

                return self._response(
                    f"You previously said: {previous}",
                    "memory"
                )

            return self._response(
                "I don't have any previous message yet.",
                "memory"
            )

        # ==========================================
        # MEMORY — LAST RESPONSE
        # ==========================================

        if (
            "what did you say" in text
            or "what was your last response" in text
        ):

            previous = (
                self.memory.last_assistant_message()
            )

            if previous:

                return self._response(
                    f"I said: {previous}",
                    "memory"
                )

            return self._response(
                "I haven't responded yet.",
                "memory"
            )

        # ==========================================
        # SCREEN VISION
        # ==========================================

        vision_phrases = [
            "what's on my screen",
            "what is on my screen",
            "what do you see on my screen",
            "look at my screen",
            "look at the screen",
            "read my screen",
            "read the screen",
            "analyze my screen",
            "analyze the screen"
        ]

        if any(
            phrase in text
            for phrase in vision_phrases
        ):

            try:

                image = self.screen.capture()

                response = self.vision.analyze(
                    image,
                    "Look at this screenshot and describe "
                    "what is visible on the screen. "
                    "Focus on useful details. "
                    "Keep the answer concise because it "
                    "will be spoken aloud."
                )

                return self._response(
                    response,
                    "vision"
                )

            except Exception as error:

                print(
                    "[VISION ERROR]",
                    error
                )

                return self._response(
                    "I'm having trouble seeing your screen right now.",
                    "vision"
                )

        # ==========================================
        # DESKTOP ACTIONS
        # ==========================================

        action_words = (
            "open ",
            "launch ",
            "start ",
            "run "
        )

        if text.startswith(action_words):

            response = self.commands.execute(
                text
            )

            return self._response(
                response,
                "action"
            )

        # ==========================================
        # DIRECT COMMANDS
        # ==========================================

        if (
            "youtube" in text
            or "calculator" in text
            or "notepad" in text
            or "github" in text
            or "gmail" in text
            or "google" in text
            or "vs code" in text
            or "file explorer" in text
        ):

            response = self.commands.execute(
                text
            )

            return self._response(
                response,
                "action"
            )

        # ==========================================
        # NATURAL CONVERSATION — LLM
        # ==========================================

        history = self.memory.recent(10)

        conversation = "\n".join(
            f"{item['role'].upper()}: {item['text']}"
            for item in history
        )

        prompt = f"""
You are Isha, a smart and friendly desktop AI assistant.

Your personality:
- Friendly
- Natural
- Calm
- Slightly witty
- Helpful
- Concise

Conversation rules:
- Understand the context of previous messages.
- Remember who or what the user is talking about.
- Understand words like "he", "she", "it", "that", "this", "there", etc.
- If the user asks a follow-up question, use previous conversation to understand it.
- Do not repeat information unnecessarily.
- Keep normal answers short because they will be spoken aloud.
- Do not claim to perform computer actions unless a tool actually performed them.
- Do not invent information about the user's computer.

        Recent conversation:
        {conversation}

        Current user message:
        {text}

        Respond naturally as Isha.
        """

        response = self.llm.ask(prompt)

        return self._response(
            response,
            "llm"
        )