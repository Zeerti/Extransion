# Repeat ad nauseam 
# 1000 400 -- Salad button
# 800 275 -- Baja 
# Press down the row, increase Y by 113 each iteration (x6)
# 2400 1300 -- PAY / CLOSE ORDER
# 1600 400 -- Exact Cash Button
# Need to add a delay due to "contacting punch"
# Click anywhere again once (Change Due message)
# AND REPEAT AND REPEAT AND REPEAT AND REPEAT
##########################################################################################

import pyautogui
from time import sleep
# Click salad section,
# order each salad in first column,
# close order
# Function assumes you are at the main menu where the Green salad button is displayed
def bump(orderIterations):
    while True:
        try:
            pyautogui.click(x=500, y=500) # Click anywhere to ensure Kitchen.exe is in Focus()
            pyautogui.press(b) # bump the order from the screen

        except TypeError:
            pyautogui.alert('Invalid operation!')