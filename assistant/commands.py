from assistant.automation import Automation


class CommandHandler:

    def __init__(self):
        self.automation = Automation()

    def execute(self, command):

        command = command.lower().strip()

        # -----------------------------
        # YouTube Search
        # -----------------------------

        if (
            "search youtube for " in command
        ):
            query = command.split(
                "search youtube for ",
                1
            )[1]

            if self.automation.search_youtube(query):
                return f"Searching YouTube for {query}."

            return "What should I search for?"

        if (
            "search on youtube for " in command
        ):
            query = command.split(
                "search on youtube for ",
                1
            )[1]

            if self.automation.search_youtube(query):
                return f"Searching YouTube for {query}."

            return "What should I search for?"

        if (
            "search youtube " in command
        ):
            query = command.split(
                "search youtube ",
                1
            )[1]

            if self.automation.search_youtube(query):
                return f"Searching YouTube for {query}."

            return "What should I search for?"

        # -----------------------------
        # Google Search
        # -----------------------------

        if (
            "search google for " in command
        ):
            query = command.split(
                "search google for ",
                1
            )[1]

            if self.automation.search_google(query):
                return f"Searching Google for {query}."

            return "What should I search for?"

        # -----------------------------
        # Open Websites
        # -----------------------------

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

        # -----------------------------
        # Windows Apps
        # -----------------------------

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