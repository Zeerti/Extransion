 # ----Assembly----
 # Execute functions in correct order
 # Login
 # Clock In
 # Assign Cash Drawer
 # Go to order screen/menu
 # Start Ordering

import loginFunction
import clockInFunction
import cashDrawerAssign
import cashOutFunction
import orderHotDog
import eel
import pyautogui
from random import randrange
from time import sleep, time

@eel.expose
def assembly(login, reg, iterations, delay, skipClockin):
    startTime = time()
    _login = login # temp val for user login
    _reg = reg      # temp val for register number
    _iterations = int(iterations)    # temp val for orders
    pyautogui.PAUSE = float(delay)
    
    if(skipClockin == True):
        print(f"Skipping ClockingIn and Drawer Assignment")
        loginFunction.loginFunction(_login)
        pyautogui.click(751, 612) # Click Manager functions
        pyautogui.click(377, 25) # Select Menu for ordering
    else:
        loginFunction.loginFunction(_login)
        clockInFunction.clockIn()
        cashDrawerAssign.cashDrawerAssign(_reg)    
    
    
    # Order hot dogs and cash out orders until iterations complete
    for i in range(_iterations):
        rand = randrange(15, 45) #Set the random range to delay next order.
        print(f"Sleeping {rand} seconds before ordering again ZzZzZz...")
        sleep(rand)
        orderHotDog.order(2)
        cashOutFunction.cashOut()
        print(f"Completed order {i} of {_iterations}")
    print(f"Completed {_iterations} orders in {time() - startTime} seconds")
    pyautogui.alert(text=f"Completed {_iterations} orders in {int(time() - startTime)} seconds", title="COMPLETED TEST", button="OK")
    


