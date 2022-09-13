﻿from drag_and_drop_camera_page import * 
  
def CheckPoints():
  launch_application()
  verify_signin_page_is_displayed()
  login_into_application(Project.Variables.Username,Project.Variables.Password)
  verify_user_successfully_logged_into_account()
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  Title = mainWindow.Title
  ''''
  aqObject.CheckProperty(mainWindow,"WPFControlText",cmpEqual,"VI MonitorPlus")
  aqObject.CompareProperty(Title,cmpEqual,"VI MonitorPlus")
  aqObject.CompareProperty(Title,cmpContains,"VI")
  aqObject.CompareProperty(Title,cmpStartsWith,"V") 
  '''
  
  if aqObject.CompareProperty(Title,cmpContains,"VI") == True:
     Log.Checkpoint("Title name matches with the contains string")
  else:
     Log.Error("Title name not matches with the contains string")
  
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow   
  property_value = aqObject.GetPropertyValue(mainWindow,"ChildCount")
  if aqObject.CompareProperty(property_value,cmpEqual,7) == True:
     Log.Checkpoint("Title name matches with the contains string")
  else:
     Log.Error("Title name not matches with the contains string")
     
     ''''
     
  if aqObject.CheckProperty(mainWindow,"ChildCount",cmpEqual,7) == True:
     Log.Checkpoint("Expected Childcount number matches with the Actual Childcount number ")
  else:
     Log.Error("Expected Childcount number not matches with the Actual Childcount number")
  
  if aqObject.CheckProperty(mainWindow,"IsVisible",cmpEqual,True) == True:
     Log.Checkpoint("Element is visible on sccreen ")
  else:
     Log.Error("Element is not visible on sccreen ")
     
  hwndsource = Aliases.VIMonitorPlus.HwndSource_MainWindow
  hwndsource.WaitWPFObject("MainWindow", "", 6000)
  if hwndsource.MainWindow.Exists == True:
     Log.Checkpoint("Element found")
  else:
     Log.Error("Element not found")
     '''