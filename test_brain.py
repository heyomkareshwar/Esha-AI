from assistant.brain import IshaBrain


brain = IshaBrain()


tests = [
    "hello",
    "who are you",
    "what can you do",

    # Desktop actions
    "open youtube",
    "open calculator",

    # LLM tests
    "explain recursion in simple words",
    "what is artificial intelligence",
    "tell me a short joke",

    # Unknown / natural language
    "I'm feeling bored",
    "what can I learn today",
]


for command in tests:

    print("\n" + "=" * 50)

    print("You:", command)

    result = brain.think(command)

    print("Type:", result["type"])

    print("Isha:", result["response"])