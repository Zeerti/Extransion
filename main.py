import pyautogui
# Adds a .5s pause to all actions
pyautogui.PAUSE = .25
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

# Repeat ad nauseam 
# 1000 400 -- Salad button
# 800 275 -- Baja 
# Press down the row, increase Y by 113 each iteration (x6)
# 2400 1300 -- PAY / CLOSE ORDER
# 1600 400 -- Exact Cash Button
# Need to add a delay due to "contacting punch"
# Click anywhere again once (Change Due message)
# AND REPEAT AND REPEAT AND REPEAT AND REPEAT

pyautogui.click(x=1000, y=400, button='left')

for i in range(6)
    pyautogui.move(0,50)
    pyautogui.click()
