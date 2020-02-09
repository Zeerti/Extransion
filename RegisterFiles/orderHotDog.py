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
from random import randrange
from time import sleep

# Callback function that executes X times
def order(numberOfOrders):
    _clicks = 0

    while(_clicks < int(numberOfOrders)):
        # Uncomment this section to make random ordering. comment out other instance.
        randoNumber = randrange(3) + 1

        if(randoNumber == 1):
            pyautogui.click(x=359, y=110) # order hotdog
        if(randoNumber == 2):
            pyautogui.click(x=355, y=192) # order chili dog
        if(randoNumber == 3):
            pyautogui.click(x=453, y=106) # order cheese dog
        if(randoNumber == 4):
            pyautogui.click(x=452, y=192) # order chili cheese dog
        _clicks = _clicks + 1
        # print("Ordered 2 hotdawgs") - for testing purposes


def orderHotDogs(iterations):
    try:
        for i in range(iterations):
            order(2) # Order X random things that are hotdogs
            pyautogui.click(x=663, y=647) #Exact Cash button
            pyautogui.click(x=764, y=581, clicks=2, interval=.25) # Okay button / confirm change
    except TypeError:
        print('General Error')

