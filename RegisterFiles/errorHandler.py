import pyautogui
from pyautogui import alert, confirm, prompt
import eel

@eel.expose
def showPopup(type, title, text):
    if(type == 'alert'):
        alert(text=text, title=title)
    if(type == 'confirm'):
        confirmed = confirm(text=text, title=title, buttons=['OK', 'Cancel'])
        return confirmed
    if(type == 'prompt'):
        confirmed = confirm(text=text, title=title)
