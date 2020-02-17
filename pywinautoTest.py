
from pywinauto.application import Application
from time import sleep
from pywinauto import timings

timings.Timings.defaults()
# app = Application(backend="uia").start(r"C:\Brink\Pos\Register.exe")
app = Application(backend="uia").connect(title="Register")
# Register apps
#app.RegisterDialog, app.Register, app.Dialog

dlg = app.RegisterDialog
dlg2 = app.Register
dlg3 = app.Dialog

actionable_dlg = dlg.wait('visible')
# dlg.print_control_identifiers(3)
loginScreen = app.RegisterDialog.child_window(auto_id="_loginScreen")
# loginGrid = loginScreen.child_window(auto_id="Button1")

# loginScreen.print_control_identifiers(2)
loginBtn1 = loginScreen.child_window(title="1", control_type="Button")
loginBtn2 = loginScreen.child_window(title="2", control_type="Button")
loginBtn3 = loginScreen.child_window(title="3", control_type="Button")
loginBtn4 = loginScreen.child_window(title="4", control_type="Button")
loginBtn5 = loginScreen.child_window(title="5", control_type="Button")
loginBtn6 = loginScreen.child_window(title="6", control_type="Button")
loginBtn7 = loginScreen.child_window(title="7", control_type="Button")
loginBtn8 = loginScreen.child_window(title="8", control_type="Button")
loginBtn9 = loginScreen.child_window(title="9", control_type="Button")
loginBtn0 = loginScreen.child_window(title="0", control_type="Button")

loginBtn1.click()
loginBtn0.click()
loginBtn0.click()
loginBtn1.click()

app.RegisterDialog['No OrdersCustom1'].print_control_identifiers(4)
    # ['Custom77', 'No OrdersCustom', 'No OrdersCustom0', 'No OrdersCustom1']
# app.RegisterDialog.Custom84.print_control_identifiers(3)
    # ['Custom84', 'Monday, February 17, 2020 11:19:20 AMCustom']

# auto_id="listBoxJobs"


# loginScreen['1Button'].click()
# loginScreen['1Button'].click()

# app.RegisterDialog.child_window(auto_id="_loginScreen").Button1.click()
# app.RegisterDialog.child_window(auto_id="_loginScreen").Button10.click()
# app.RegisterDialog.child_window(auto_id="_loginScreen").Button10.click()
# app.RegisterDialog.child_window(auto_id="_loginScreen").Button1.click()


#with open("Output.txt", "w") as text_file:
    #print(f"DIALOG: {app.RegisterDialog.print_control_identifiers(2)}", file=text_file)
