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
    
    # Order hot dogs and cash out orders until iterations complete
    for i in range(_iterations):
        order(2)
        cashOut()

