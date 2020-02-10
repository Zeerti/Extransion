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
from time import sleep

@eel.expose
def assembly(login, reg, iterations, delay):
    _login = login # temp val for user login
    _reg = reg      # temp val for register number
    _iterations = int(iterations)    # temp val for orders
    pyautogui.PAUSE = float(delay)
    # Function calls with temp val
    loginFunction.loginFunction(_login)
    clockInFunction.clockIn()
    cashDrawerAssign.cashDrawerAssign(_reg)
    
    # Order hot dogs and cash out orders until iterations complete
    for i in range(_iterations):
        rand = randrange(15, 45) #Set the random range to delay next order.
        sleep(rand)
        orderHotDog.order(2)
        cashOutFunction.cashOut()


