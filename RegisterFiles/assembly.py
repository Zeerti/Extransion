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
import orderHotDog

def assembly(login, reg, iterations):
    _login = login # temp val for user login
    _reg = reg      # temp val for register number
    _iterations = iterations    # temp val for orders
    
    # Function calls with temp val
    loginFunction(_login)
    clockInFunction()
    cashDrawerAssign(_reg)
    order(2)
    cashOut()

