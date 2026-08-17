from assistant.llm_brain import LLMBrain


brain = LLMBrain()

response = brain.ask(
    "You are Isha, a helpful desktop AI assistant. "
    "Answer briefly and naturally. "
    "User: What is recursion?"
)

print("\nIsha:")
print(response)