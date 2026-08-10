from assistant.wake_word import WakeWordListener


listener = WakeWordListener()

listener.listen_for_wake_word()

print("Isha is awake!")