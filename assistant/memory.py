class Memory:

    def __init__(self, max_items=20):
        self.max_items = max_items
        self.history = []

    def add(self, role, text):
        self.history.append({
            "role": role,
            "text": text
        })

        if len(self.history) > self.max_items:
            self.history.pop(0)

    def recent(self, count=10):
        return self.history[-count:]

    def last_user_message(self):
        for item in reversed(self.history):
            if item["role"] == "user":
                return item["text"]

        return None

    def last_assistant_message(self):
        for item in reversed(self.history):
            if item["role"] == "assistant":
                return item["text"]

        return None

    def clear(self):
        self.history.clear()