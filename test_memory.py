from assistant.brain import IshaBrain


brain = IshaBrain()

print(brain.think("hello"))
print(brain.think("who are you"))

print("\nMemory:")
for item in brain.memory.recent():
    print(item)