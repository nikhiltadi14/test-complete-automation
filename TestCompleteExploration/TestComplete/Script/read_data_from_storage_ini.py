from drag_and_drop_camera_page import *
from utility_method import *

def StorageIni():
   launch_application()
   verify_signin_page_is_displayed()
   VIMonitorPlus = Aliases.VIMonitorPlus.HwndSource_MainWindow
   loginWindow = VIMonitorPlus.LoginWindow
   aqObject.CheckProperty(loginWindow.txtUserName, "IsVisible", cmpEqual, True)
   loginWindow.txtUserName.Clear()
   username = ReadDataFromINIFIle("Credentials","Username")
   Log.Message(username)
   loginWindow.txtUserName.SetText(username)
   aqObject.CheckProperty(loginWindow.txtPassword, "IsVisible", cmpEqual, True)
   loginWindow.txtPassword.Clear()
   password = ReadDataFromINIFIle("Credentials","Password")
   Log.Message(password)
   loginWindow.txtPassword.SetText(password)
   VIMonitorPlus.LoginWindow.btnLogIn.ClickButton()
   AddDataIntoINIFile("Hi","Username1","Vikas Reddy")