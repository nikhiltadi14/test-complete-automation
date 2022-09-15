from drag_and_drop_camera_page import *
from export_video_page import *
from utility_method import *

def TestExportMultiplex():
  launch_application()
  verify_signin_page_is_displayed()
  login_into_application(Project.Variables.Username,Project.Variables.Password)
  
  #successfully_logged_into_account 
  hwndsource = Aliases.VIMonitorPlus.HwndSource_MainWindow
  #hwndsource.WaitWPFObject("HwndSource", "VI MonitorPlus", 6000)
  
  if (hwndsource.WaitProperty("WndCaption", "VI MonitorPlus", 6000)):
    Log.Checkpoint("Property is present")
  else:
    Log.Error("The OK button didn't become enabled within 15 seconds.")
    
  aqObject.CheckProperty(hwndsource.MainWindow, "WPFControlText", cmpEqual, "VI MonitorPlus")
  
  #Check object state
  if (hwndsource.visible):
    Log.Checkpoint("Visible on screen")
  else:
    Log.Error("The Notepad window is invisible")
    
  Log.Message(hwndsource.visible)
  
  if(hwndsource.WaitChild("MainWindow", 5000) == True):
     if(hwndsource.MainWindow.VisibleOnScreen):
         Log.Message('Working')
  else: 
     Log.Warning('Not Working')
  
  VIMonitorPlus = Aliases.VIMonitorPlus
  menu = VIMonitorPlus.HwndSource_MainWindow.MainWindow
    
  if (menu.WaitAliasChild("mnuMain", 10000).Visible): 
    Log.Message("The Font window has appeared")
  else:
    Log.Error("The Font window has not appeared.")
  
  ''''
  security_setup = Aliases.VIMonitorPlus.HwndSource_SecuritySetup
  if (security_setup.WaitAliasChild("SecuritySetup", 10000).Visible): 
    Log.Message("The Font window has appeared")
  else:
    Log.Error("The Font window has not appeared.")
    '''
  wait_until_object_is_visible(menu,"mnuMain",10000)
    
  close_application()