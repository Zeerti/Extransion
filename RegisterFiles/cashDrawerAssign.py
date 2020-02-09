# Assign cash drawer
# Login > Clock in > Manager Functions > Assign drawer > Go to Menu

import pyautogui
import calculateCDPosition

def cashDrawerAssign(reg):
    _reg = reg # new variable for register number

    pyautogui.click(751, 612) # Click Manager functions
    pyautogui.click(515, 257) # Click Manager drawers
            
    # Call to cash drawer grid
    _x, _y = calculateCoords(_reg) # returns coords for drawer click
    pyautogui.click(_x, _y) #click cash drawer grid

    pyautogui.click(95, 724) # Click Assign button
    pyautogui.click(368, 334) # Click top left available employee
    pyautogui.click(444, 570) # Click OK in Bank Amount
    pyautogui.click(915, 728) # Click Done in cash drawer assignments
    pyautogui.click(377, 25) # Select Menu for ordering