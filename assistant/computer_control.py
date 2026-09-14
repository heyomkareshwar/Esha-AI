import pyautogui


class ComputerControl:

    def move_mouse(self, x, y):
        pyautogui.moveTo(x, y, duration=0.2)

    def click(self):
        pyautogui.click()

    def double_click(self):
        pyautogui.doubleClick()

    def right_click(self):
        pyautogui.rightClick()

    def type_text(self, text):
        pyautogui.write(
            text,
            interval=0.02
        )

    def press_key(self, key):
        pyautogui.press(key)

    def hotkey(self, *keys):
        pyautogui.hotkey(*keys)