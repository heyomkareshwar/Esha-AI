from assistant.brain import IshaBrain


brain = IshaBrain()

tests = [
    "who is Elon Musk",
    "what company does he own",
    "tell me more about it",
]

for command in tests:

    print("\n" + "=" * 50)

    print("You:", command)

    result = brain.think(command)

    print("Type:", result["type"])
    print("Isha:", result["response"])