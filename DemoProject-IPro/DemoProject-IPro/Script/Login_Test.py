﻿def Test1():
  desktopWindowXamlSource = Aliases.explorer.wndShell_TrayWnd.DesktopWindowXamlSource
  desktopWindowXamlSource.Click(1336, 32)
  Aliases.VIMonitorPlus = Aliases.Aliases.VIMonitorPlus
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  mainWindow.mnuMain.WPFMenu.Click("Administration|Users & Groups|Setup and Configuration")
  securitySetup = Aliases.VIMonitorPlus.HwndSource_SecuritySetup.SecuritySetup
  aqObject.CheckProperty(securitySetup, "WPFControlText", cmpEqual, "Security Setup")
  expander = securitySetup.expUsers
  aqObject.CheckProperty(expander, "WPFControlText", cmpEqual, "Users")
  aqObject.CheckProperty(securitySetup.TextblockSelectAUserGroupOrClickTheButton, "WPFControlText", cmpEqual, "Select a User/Group or click the + button.")
  expander.Click(261, 21)
  aqObject.CheckProperty(securitySetup.TextblockUserInformation, "WPFControlText", cmpEqual, "User Information")
  aqObject.CheckProperty(securitySetup.TextblockPermissions, "WPFControlText", cmpEqual, "Permissions")
  aqObject.CheckProperty(securitySetup.TextboxUserId, "wText", cmpEqual, "3490830517939722240")
  textBox = securitySetup.txtUserName
  textBox.DblClick(119, 22)
  textBox.Keys("^a")
  textBox.SetText("Vikas2")
  textBox2 = securitySetup.TextboxFullName
  textBox2.Click(38, 23)
  textBox2.SetText("Vol2")
  textBox3 = securitySetup.TextboxEmail
  textBox3.Click(59, 13)
  textBox3.SetText("v1@gmail.com")
  passwordBox = securitySetup.PasswordBox
  passwordBox.Click(39, 18)
  passwordBox.SetText(Project.Variables.Password1)
  passwordBox.Keys("![ReleaseLast]")
  passwordBox.SetText(Project.Variables.Password2)
  passwordBox2 = securitySetup.PasswordboxVerify
  passwordBox2.Click(63, 19)
  passwordBox2.SetText(Project.Variables.Password2)
  toggleButton = securitySetup.ToggleButton
  toggleButton.ClickButton(cbChecked)
  textBox4 = securitySetup.TextBox
  textBox4.Click(33, 9)
  textBox4.SetText("5")
  aqObject.CheckProperty(textBox, "wText", cmpEqual, "Vikas2")
  aqObject.CheckProperty(textBox2, "wText", cmpEqual, "Vol2")
  aqObject.CheckProperty(textBox3, "wText", cmpEqual, "v1@gmail.com")
  aqObject.CheckProperty(passwordBox, "wText", cmpEqual, "Orbita11")
  aqObject.CheckProperty(passwordBox2, "wText", cmpEqual, "Orbita11")
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
  desktopWindowXamlSource.Click(1353, 34)
  button = mainWindow.WindowCommands.UserPB
  button.ClickButton()
  button.PopupMenu.Click("Log Out")
  loginWindow = Aliases.VIMonitorPlus.HwndSource_LoginWindow.LoginWindow
  textBox = loginWindow.txtUserName
  textBox.Click(122, 32)
  textBox.Keys("^a")
  textBox.SetText("Vikas2")
  passwordBox = loginWindow.txtPassword
  passwordBox.Click(82, 18)
  passwordBox.SetText(Project.Variables.Password2)
  loginWindow.btnLogIn.ClickButton()
  expander = mainWindow.expCameras
  expander.Expand()
  treeView = expander.treeCameras
  treeView.ClickItem("|[0]")
  tabControl = mainWindow.tabWorkspaces
  button = tabControl.playbackModeButton
  button.ClickButton()
  aqObject.CheckProperty(tabControl.btnExportVideoClip, "Exists", cmpEqual, True)
  tabControl.btnSwitchToLive.ClickButton()
  treeView.ClickItem("|[1]")
  button.ClickButton()
  messageBoxVI = Aliases.VIMonitorPlus.MessageBoxVI
  aqObject.CheckProperty(messageBoxVI.zMonitorStationEx_UltraFormManager_Dock_Area_Top, "Exists", cmpEqual, True)
  panel = messageBoxVI.VIMessageBox_Fill_Panel.UltraPanelClientAreaUnsafe.pnlTop
  aqObject.CheckProperty(panel.lblMessage, "Text", cmpEqual, "You do not have permission to view recorded video for one or more of the selected cameras.")
  panel.TableLayoutPanel1.btnOk.ClickButton()
  expander2 = mainWindow.expLayouts
  expander2.Expand()
  expander.Expand()
  expander2.Expand()
  treeView = expander2.treeLayouts
  aqObject.CheckProperty(treeView.TreeviewitemPocView1.TextblockPocView1, "WPFControlText", cmpEqual, "POC_View1")
  expander = mainWindow.expMaps
  expander.Expand()
  treeView2 = expander.treeMaps
  aqObject.CheckProperty(treeView2.TreeviewitemPocMap1.TextblockPocMap1, "WPFControlText", cmpEqual, "POC_Map1")
  expander2.Expand()
  treeView.ClickItem("|[0]")
  expander.Expand()
  treeView2.ClickItem("|[0]")
