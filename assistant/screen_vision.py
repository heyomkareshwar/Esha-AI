import pyautogui


class ScreenVision:

    def capture(self):
        """Capture the current screen."""
        return pyautogui.screenshot()

    def save(self, path="screen_test.png"):
        """Capture and save the current screen."""
        screenshot = self.capture()
        screenshot.save(path)
        return path