import pyautogui
import time

while True:
    time.sleep(3)
    pyautogui.typewrite('I Love You Sona.')
    pyautogui.press('enter')
    print('I Love You Sona.')