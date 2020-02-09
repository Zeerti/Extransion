# Clock In
# Login > Clock In

# this should execute once after the initial login

def clockIn():
        while True:
        try:
            pyautogui.click(727, 739) # Click clockin

        except TypeError:
            pyautogui.alert('Invalid operation!')

# After clocking in, go to cash drawer assignment