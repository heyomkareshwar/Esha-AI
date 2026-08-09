import os
import subprocess
import webbrowser


class Automation:

    def open_youtube(self):
        webbrowser.open("https://www.youtube.com")

    def open_google(self):
        webbrowser.open("https://www.google.com")

    def open_github(self):
        webbrowser.open("https://github.com")

    def open_gmail(self):
        webbrowser.open("https://mail.google.com")

    def open_calculator(self):
        subprocess.Popen("calc.exe")

    def open_notepad(self):
        subprocess.Popen("notepad.exe")

    def open_file_explorer(self):
        subprocess.Popen("explorer.exe")

    def open_vscode(self):
        # Works if VS Code is available in PATH.
        try:
            subprocess.Popen("code")
        except FileNotFoundError:
            print("VS Code command not found.")