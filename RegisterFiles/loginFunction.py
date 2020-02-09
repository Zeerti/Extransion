# Function to set the login number on POS
# Store input in list
# Input will be from GUI
# Input translated to login button map
# Button coordinates triggered with PyAutoGui.click

## --reserved for later use--
# length = len(userLogin) # get total length of array to set list() dynamically

# login commands from GUI
def loginFunction(pin): 
    # initializing login string from user
    loginString = pin

    userLogin = [] # store login numbers from user in array
    for i in loginString:
        userLogin.append(i)

    # Numbers input by user mapped to coordinates on login screen
    for i in userLogin: 
        _value = int(i)
        if(_value == 1):
            pyautogui.click(417, 184) # Click 1 on screen
        if(_value == 2):
            pyautogui.click(507, 176) # Click 2 on screen
        if(_value == 3):
            pyautogui.click(595, 176) # Click 3 on screen
        if(_value == 4):
            pyautogui.click(413, 216) # Click 4 on screen
        if(_value == 5):
            pyautogui.click(504, 248) # Click 5 on screen
        if(_value == 6):
            pyautogui.click(593, 244) # Click 6 on screen
        if(_value == 7):
            pyautogui.click(416, 313) # Click 7 on screen
        if(_value == 8):
            pyautogui.click(506, 317) # Click 8 on screen
        if(_value == 9):
            pyautogui.click(594, 315) # Click 9 on screen
        if(_value == 0):
            pyautogui.click(417, 384) # Click 0 on screen

    ## Button maps for 1024 * 768 Register 
    # 417 184 -- 1
    # 507 176 -- 2
    # 595 176 -- 3
    # 413 216 -- 4
    # 504 248 -- 5
    # 593 244 -- 6
    # 416 313 -- 7
    # 506 317 -- 8
    # 594 315 -- 9
    # 417 384 -- 0