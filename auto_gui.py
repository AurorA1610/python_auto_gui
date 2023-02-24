import pyautogui
import time
no_of_messages = 100
while no_of_messages > 0:
    time.sleep(4)
    pyautogui.typewrite("Hi. How are you?")
    time.sleep(2)
    pyautogui.press("enter")
    no_of_messages = no_of_messages - 1
