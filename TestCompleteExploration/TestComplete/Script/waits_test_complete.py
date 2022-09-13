﻿from drag_and_drop_camera_page import *
from export_video_page import *
from utility_method import *
import random
import smtplib
from datetime import datetime, timedelta

def TestExportMultiplex():
  launch_application()
  
  # signin_page_is_displayed
  VIMonitorPlus = Aliases.VIMonitorPlus.HwndSource_MainWindow
  loginWindow = VIMonitorPlus.LoginWindow
  loginWindow.WaitWPFObject("VIMonitorPlus.LoginWindow","",10000)
  aqObject.CheckProperty(loginWindow.btnLogIn, "WPFControlText", cmpEqual, "Log In")
  
  
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
  
  ''''
  MainWindow = Aliases.VIMonitorPlus2.HwndSource_MainWindow.MainWindow
  treeViewItem = MainWindow.treeServers.TreeviewitemDemoipCom
  aqObject.CheckProperty(treeViewItem.TextblockDemoipCom, "WPFControlText", cmpEqual, "demoip.com")
  treeViewItem.WaitWPFObject("TreeViewItem", "",1 ,80000)
  '''
  close_application()