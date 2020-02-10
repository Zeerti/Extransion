# Bump orders from Kitchen Display
# Click to keep kitchen in focus
# AND REPEAT AND REPEAT AND REPEAT AND REPEAT

import pyautogui
import eel

@eel.expose
def bump():
    while True:
        try:
            pyautogui.click(x=500, y=500) # Click anywhere to ensure Kitchen.exe is in Focus()
            pyautogui.press('1') # bump the order from the screen
        except TypeError:
            print("error dawg")