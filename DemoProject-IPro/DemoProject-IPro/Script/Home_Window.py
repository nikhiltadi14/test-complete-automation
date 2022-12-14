def verifyThatSpecifiedUserIsLoggedInCorrectly(username):
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  aqObject.CheckProperty(mainWindow.WindowCommands.TextblockAdministrator, "WPFControlText", cmpEqual, username)

def waitForCamerasToLoadInLeftTreeView():
  treeView = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.treeServers
  treeViewItem = treeView.TreeviewitemDemoipCom
  aqObject.CheckProperty(treeViewItem.TextblockDemoipCom, "WPFControlText", cmpEqual, "demoip.com")
  treeViewItem.WaitWPFObject("TreeViewItem", "",1 ,80000)
  
def navigateToSetupAndConfigurationPopup():
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  mainWindow.mnuMain.WPFMenu.Click("Administration|Users & Groups|Setup and Configuration")
  
def logOutOfTheApplication():
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  button = mainWindow.WindowCommands.UserPB
  button.ClickButton()
  button.PopupMenu.Click("Log Out")
  
def verifyThatSpecifiedCamerasAreDisplayed():
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  expander = mainWindow.expCameras
  expander.Expand()
  treeView = expander.treeCameras
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.expCameras.treeCameras.TreeviewitemParkingCameraH265, "WPFControlText", cmpEqual, "Parking Camera (H.265)")
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.expCameras.treeCameras.TreeviewitemWvS4176H265, "WPFControlText", cmpEqual, "WV-S4176(H.265)")

def verifyThatLiveAndRecordOptionIsDisplayedForParkingCamera():
  treeView = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.expCameras.treeCameras
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  treeView.ClickItem("|[0]")
  tabControl = mainWindow.tabWorkspaces
  button = tabControl.playbackModeButton
  button.ClickButton()
  aqObject.CheckProperty(tabControl.btnExportVideoClip, "Exists", cmpEqual, True)
  tabControl.btnSwitchToLive.ClickButton()
  
def verifyThatRecordedViewIsNotDisplayedForSecondCamera():
  treeView = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.expCameras.treeCameras
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  treeView.ClickItem("|[1]")
  tabControl = mainWindow.tabWorkspaces
  button = tabControl.playbackModeButton
  button.ClickButton()
  messageBoxVI = Aliases.VIMonitorPlus.MessageBoxVI
  aqObject.CheckProperty(messageBoxVI.zMonitorStationEx_UltraFormManager_Dock_Area_Top, "Exists", cmpEqual, True)
  panel = messageBoxVI.VIMessageBox_Fill_Panel.UltraPanelClientAreaUnsafe.pnlTop
  aqObject.CheckProperty(panel.lblMessage, "Text", cmpEqual, "You do not have permission to view recorded video for one or more of the selected cameras.")
  panel.TableLayoutPanel1.btnOk.ClickButton()
  
def verifyThatSelectedViewIsDisplayedCorrectly():
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  expander2 = mainWindow.expLayouts
  expander2.Expand()
  treeView = expander2.treeLayouts
  aqObject.CheckProperty(treeView.TreeviewitemPocView1.TextblockPocView1, "WPFControlText", cmpEqual, "POC_View1")
  treeView.ClickItem("|[0]")
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.TabitemPocView1, "WPFControlText", cmpEqual, "POC_View1")
  
def verifyThatSelectedMapIsDisplayedCorrectly():
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  expander = mainWindow.expMaps
  expander.Expand()
  treeView2 = expander.treeMaps
  aqObject.CheckProperty(treeView2.TreeviewitemPocMap1.TextblockPocMap1, "WPFControlText", cmpEqual, "POC_Map1")
  treeView2.ClickItem("|[0]")
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.TabitemPocMap1, "WPFControlText", cmpEqual, "POC_Map1")