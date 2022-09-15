import random

def Test1():
  
  TestedApps.VIMonitorPlus.Run(1, True)
  Sys.WaitProcess("VIMonitorPlus",60000)
  
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_LoginWindow.LoginWindow.Image, "FullName", cmpEqual, 'Sys.Process(\"VIMonitorPlus\").WPFObject(\"HwndSource: LoginWindow\", \"VI MonitorPlus\").WPFObject(\"LoginWindow\", \"VI MonitorPlus\", 1).WPFObject(\"LoginCanvas\").WPFObject(\"LoginPanel\").WPFObject(\"StackPanel\", \"\", 1).WPFObject(\"Image\", \"\", 1)')
  VIMonitorPlus = Aliases.VIMonitorPlus
  hwndSource = VIMonitorPlus.HwndSource_LoginWindow
  loginWindow = hwndSource.LoginWindow   
  textBox = loginWindow.txtUserName
  textBox.SetText("Administrator")
  passwordBox = loginWindow.txtPassword
  passwordBox.SetText(Project.Variables.Password)
  loginWindow.cboLoginMode.ClickItem("Multiple Servers")
  dataGrid = loginWindow.gridConnections
  
  popupRoot = VIMonitorPlus.HwndSource_PopupRoot.PopupRoot
  if dataGrid.TextblockDemoipCom.Exists: 
    aqObject.CheckProperty(dataGrid.TextblockDemoipCom, "WPFControlText", cmpEqual, "demoip.com")
    dataGrid.ClickCellXY(0, "Server Name", 133, 16)  
  else:
    loginWindow.btnServerAdd.ClickButton()
    popupRoot.txtNewConnectionIPAddress.Click(47, 25)
    hwndSource.Keys("demoip.com")
    hwndSource.Keys("4021")
    popupRoot.btnTestConnectionServer.ClickButton()
    aqObject.CheckProperty(popupRoot.txtNewServerName, "wText", cmpEqual, "demoip.com")
    popupRoot.btnUpdateConnectionServer.ClickButton()  
  
  loginWindow.btnLogIn.ClickButton()
  hwndSource = VIMonitorPlus.HwndSource_MainWindow
  mainWindow = hwndSource.MainWindow
  mainWindow.WindowButtonCommands.Click()
  aqObject.CheckProperty(mainWindow.WindowCommands.TextblockAdministrator, "WPFControlText", cmpEqual, "Administrator")
  
  treeView = mainWindow.treeServers
  treeViewItem = treeView.TreeviewitemDemoipCom
  aqObject.CheckProperty(treeViewItem.TextblockDemoipCom, "WPFControlText", cmpEqual, "demoip.com")
  treeViewItem.WaitWPFObject("TreeViewItem", "",1 ,50000)
  
  mainWindow.mnuMain.WPFMenu.Click("Administration|Users & Groups|Setup and Configuration")
  securitySetup = VIMonitorPlus.HwndSource_SecuritySetup.SecuritySetup
  aqObject.CheckProperty(securitySetup, "WPFControlText", cmpEqual, "Security Setup")
  expander = securitySetup.expUsers
  aqObject.CheckProperty(expander, "WPFControlText", cmpEqual, "Users")
  aqObject.CheckProperty(securitySetup.TextblockSelectAUserGroupOrClickTheButton, "WPFControlText", cmpEqual, "Select a User/Group or click the + button.")
  expander.Click(261, 21)
  aqObject.CheckProperty(securitySetup.TextblockUserInformation, "WPFControlText", cmpEqual, "User Information")
  aqObject.CheckProperty(securitySetup.TextblockPermissions, "WPFControlText", cmpEqual, "Permissions")
  aqObject.CheckProperty(securitySetup.TextboxUserId, "wText", cmpMatches, "\z")
  sRand = str(random.randint(0,5000))
  textBox = securitySetup.txtUserName
  textBox.SetText("Vikas"+sRand)
  textBox2 = securitySetup.TextboxFullName
  textBox2.SetText("Vol"+sRand)
  textBox3 = securitySetup.TextboxEmail
  textBox3.SetText("v"+sRand+"@gmail.com")
  passwordBox = securitySetup.PasswordBox
  passwordBox.SetText(Project.Variables.Password)
  passwordBox2 = securitySetup.PasswordboxVerify
  passwordBox2.SetText(Project.Variables.Password)
  toggleButton = securitySetup.ToggleButton
  toggleButton.ClickButton(cbChecked)
  textBox4 = securitySetup.TextBox
  textBox4.SetText("5")
  aqObject.CheckProperty(textBox, "wText", cmpEqual, "Vikas"+sRand)
  aqObject.CheckProperty(textBox2, "wText", cmpEqual, "Vol"+sRand)
  aqObject.CheckProperty(textBox3, "wText", cmpEqual, "v"+sRand+"@gmail.com")
  aqObject.CheckProperty(passwordBox, "wText", cmpEqual, Project.Variables.Password.DecryptedValue)
  aqObject.CheckProperty(passwordBox2, "wText", cmpEqual, Project.Variables.Password.DecryptedValue)
  aqObject.CheckProperty(toggleButton, "wState", cmpEqual, 1)
  aqObject.CheckProperty(textBox4, "wText", cmpEqual, "5")
  tabControl = securitySetup.TabControl
  xamDataGrid = tabControl.gridCameraPermissions
  xamDataGrid.ClickCell(3, "AllowViewing")
  xamDataGrid.ClickCell(3, "AllowPlayback")
  xamDataGrid.ClickCell(10, "AllowViewing")
  recordListControl = xamDataGrid.RecordListControl
  aqObject.CheckProperty(recordListControl.XamCheckEditor, "IsChecked", cmpEqual, True)
  aqObject.CheckProperty(recordListControl.XamCheckEditor2, "IsChecked", cmpEqual, True)
  aqObject.CheckProperty(recordListControl.XamCheckEditor3, "IsChecked", cmpEqual, True)
  aqObject.CheckProperty(recordListControl.XamCheckEditor4, "IsChecked", cmpEqual, False)
  tabControl.ClickTab("Other Resources")
  xamDataGrid = tabControl.gridResourcePermissions
  xamDataGrid.ClickCell(2, "HasPermission")
  xamDataGrid.ClickCell(3, "HasPermission")
  recordListControl = xamDataGrid.RecordListControl
  aqObject.CheckProperty(recordListControl.XamCheckEditor, "IsChecked", cmpEqual, True)
  aqObject.CheckProperty(recordListControl.XamCheckEditor2, "IsChecked", cmpEqual, True)
  button = securitySetup.ButtonSave
  aqObject.CheckProperty(button, "Enabled", cmpEqual, True)
  button.ClickButton()
  aqObject.CheckProperty(button, "Enabled", cmpEqual, False)
  securitySetup.WindowButtonCommands.Click(106, 19)
  button = mainWindow.WindowCommands.UserPB
  button.ClickButton()
  button.PopupMenu.Click("Log Out")
  
  hwndSource = VIMonitorPlus.HwndSource_LoginWindow
  loginWindow = hwndSource.LoginWindow   
  textBox = loginWindow.txtUserName
  textBox.SetText("Vikas"+sRand)
  passwordBox = loginWindow.txtPassword
  passwordBox.SetText(Project.Variables.Password)
  loginWindow.cboLoginMode.ClickItem("Multiple Servers")  
  loginWindow.btnLogIn.ClickButton()
  hwndSource = VIMonitorPlus.HwndSource_MainWindow
  mainWindow = hwndSource.MainWindow
  mainWindow.WindowButtonCommands.Click()
  aqObject.CheckProperty(mainWindow.WindowCommands.TextblockAdministrator, "WPFControlText", cmpEqual, "Vikas"+sRand)
  treeView = mainWindow.treeServers
  treeViewItem = treeView.TreeviewitemDemoipCom
  aqObject.CheckProperty(treeViewItem.TextblockDemoipCom, "WPFControlText", cmpEqual, "demoip.com")
  treeViewItem.WaitWPFObject("TreeViewItem", "",1 ,50000)
  expander = mainWindow.expCameras
  expander.Expand()
  treeView = expander.treeCameras
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.expCameras.treeCameras.TreeviewitemParkingCameraH265, "WPFControlText", cmpEqual, "Parking Camera (H.265)")
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.expCameras.treeCameras.TreeviewitemWvS4176H265, "WPFControlText", cmpEqual, "WV-S4176(H.265)")
  treeView.ClickItem("|[0]")
  tabControl = mainWindow.tabWorkspaces
  button = tabControl.playbackModeButton
  button.ClickButton()
  aqObject.CheckProperty(tabControl.btnExportVideoClip, "Exists", cmpEqual, True)
  tabControl.btnSwitchToLive.ClickButton()
  treeView.ClickItem("|[1]")
  button.ClickButton()
  messageBoxVI = VIMonitorPlus.MessageBoxVI
  aqObject.CheckProperty(messageBoxVI.zMonitorStationEx_UltraFormManager_Dock_Area_Top, "Exists", cmpEqual, True)
  panel = messageBoxVI.VIMessageBox_Fill_Panel.UltraPanelClientAreaUnsafe.pnlTop
  aqObject.CheckProperty(panel.lblMessage, "Text", cmpEqual, "You do not have permission to view recorded video for one or more of the selected cameras.")
  panel.TableLayoutPanel1.btnOk.ClickButton()
  expander2 = mainWindow.expLayouts
  expander2.Expand()
  treeView = expander2.treeLayouts
  aqObject.CheckProperty(treeView.TreeviewitemPocView1.TextblockPocView1, "WPFControlText", cmpEqual, "POC_View1")
  treeView.ClickItem("|[0]")
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.TabitemPocView1, "WPFControlText", cmpEqual, "POC_View1")
  expander = mainWindow.expMaps
  expander.Expand()
  treeView2 = expander.treeMaps
  aqObject.CheckProperty(treeView2.TreeviewitemPocMap1.TextblockPocMap1, "WPFControlText", cmpEqual, "POC_Map1")
  treeView2.ClickItem("|[0]")
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.TabitemPocMap1, "WPFControlText", cmpEqual, "POC_Map1")
  TestedApps.VIMonitorPlus.Terminate()