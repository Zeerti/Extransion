# Cash orders out and begin again!

import pyautogui

def cashOut():
    pyautogui.click(664, 646) # Exact cash
    pyautogui.click(768, 577) # Click OK button on Change Due screen
        
# repeats order iteration