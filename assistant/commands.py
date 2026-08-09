from assistant.automation import Automation


class CommandHandler:

    def __init__(self):
        self.automation = Automation()

    def execute(self, command):

        command = command.lower().strip()

        if "open youtube" in command:
            self.automation.open_youtube()
            return "Opening YouTube."

        if "open google" in command:
            self.automation.open_google()
            return "Opening Google."

        if "open github" in command:
            self.automation.open_github()
            return "Opening GitHub."

        if "open gmail" in command:
            self.automation.open_gmail()
            return "Opening Gmail."

        if "open calculator" in command:
            self.automation.open_calculator()
            return "Opening calculator."

        if "open notepad" in command:
            self.automation.open_notepad()
            return "Opening Notepad."

        if "open file explorer" in command:
            self.automation.open_file_explorer()
            return "Opening File Explorer."

        if "open vs code" in command:
            self.automation.open_vscode()
            return "Opening VS Code."

        return "I don't know that command yet."