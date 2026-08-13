from assistant.brain import IshaBrain


brain = IshaBrain()

tests = [
    "hello",
    "who are you",
    "what can you do",
    "open youtube",
    "open calculator",
    "do something random",
]


for command in tests:

    print("\nYou:", command)

    result = brain.think(command)

    print("Type:", result["type"])
    print("Isha:", result["response"])