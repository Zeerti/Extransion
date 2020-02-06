import pyautogui
import time
from orderSalads import order
# Adds a pause between all actions
pyautogui.PAUSE = .03
# Moving mouse to upper-left will abort program when true
pyautogui.FAILSAFE = True

# Function continually prints out the current mouse X,Y coords for quick prototyping
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionString = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionString, end='')
#         print('\b' * len(positionString), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

# Click anywhere on the monitor
# press the "b" key
# wait 1 second
# press the "b" key

def kitchenMain():
    # add functions here
    bump(3500) # bumps orders

if __name__ == '__main__':
    pyautogui.alert('Ensure Kitchen is running and in focus()!')
    start_time = time.time() #getting what the current time is, and saving variable
    kitchenMain()
    print("--- %s seconds to execute 3000 orders in main --- " % (time.time() - start_time)) 
    #current time -prev time
    # to show what the total time was when the program finishes
