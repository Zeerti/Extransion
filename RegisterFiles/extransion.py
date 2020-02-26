import pyautogui
import time
import eel
import errorHandler
import assembly
import kitchenBump
import asyncio


# Adds a pause between all actions
# pyautogui.PAUSE = 1
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

#######################################
# Coords Based on 2560 x 1440 monitor #
#######################################

#15 - 45 seconds
#5 second to order
#smoketest-k91 TO K93
#smoketest-r01 -- R1
async def main():
    # add functions here
    # order(3000) # orders salads X times
    # orderHotDog.orderHotDogs(300)
    eel.init('web')
    eel.start('index.html', mode='edge', size=(1024, 768), position=(0,0), block=False)

    i = 0
    while True:
        i += 1
        eel.sleep(1)
        print(f"Updating status: {i}")

if __name__ == '__main__':
    # pyautogui.alert('Ensure Brink is at the main menu where the salad button is visible!')
    asyncio.run(main())
    #current time -prev time
   # to show what the total time was when the program finishes

