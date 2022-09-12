import json
from drag_and_drop_camera_page import *
from utility_method import *
  
def ReadJson():
   launch_application()
   verify_signin_page_is_displayed()
   VIMonitorPlus = Aliases.VIMonitorPlus.HwndSource_MainWindow
   loginWindow = VIMonitorPlus.LoginWindow
   aqObject.CheckProperty(loginWindow.txtUserName, "IsVisible", cmpEqual, True)
   loginWindow.txtUserName.Clear()
   username = ReadDataFromJson("logincredentails","username")
   loginWindow.txtUserName.SetText(username)
   aqObject.CheckProperty(loginWindow.txtPassword, "IsVisible", cmpEqual, True)
   loginWindow.txtPassword.Clear()
   password = ReadDataFromJson("logincredentails","password")
   loginWindow.txtPassword.SetText(password)
   VIMonitorPlus.LoginWindow.btnLogIn.ClickButton()
   #close_application()

   