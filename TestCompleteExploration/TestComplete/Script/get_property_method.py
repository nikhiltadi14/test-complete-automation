﻿from drag_and_drop_camera_page import * 
import re
  
def Main():
  launch_application()
  verify_signin_page_is_displayed()
  login_into_application(Project.Variables.Username,Project.Variables.Password)
  verify_user_successfully_logged_into_account()
  #wait_for_the_cameras_to_load()
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  property_value = aqObject.GetPropertyValue(mainWindow,"WPFControlText")
  Log.Message(property_value)
  propert_value_visible = aqObject.GetPropertyValue(mainWindow,'Visible')
  Log.Message(propert_value_visible)
  ''''
  Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.Camera4.click()
  video_container = Aliases.VIMonitorPlus.HwndSource_MainWindow.WinFormsAdapter.VideoContainer
  property_value_video_container = aqObject.GetPropertyValue(video_container,"WinFormsControlName")
  Log.Message(property_value_video_container)
  property_value_visible = aqObject.GetPropertyValue(video_container,"visible")
  Log.Message(property_value_visible)
  Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.WPFObject("LoginCanvas").WPFObject("lblVersion")
  close_application()
  '''