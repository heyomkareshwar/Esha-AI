from assistant.commands import CommandHandler

handler = CommandHandler()

print(
    handler.execute(
        "search youtube for python tutorials"
    )
)