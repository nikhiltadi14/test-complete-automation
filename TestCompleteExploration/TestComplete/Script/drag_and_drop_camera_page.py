def launch_application():
  if Sys.waitProcess("VIMonitorPlus", 5000).Exists:
     Sys.waitProcess("VIMonitorPlus", 5000).Terminate()
     TestedApps.VIMonitorPlus.Run(1, True)

  else:
      Log.Message('Launching Application')
      TestedApps.VIMonitorPlus.Run(1, True)
  
def verify_signin_page_is_displayed():
  VIMonitorPlus = Aliases.VIMonitorPlus.HwndSource_MainWindow
  loginWindow = VIMonitorPlus.LoginWindow
  loginWindow.WaitWPFObject("VIMonitorPlus.LoginWindow","",10000)
  aqObject.CheckProperty(loginWindow.btnLogIn, "WPFControlText", cmpEqual, "Log In")
  
def login_into_application(username,password):
  VIMonitorPlus = Aliases.VIMonitorPlus.HwndSource_MainWindow
  loginWindow = VIMonitorPlus.LoginWindow
  aqObject.CheckProperty(loginWindow.txtUserName, "IsVisible", cmpEqual, True)
  loginWindow.txtUserName.Clear()
  loginWindow.txtUserName.SetText(username)
  aqObject.CheckProperty(loginWindow.txtPassword, "IsVisible", cmpEqual, True)
  loginWindow.txtPassword.Clear()
  loginWindow.txtPassword.SetText(password)
  VIMonitorPlus.LoginWindow.btnLogIn.ClickButton()

def verify_user_successfully_logged_into_account():  
  hwndsource = Aliases.VIMonitorPlus.HwndSource_MainWindow
  hwndsource.WaitWPFObject("HwndSource", "VI MonitorPlus", 6000)
  aqObject.CheckProperty(hwndsource.MainWindow, "WPFControlText", cmpEqual, "VI MonitorPlus")
    
def wait_for_the_cameras_to_load():
  MainWindow = Aliases.VIMonitorPlus2.HwndSource_MainWindow.MainWindow
  treeViewItem = MainWindow.treeServers.TreeviewitemDemoipCom
  aqObject.CheckProperty(treeViewItem.TextblockDemoipCom, "WPFControlText", cmpEqual, "demoip.com")
  treeViewItem.WaitWPFObject("TreeViewItem", "",1 ,80000)
  
def verify_2_camera_panel_is_displayed():
  Mainwindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces
  aqObject.CheckProperty(Mainwindow.Button2, "IsVisible", cmpEqual, True)
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.Textblock2Cameras, "WPFControlText", cmpEqual, "2 Cameras")
     
def click_on_2_camera_panel():
  MainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces
  MainWindow.Button2.ClickButton()
  
def verify_2_camera_panel_is_blank():
  hwndSource = Aliases.VIMonitorPlus.HwndSource_MainWindow
  videoContainerObj = hwndSource.WinFormsAdapter.VideoContainer
  varray = videoContainerObj.FindAll("WinFormsControlName","*pnlBackground_EmptyServerList*",2,True)
  if aqObject.CompareProperty(len(varray),cmpEqual, 0, True):
    Log.Checkpoint("2 Panels are blank")
  else:
    Log.Warning("Panels are not blank, please check")
  Log.Message(len(varray), "", 0)

def drag_and_drop_camera():
  hwndSource = Aliases.VIMonitorPlus2.HwndSource_MainWindow
  treeViewItem = hwndSource.MainWindow.treeServers.TreeviewitemDemoipCom
  treeViewItem.TreeviewitemParkingCameraH265.Drag(133, 12, 409, 33)
  videoContainer = hwndSource.WinFormsAdapter.VideoContainer
  #aqObject.CheckProperty(videoContainer.pnlBackground_6950726765843833856_0_4890587338688359686, "ClrFullClassName", cmpEqual, "System.Windows.Forms.Panel")
  treeViewItem.TreeviewitemTrainCameraH264.Drag(156, 19, 1119, 97)
  #.CheckProperty(videoContainer.pnlBackground_6950726765843833856_0_5013642087305423551.lblDisplayCtrl_6950726765843833856_406392038_5013642087305423551, "ClrFullClassName", cmpEqual, "System.Windows.Forms.Label")

def verify_videos_are_streaming_live():
  hwndSource = Aliases.VIMonitorPlus2.HwndSource_MainWindow
  videoContainerObj = hwndSource.WinFormsAdapter.VideoContainer
  varray = videoContainerObj.FindAll("WinFormsControlName","*lblDisplayCtrl*",2,True)
  Log.Message(len(varray))
  if aqObject.CompareProperty(len(varray),cmpEqual, 2, True):
    Log.Checkpoint("All 2 live videos are displayed correctly")
  else:
    Log.Warning("Some live videos are not loading, please check")
  Log.Message(len(varray), "", 0)
  
def logout_from_application():
  hwndSource = Aliases.VIMonitorPlus.HwndSource_MainWindow
  mainWindow = hwndSource.MainWindow
  button = mainWindow.WindowCommands.WindowCommandsItem.UserPB
  button.ClickButton()
  button.PopupMenu.Click("Log Out")

def close_application():
  TestedApps.VIMonitorPlus.Close()

  