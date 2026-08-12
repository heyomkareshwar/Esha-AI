from enum import Enum


class AssistantState(Enum):
    IDLE = "idle"
    WAKE = "wake"
    LISTENING = "listening"
    THINKING = "thinking"
    SPEAKING = "speaking"