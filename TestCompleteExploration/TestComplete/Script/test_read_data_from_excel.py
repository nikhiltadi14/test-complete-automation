from drag_and_drop_camera_page import *
from utility_method import *
  
def ReadDataFromExcel():
   launch_application()
   count = excel_filled_row_value_count()
   list_elements = read_data_from_excel(count)
   verify_signin_page_is_displayed()
   VIMonitorPlus = Aliases.VIMonitorPlus.HwndSource_MainWindow
   loginWindow = VIMonitorPlus.LoginWindow
   aqObject.CheckProperty(loginWindow.txtUserName, "IsVisible", cmpEqual, True)
   loginWindow.txtUserName.Clear()
   loginWindow.txtUserName.SetText(list_elements[0])
   aqObject.CheckProperty(loginWindow.txtPassword, "IsVisible", cmpEqual, True)
   loginWindow.txtPassword.Clear()
   loginWindow.txtPassword.SetText(list_elements[1])
   VIMonitorPlus.LoginWindow.btnLogIn.ClickButton()

  
  