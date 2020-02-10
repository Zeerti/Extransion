import pyautogui
import time
import eel
import errorHandler
import assembly
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
def main():
    # add functions here
    # order(3000) # orders salads X times
    # orderHotDog.orderHotDogs(300)
    eel.init('web')
    eel.start('index.html', mode='edge', size=(1024, 768), position=(0,0))

if __name__ == '__main__':
    # pyautogui.alert('Ensure Brink is at the main menu where the salad button is visible!')
    start_time = time.time() #getting what the current time is, and saving variable
    main()
    #current time -prev time
   # to show what the total time was when the program finishes

# num = guiInput.seperated()

# for i in num:
#     if i = 1:
#         clickNumber1()
#     if i = 2:
#         clickNumber2()
#     if i = 3:
#         clickNumber3()
#     if i = 4:
#         clickNumber4()
