# 729 742 -- clock in
# 746 614 -- manager functions
# 517 260 -- manage drawers 
# See below on column details for how to click what
################################
# 103 728 -- assign button
# 365 330 -- select employee
# 440 565 -- starting bank
# 916 728 -- done
# 377 22 -- menu button


#################################
# Column details
#################################
# There are 4 columns and 10 rows

# 150 80 -- Column 1 and Row 1
# 390 85 -- Column 2
# 629 85 -- Column 3
# 866 85 -- Column 4

# Row 2 -- 162 

# Button Width -- 210
# Button Height -- 45

# without scrolling you can get to CD 36
# 2 mouse wheel clicks 
# 150, 650

# Assign cash drawer
# Login > Clock in > Manager Functions > Assign drawer > Go to Menu

import pyautogui
import calculateCDPosition

def cashDrawerAssign():
    _reg = reg # new variable for register number

    pyautogui.click(812, 27) # Click Manager functions
    pyautogui.click(510, 178) # Click Manager drawers
            
    # Call to cash drawer grid
    _x, _y = calculateCoords(_reg) # returns coords for drawer click
    pyautogui.click(_x, _y) #click cash drawer grid

    pyautogui.click(87, 729) # Click Assign button
    pyautogui.click(381, 338) # Click top left available employee
    pyautogui.click(442, 572) # Click OK in Bank Amount
    pyautogui.click(932, 724) # Click Done in cash drawer assignments
    pyautogui.click(358, 101) # Select Menu for ordering

