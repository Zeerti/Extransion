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
def order(orderIterations):
    try:
        for i in range(orderIterations):
            pyautogui.click(x=1000, y=400) # Click Salad button
            pyautogui.click(x=800, y=275) # Click top most salad in column
            for i in range(6): # Iterate through all the rest of the salads. Each button is 113 pixels apart. 
                pyautogui.move(0,113) # Move mouse down 113 pixels from current position to hit next button in column
                pyautogui.click() # Click
            pyautogui.click(x=2400, y=1300) # Pay / close order
            pyautogui.click(x=1600, y=400) # Exact Cash button
            # sleep(1) # 1 second sleep while punchh does its thing
            pyautogui.click(x=1600, y=400)
    except TypeError:
        print('Oops! That was an invalid number for the "orderSalads" function. Please try again.')