from drag_and_drop_camera_page import * 
  
def CheckPositiveNegitive():
  launch_application()
  verify_signin_page_is_displayed()
  login_into_application(Project.Variables.Username,Project.Variables.Password)
  verify_user_successfully_logged_into_account()
  administrator = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.mnuMain
  # Checking for Invisibility
  aqObject.CheckProperty(administrator.mnuAdministration,"IsVisible",cmpEqual,False)
  Log.Checkpoint("Checkpoint message",500)
  wait_for_the_cameras_to_load()
  # Checking for visibility
  aqObject.CheckProperty(administrator.mnuAdministration,"IsVisible",cmpEqual,True)
  main_window = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  main_window.WindowCommands.WindowCommandsItem.AlertPB.click()
  Aliases.VIMonitorPlus.HwndSource_PopupRoot2.PopupRoot.Button.click()
  #close_application()
  #aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_PopupRoot.PopupRoot,"VisibleOnScreen",cmpEqual,True)