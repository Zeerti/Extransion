import pyautogui
import sys
import platform
import time
import eel
import errorHandler
import assembly
import kitchenBump


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

def main():
    try:
        print('Starting EEL GUI...')
        eel.init('web')
        eel.start('index.html', mode="chrome")
    except EnvironmentError:
        print("\n****************\nFailed auto-launching edge. Attemping to load default browswer\n****************\n\nPlease navigate to localhost:8000/index.html manually if it doesn't automatically open")
        # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
        if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
            eel.start('index.html', mode ="False")
        else:
            raise

if __name__ == '__main__':
    main()


