import pyautogui
import time

text = "gheu gheu!"
time_limit = 10

while time_limit:
    time_limit -= 1
    time.sleep(1)
    pyautogui.typewrite(text)
    pyautogui.press('enter')
    print(text)