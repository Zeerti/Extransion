import pyautogui
import time
import eel
from orderSalads import order
import orderHotDog
# Adds a pause between all actions
pyautogui.PAUSE = .1
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


# Only needs to be done once a day.
## Login (x4)
## 1187, 181
## Set drawer if needed
## 1610 56 -- manager
## 1592 350 -- Manage Drawers
## 800 100 -- CD1 - TO-GO
## 300 1400 -- Assign Drawer
## 1100 700 -- Name of person to assign to
## 1200 900 -- Set bank amount
## 2300 1400 -- Close drawer management
## 2400 50 -- Logout
## 1187 181(x4) -- Login
### click anywhere again once (Due to Busi-date not matching)

def main():
    # add functions here
    # order(3000) # orders salads X times
    # orderHotDog.orderHotDogs(300)
    eel.init('static_web_folder')
    eel.start('index.html', mode='edge')

if __name__ == '__main__':
    pyautogui.alert('Ensure Brink is at the main menu where the salad button is visible!')
    start_time = time.time() #getting what the current time is, and saving variable
    main()
    print("--- %s seconds to execute 3000 orders in main --- " % (time.time() - start_time)) 
    #current time -prev time
   # to show what the total time was when the program finishes

num = guiInput.seperated()

for i in num:
    if i = 1:
        clickNumber1()
    if i = 2:
        clickNumber2()
    if i = 3:
        clickNumber3()
    if i = 4:
        clickNumber4()
