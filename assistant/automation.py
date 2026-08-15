import subprocess
import webbrowser
from urllib.parse import quote_plus


class Automation:

    def open_youtube(self):
        webbrowser.open(
            "https://www.youtube.com"
        )

    def search_youtube(self, query):
        query = query.strip()

        if not query:
            return False

        url = (
            "https://www.youtube.com/results?search_query="
            + quote_plus(query)
        )

        webbrowser.open(url)

        return True

    def open_google(self):
        webbrowser.open(
            "https://www.google.com"
        )

    def search_google(self, query):
        query = query.strip()

        if not query:
            return False

        url = (
            "https://www.google.com/search?q="
            + quote_plus(query)
        )

        webbrowser.open(url)

        return True

    def open_github(self):
        webbrowser.open(
            "https://github.com"
        )

    def open_gmail(self):
        webbrowser.open(
            "https://mail.google.com"
        )

    def open_calculator(self):
        subprocess.Popen("calc.exe")

    def open_notepad(self):
        subprocess.Popen("notepad.exe")

    def open_file_explorer(self):
        subprocess.Popen("explorer.exe")

    def open_vscode(self):
        try:
            subprocess.Popen("code")
        except FileNotFoundError:
            print("VS Code command not found.")