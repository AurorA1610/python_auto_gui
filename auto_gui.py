import pyautogui
import time
no_of_messages = 100
while no_of_messages > 0:
    time.sleep(4)
    pyautogui.typewrite("Hi. I love you. Bye.")
    time.sleep(2)
    pyautogui.press("enter")
    no_of_messages = no_of_messages - 1