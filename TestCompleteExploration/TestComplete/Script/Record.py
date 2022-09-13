#ḍef main():
  # Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.TextblockNewWorkspaces.Click()
   
def Test1():
  tabControl = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces
  aqObject.CheckProperty(tabControl.TextblockNewWorkspaces, "ClrClassName", cmpEqual, "TextBlock")
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.Border, "IsVisible", cmpEqual, True)
  aqObject.CheckProperty(tabControl.TextblockApplicationPlugIns, "ClrClassName", cmpEqual, "TextBlock")

def Test2():
  hwndSource = Aliases.VIMonitorPlus.HwndSource_MainWindow
  hwndSource.MainWindow.tabWorkspaces.Button.ClickButton()
  videoContainer = hwndSource.WinFormsAdapter.VideoContainer
  aqObject.CheckProperty(videoContainer.pnlBackground_6950726765843833856_0_12408804398585512806, "Enabled", cmpEqual, True)
  videoContainer.pnlBackground_6950726765843833856_0_16184689649413323230.Click(603, 112)

def Test3():
  VIMonitorPlus = Aliases.VIMonitorPlus
  mainWindow = VIMonitorPlus.HwndSource_MainWindow.MainWindow
  mainWindow.treeServers.ClickItem("|[0]|[6]")
  windowCommandsItem = mainWindow.WindowCommands.WindowCommandsItem
  windowCommandsItem.Click(77, 27)
  aqObject.CheckProperty(windowCommandsItem.TextblockAdministrator, "WPFControlText", cmpEqual, "Administrator")
  windowCommandsItem.AlertPB.ClickButton()
  textBlock = VIMonitorPlus.HwndSource_PopupRoot.PopupRoot.TextblockDownloads
  OCR.Recognize(textBlock).BlockByText("Downloads").Click()
  OCR.Recognize(textBlock).BlockByText("Downloads").Click()
  aqObject.CheckProperty(textBlock, "WPFControlText", cmpEqual, "Downloads")

def Test5():
  loginWindow = Aliases.VIMonitorPlus.HwndSource_LoginWindow.LoginWindow
  textBox = loginWindow.txtUserName
  textBox.Click(141, 24)
  textBox.Keys("^a")
  textBox.SetText("")
  aqObject.CheckProperty(textBox, "IsVisible", cmpEqual, True)
  textBox.SetText("Administrator")
  aqObject.CheckProperty(loginWindow.txtPassword, "IsVisible", cmpEqual, True)

def Test4():
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_LoginWindow.LoginWindow.btnLogIn, "WPFControlText", cmpEqual, "Log In")

def Test6():
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow, "WPFControlText", cmpEqual, "VI MonitorPlus")
  aqObject.CheckProperty(NameMapping.Sys.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.Button2, "IsVisible", cmpEqual, True)

def Test7():
  hwndSource = Aliases.VIMonitorPlus.HwndSource_MainWindow
  mainWindow = hwndSource.MainWindow
  treeViewItem = mainWindow.treeServers.TreeviewitemDemoipCom
  treeViewItem2 = treeViewItem.TreeviewitemParkingCameraH265
  aqObject.CheckProperty(treeViewItem2.TextblockParkingCameraH265, "WPFControlText", cmpEqual, "Parking Camera (H.265)")
  treeViewItem2.Drag(184, 12, 291, 52)
  treeViewItem2 = treeViewItem.TreeviewitemTrainCameraH264
  aqObject.CheckProperty(treeViewItem2.TextblockTrainCameraH264, "WPFControlText", cmpEqual, "Train Camera (H.264)")
  treeViewItem2.Drag(163, 18, 1074, 129)
  videoContainer = hwndSource.WinFormsAdapter.VideoContainer
  aqObject.CheckProperty(videoContainer.pnlBackground_6950726765843833856_0_3753112684744761249.lblDisplayCtrl_6950726765843833856_990648698_3753112684744761249, "Name", cmpEqual, "lblDisplayCtrl_6950726765843833856_990648698_3753112684744761249")
  aqObject.CheckProperty(videoContainer.pnlBackground_6950726765843833856_0_12401977592198128397.lblDisplayCtrl_6950726765843833856_406392038_12401977592198128397, "Name", cmpEqual, "lblDisplayCtrl_6950726765843833856_406392038_12401977592198128397")
  button = mainWindow.WindowCommands.WindowCommandsItem.UserPB
  button.ClickButton()
  button.PopupMenu.Click("Log Out")


def Test8():
  videoContainer = Aliases.VIMonitorPlus.HwndSource_MainWindow.WinFormsAdapter.VideoContainer
  aqObject.CheckProperty(videoContainer.pnlBackground_EmptyServerList_0_18200774302212082740.lblDisplayCtrl_EmptyServerList_0_18200774302212082740, "Name", cmpEqual, "lblDisplayCtrl_EmptyServerList_0_18200774302212082740")
  aqObject.CheckProperty(videoContainer.pnlBackground_EmptyServerList_0_13821590524154957167, "Name", cmpEqual, "pnlBackground_EmptyServerList_0_13821590524154957167")
  aqObject.CheckProperty(NameMapping.Sys.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.Button2, "IsVisible", cmpEqual, True)
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.Textblock2Cameras, "WPFControlText", cmpEqual, "2 Cameras")

def DeleteUser():
  VIMonitorPlus = Aliases.VIMonitorPlus
  menu = VIMonitorPlus.HwndSource_MainWindow.MainWindow.mnuMain
  aqObject.CheckProperty(menu.mnuAdministration, "WPFControlText", cmpEqual, "Administration")
  menu.WPFMenu.Click("Administration|Users & Groups|Setup and Configuration")
  securitySetup = VIMonitorPlus.HwndSource_SecuritySetup.SecuritySetup
  aqObject.CheckProperty(securitySetup.expUsers, "IsVisible", cmpEqual, True)
  treeView = securitySetup.treeUsers
  treeView.ClickItem("|[12]")
  treeViewItem = treeView.TreeviewitemSuresh73
  treeViewItem.ClickR(173, 9)
  aqObject.CheckProperty(VIMonitorPlus.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuitemDeleteUser, "WPFControlText", cmpEqual, "Delete User")
  treeViewItem.ClickR(221, 15)
  treeView.TreeviewitemNewUser.StackPanel.PopupMenu.Click("Delete User")
  panel = VIMonitorPlus.MessageBoxVI.VIMessageBox_Fill_Panel.UltraPanelClientAreaUnsafe.pnlTop
  aqObject.CheckProperty(panel.lblMessage, "Text", cmpEqual, "Delete the user 'suresh73' from the system?")
  panel.TableLayoutPanel1.btnYes.ClickButton()

def Test9():
  Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.WindowButtonCommands.Click(18, 0)
  Aliases.explorer.wndShell_TrayWnd.DesktopWindowXamlSource.Click(1161, 28)

def Test10():
  VIMonitorPlus = Aliases.VIMonitorPlus
  treeView = VIMonitorPlus.HwndSource_SecuritySetup.SecuritySetup.treeUsers
  treeViewItem = treeView.TreeviewitemSuresh252
  aqObject.CheckProperty(treeViewItem, "ClrFullClassName", cmpEqual, "System.Windows.Controls.TreeViewItem")
  treeViewItem.ClickR(183, 22)
  treeViewItem.ClickR(124, 15)
  treeView.ClickItem("|[12]")
  treeViewItem.ExpandItem("|[12]")
  treeViewItem.ClickR(99, 15)
  treeView.TreeviewitemNewUser.StackPanel.PopupMenu.Click("Delete User")
  VIMonitorPlus.MessageBoxVI.VIMessageBox_Fill_Panel.UltraPanelClientAreaUnsafe.pnlTop.TableLayoutPanel1.btnYes.ClickButton()

def Test11():
  securitySetup = Aliases.VIMonitorPlus.HwndSource_SecuritySetup.SecuritySetup
  treeView = securitySetup.treeUsers
  treeView.TreeviewitemSuresh620.MouseWheel(1)
  treeView.TreeviewitemSuresh324.MouseWheel(3)
  treeView.TreeviewitemSuresh4.MouseWheel(1)
  treeView.TreeviewitemSuresh1.MouseWheel(3)
  treeView.TreeviewitemDemouser1.MouseWheel(9)
  aqObject.CheckProperty(securitySetup.expUsers, "ClrFullClassName", cmpEqual, "System.Windows.Controls.Expander")
  treeView.ClickItem("|[10]")

def Test12():
  desktopWindowXamlSource = Aliases.explorer.wndShell_TrayWnd.DesktopWindowXamlSource
  desktopWindowXamlSource.Click(1191, 41)
  desktopWindowXamlSource.Click(1204, 39)
  desktopWindowXamlSource.Click(1204, 39)
  VIMonitorPlus = Aliases.VIMonitorPlus
  hwndSource = VIMonitorPlus.HwndSource_SecuritySetup
  expander = hwndSource.SecuritySetup.expSearch
  expander.Expand()
  expander.Keys("![ReleaseLast]VIkas11")
  treeView = expander.treeSearch
  treeViewItem = treeView.TreeviewitemVikas1119
  stackPanel = treeViewItem.StackPanel
  aqObject.CheckProperty(stackPanel, "IsVisible", cmpEqual, True)
  treeView.ClickItem("|[0]")
  treeViewItem.ClickR(163, 24)
  hwndSource.Keys("[Tab]")
  stackPanel.PopupMenu.Click("Delete User")
  VIMonitorPlus.MessageBoxVI.VIMessageBox_Fill_Panel.UltraPanelClientAreaUnsafe.pnlTop.TableLayoutPanel1.btnYes.ClickButton()

def Test13():
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_SecuritySetup.SecuritySetup.expSearch.treeSearch.TreeviewitemVikas1948, "WPFControlText", cmpEqual, "Vikas1948")

def Test14():
  VIMonitorPlus = Aliases.VIMonitorPlus
  OCR.Recognize(VIMonitorPlus.HwndSource_SecuritySetup.SecuritySetup.expSearch.treeSearch.TreeviewitemVikas1948.TextblockVikas1948).BlockByText("1948").ClickR()
  aqObject.CheckProperty(VIMonitorPlus.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuitemDeleteUser, "WPFControlText", cmpEqual, "Delete User")

def Test15():
  treeViewItem = Aliases.VIMonitorPlus.HwndSource_SecuritySetup.SecuritySetup.expSearch.treeSearch.TreeviewitemVikas1948
  treeViewItem.ClickR(49, 3)
  OCR.Recognize(treeViewItem.TextblockVikas1948).BlockByText("Vikas").ClickR()
  treeViewItem.StackPanel.PopupMenu.Click("Delete User")

def Test16():
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_SecuritySetup.SecuritySetup, "WPFControlText", cmpEqual, "Security Setup")

def Test17():
  explorer = Aliases.explorer
  explorer.wndShell_TrayWnd.DesktopWindowXamlSource.Click(960, 59)
  HWNDView = explorer.wndDesktop.Desktop.DUIViewWndClassName.Explorer_Pane
  UIItemsView = HWNDView.CtrlNotifySink.ShellView.Items_View
  UIItemsView.VI_MonitorPLus.DblClick(29, 34)
  HWNDView.CtrlNotifySink2.NamespaceTreeControl.tvNamespaceTreeControl.ExpandItem("|Desktop|Network")
  UIItemsView.File217.Name.Click(10, 5)

def Test18():
  expander = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.expSearch
  expander.Expand()
  aqObject.CheckProperty(expander, "WPFControlText", cmpEqual, "Search")
  expander.Click(146, 23)
  expander.Keys("P")
  expander.Keys("OC")
  treeView = expander.treeSearch
  aqObject.CheckProperty(treeView.TreeviewitemPocView1.TextblockPocView1, "WPFControlText", cmpEqual, "POC_View1")
  treeView.ClickItem("|[0]")

def Test19():
  VIMonitorPlus = Aliases.VIMonitorPlus
  VIMonitorPlus.HwndSource_MainWindow.MainWindow.expSearch.Click(215, 15)
  aqObject.CheckProperty(VIMonitorPlus.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator, "IsVisible", cmpEqual, True)

def Test20():
  VIMonitorPlus = Aliases.VIMonitorPlus
  expander = VIMonitorPlus.HwndSource_MainWindow.MainWindow.expSearch
  expander.Click(227, 16)
  expander.Click(222, 20)
  VIMonitorPlus.HwndSource_PopupRoot.Click(986, -66)

def Test21():
  VIMonitorPlus = Aliases.VIMonitorPlus
  mainWindow = VIMonitorPlus.HwndSource_MainWindow.MainWindow
  expander = mainWindow.expServers
  expander.Click(216, 21)
  expander.Click(216, 21)
  hwndSource = VIMonitorPlus.HwndSource_PopupRoot
  hwndSource.Click(921, -113)
  mainWindow.expSearch.Click(216, 24)
  hwndSource.Click(921, -73)

def Test22():
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  expander = mainWindow.expCameras
  expander.Expand()
  aqObject.CheckProperty(expander.treeCameras, "IsVisible", cmpEqual, True)
  expander = mainWindow.expLayouts
  expander.Expand()
  expander.treeLayouts.ClickItem("|[0]")
  tabControl = mainWindow.tabWorkspaces
  aqObject.CheckProperty(tabControl.TabitemPocView1, "WPFControlText", cmpEqual, "POC_View1")
  expander = mainWindow.expMaps
  expander.Expand()
  expander.treeMaps.ClickItem("|[0]")
  aqObject.CheckProperty(tabControl.imgMap, "IsVisible", cmpEqual, True)

def Test23():
  Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.expCameras.Expand()

def Test24():
  tabControl = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces
  tabControl.ClickTab("New Workspace")
  tabControl.ClickTab("+")
  tabControl.ClickTab(1)

def Test25():
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_SecuritySetup.SecuritySetup.expSearch.treeSearch.UserNameDelete.StackPanel2, "IsVisible", cmpEqual, True)

def Test26():
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.WinFormsAdapter.VideoContainer.pnlBackground_6950726765843833856_0_10947471488145003625, "Enabled", cmpEqual, True)

def Test27():
  videoContainer = Aliases.VIMonitorPlus.HwndSource_MainWindow.WinFormsAdapter.VideoContainer
  aqObject.CheckProperty(videoContainer, "ClrClassName", cmpEqual, "VideoContainer")
  videoContainer.pnlBackground_6950726765843833856_0_15056904352359374772.MouseWheel(-1)

def Test28():
  button = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.StackPanel2.Button2
  aqObject.CheckProperty(button, "IsVisible", cmpEqual, True)
  button.ClickButton()

def Test29():
  tabControl = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces
  button = tabControl.StackPanel2.Button
  aqObject.CheckProperty(button.Textblock1Camera, "WPFControlText", cmpEqual, "1 Camera")
  button.ClickButton()
  aqObject.CheckProperty(tabControl.cboLayoutType, "Name", cmpEqual, "cboLayoutType")

def Test30():
  VIMonitorPlus = Aliases.VIMonitorPlus
  mainWindow = VIMonitorPlus.HwndSource_MainWindow.MainWindow
  comboBox = mainWindow.tabWorkspaces.cboLayoutType
  comboBox.DropDown()
  comboBox.ClickItem(10)
  comboBox.DropDown()
  VIMonitorPlus.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.ComboBoxItem.MouseWheel(-2)
  comboBox.ClickItem(4)
  mainWindow.WindowButtonCommands.Click(37, 12)

def Test31():
  tabControl = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces
  tabControl.TabitemCameraView
  aqObject.CheckProperty(tabControl.TabitemCameraView, "IsVisible", cmpEqual, True)

def Test32():
  comboBox = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.cboLayoutType
  comboBox.DropDown()
  aqObject.CheckProperty(comboBox, "IsVisible", cmpEqual, True)
  comboBox.ClickItem(5)

def Test33():
  Aliases.explorer.wndShell_TrayWnd.DesktopWindowXamlSource.Click(984, 59)


def Test34():
  comboBox = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.cboLayoutType
  comboBox.DropDown()
  comboBox.ClickItem(0)
  comboBox.DropDown()
  comboBox.CloseUp()

def Test35():
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.Button4, "IsVisible", cmpEqual, True)

def Test36():
  tabControl = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces
  aqObject.CheckProperty(tabControl.Textblock1Camera, "IsVisible", cmpEqual, True)
  aqObject.CheckProperty(tabControl.Textblock2Cameras, "IsVisible", cmpEqual, True)
  aqObject.CheckProperty(tabControl.Button.Textblock4Cameras, "IsVisible", cmpEqual, True)
  aqObject.CheckProperty(tabControl.Button3.Textblock8Cameras, "IsVisible", cmpEqual, True)
  aqObject.CheckProperty(tabControl.Button4.Textblock9Cameras, "IsVisible", cmpEqual, True)
  aqObject.CheckProperty(tabControl.Textblock10Cameras, "IsVisible", cmpEqual, True)
  aqObject.CheckProperty(tabControl.Textblock13Cameras, "IsVisible", cmpEqual, True)
  aqObject.CheckProperty(tabControl.Textblock13Cameras2, "IsVisible", cmpEqual, True)
  aqObject.CheckProperty(tabControl.Textblock16Cameras, "IsVisible", cmpEqual, True)
  aqObject.CheckProperty(tabControl.Textblock19Cameras, "IsVisible", cmpEqual, True)
  aqObject.CheckProperty(tabControl.Textblock25Cameras, "IsVisible", cmpEqual, True)
  aqObject.CheckProperty(tabControl.Button32, "IsVisible", cmpEqual, True)
  aqObject.CheckProperty(tabControl.Textblock18CamerasWide, "IsVisible", cmpEqual, True)
  aqObject.CheckProperty(tabControl.Textblock24CamerasWide, "IsVisible", cmpEqual, True)

def Test37():
  tabControl = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces
  aqObject.CheckProperty(tabControl.Textblock1Camera, "WPFControlText", cmpEqual, "1 Camera")
  textBlock = tabControl.Textblock24CamerasWide
  aqObject.CheckProperty(textBlock, "WPFControlText", cmpEqual, "2 Cameras")
  aqObject.CheckProperty(textBlock, "WPFControlText", cmpEqual, "4 Cameras")

def Test38():
  tabControl = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces
  textBlock = tabControl.Textblock24CamerasWide
  aqObject.CheckProperty(textBlock, "WPFControlText", cmpEqual, "24 Cameras (Wide)")
  aqObject.CheckProperty(tabControl.Textblock18CamerasWide, "WPFControlText", cmpEqual, "18 Cameras (Wide)")
  aqObject.CheckProperty(textBlock, "WPFControlText", cmpEqual, "36 Cameras")
  aqObject.CheckProperty(tabControl.Textblock25Cameras, "WPFControlText", cmpEqual, "25 Cameras")
  aqObject.CheckProperty(tabControl.Textblock19Cameras, "WPFControlText", cmpEqual, "19 Cameras")
  aqObject.CheckProperty(textBlock, "WPFControlText", cmpEqual, "16 Cameras")
  aqObject.CheckProperty(tabControl.Textblock13Cameras2, "WPFControlText", cmpEqual, "13 Cameras")
  aqObject.CheckProperty(tabControl.Textblock13Cameras, "WPFControlText", cmpEqual, "13 Cameras")

def Test39():
  tabControl = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces
  aqObject.CheckProperty(tabControl.Tabitem1CameraView2, "WPFControlText", cmpEqual, "1 Camera View")
  aqObject.CheckProperty(tabControl.Tabitem2CameraView, "WPFControlText", cmpEqual, "2 Camera View")
  aqObject.CheckProperty(tabControl.Tabitem4CameraView, "WPFControlText", cmpEqual, "4 Camera View")
  aqObject.CheckProperty(tabControl.Tabitem8CameraView, "WPFControlText", cmpEqual, "8 Camera View")
  aqObject.CheckProperty(tabControl.Tabitem9CameraView, "WPFControlText", cmpEqual, "9 Camera View")
  aqObject.CheckProperty(tabControl.Tabitem10CameraView, "WPFControlText", cmpEqual, "10 Camera View")
  tabItem = tabControl.Tabitem13CameraView
  aqObject.CheckProperty(tabItem, "WPFControlText", cmpEqual, "13 Camera View")
  aqObject.CheckProperty(tabItem, "WPFControlText", cmpEqual, "13 Camera View")
  aqObject.CheckProperty(tabControl.Tabitem16CameraView, "WPFControlText", cmpEqual, "16 Camera View")
  aqObject.CheckProperty(tabControl.Tabitem19CameraView, "WPFControlText", cmpEqual, "19 Camera View")
  aqObject.CheckProperty(tabControl.Tabitem25CameraView, "WPFControlText", cmpEqual, "25 Camera View")
  aqObject.CheckProperty(tabControl.Tabitem36CameraView, "WPFControlText", cmpEqual, "36 Camera View")
  aqObject.CheckProperty(tabControl.Tabitem18CameraView, "WPFControlText", cmpEqual, "18 Camera View")
  aqObject.CheckProperty(tabControl.Tabitem24CameraView, "WPFControlText", cmpEqual, "24 Camera View")

def Test40():
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.WindowCommands.WindowCommandsItem.TextblockAdministrator, "WPFControlText", cmpEqual, "Administrator")

def Test41():
  loginWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.LoginWindow
  button = loginWindow.btnLogIn
  aqObject.CheckProperty(button, "WPFControlText", cmpEqual, "Log In")
  textBox = loginWindow.txtUserName
  textBox.Click(179, 27)
  textBox.Keys("^a")
  textBox.SetText("Administrator")
  passwordBox = loginWindow.txtPassword
  passwordBox.Click(67, 22)
  passwordBox.SetText(Project.Variables.Password1)
  loginWindow.cboLoginMode.ClickItem("Multiple Servers")
  button.ClickButton()

def Test42():
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.Button2, "IsVisible", cmpEqual, True)

def Test43():
  hwndSource = Aliases.VIMonitorPlus.HwndSource_MainWindow
  mainWindow = hwndSource.MainWindow
  mainWindow.tabWorkspaces.Camera4.ClickButton()
  treeViewItem = mainWindow.treeServers.TreeviewitemDemoipCom
  treeViewItem.TreeviewitemParkingCameraH265.Drag(121, 8, 558, 65)
  treeViewItem.TreeviewitemTrainCameraH264.Drag(65, 13, 1515, 106)
  treeViewItem.TreeviewitemWvU1142H265.Drag(118, 20, 867, 575)
  hwndSource.WinFormsAdapter.VideoContainer.pnlBackground_6950726765843833856_0_17500462890428936937.DragM(730, 352, 17, -15)
  treeViewItem.TreeviewitemSncEm641.Drag(132, 11, 1653, 492)

def Test44():
  videoContainer = Aliases.VIMonitorPlus.HwndSource_MainWindow.WinFormsAdapter.VideoContainer
  aqObject.CheckProperty(videoContainer.pnlBackground_6950726765843833856_0_6445497542269588713.lblDisplayCtrl_6950726765843833856_990648698_6445497542269588713, "Name", cmpEqual, "lblDisplayCtrl_6950726765843833856_990648698_6445497542269588713")
  aqObject.CheckProperty(videoContainer.pnlBackground_6950726765843833856_0_16423586375518687464.lblDisplayCtrl_6950726765843833856_406392038_16423586375518687464, "Name", cmpEqual, "lblDisplayCtrl_6950726765843833856_406392038_16423586375518687464")
  aqObject.CheckProperty(videoContainer.pnlBackground_6950726765843833856_0_9197682878936359476.lblDisplayCtrl_6950726765843833856_1791570276_9197682878936359476, "Name", cmpEqual, "lblDisplayCtrl_6950726765843833856_1791570276_9197682878936359476")

def Test45():
  pass

def Test46():
  VIMonitorPlus = Aliases.VIMonitorPlus2
  VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.btnExportVideoClip.ClickButton()
  exportMultiplexVideo = VIMonitorPlus.HwndSource_ExportMultiplexVideo.ExportMultiplexVideo
  watermarkTextBox = exportMultiplexVideo.wtmTxtStartDateTime
  watermarkTextBox.Click(170, 13)
  aqObject.CheckProperty(watermarkTextBox, "Name", cmpEqual, "wtmTxtStartDateTime")
  watermarkTextBox = exportMultiplexVideo.wtmTxtEndDateTime
  watermarkTextBox.Click(149, 27)
  aqObject.CheckProperty(watermarkTextBox, "Name", cmpEqual, "wtmTxtEndDateTime")

def Test47():
  treeViewItem = Aliases.VIMonitorPlus2.HwndSource_MainWindow.MainWindow.treeServers.TreeviewitemDemoipCom
  aqObject.CheckProperty(treeViewItem, "WPFControlText", cmpEqual, "demoip.com")
  aqObject.CheckProperty(treeViewItem.TextblockDemoipCom, "WPFControlText", cmpEqual, "demoip.com")
  aqObject.CheckProperty(treeViewItem.TreeviewitemParkingCameraH265.TextblockParkingCameraH265, "WPFControlText", cmpEqual, "Parking Camera (H.265)")
  aqObject.CheckProperty(treeViewItem.TreeviewitemTrainCameraH264, "WPFControlText", cmpEqual, "Train Camera (H.264)")

def Test48():
  hwndSource = Aliases.VIMonitorPlus2.HwndSource_MainWindow
  treeViewItem = hwndSource.MainWindow.treeServers.TreeviewitemDemoipCom
  treeViewItem.TreeviewitemParkingCameraH265.Drag(133, 12, 409, 33)
  videoContainer = hwndSource.WinFormsAdapter.VideoContainer
  aqObject.CheckProperty(videoContainer.pnlBackground_6950726765843833856_0_4890587338688359686, "ClrFullClassName", cmpEqual, "System.Windows.Forms.Panel")
  treeViewItem.TreeviewitemTrainCameraH264.Drag(156, 19, 1119, 97)
  aqObject.CheckProperty(videoContainer.pnlBackground_6950726765843833856_0_5013642087305423551.lblDisplayCtrl_6950726765843833856_406392038_5013642087305423551, "ClrFullClassName", cmpEqual, "System.Windows.Forms.Label")

def Test49():
  VIMonitorPlus = Aliases.VIMonitorPlus2
  hwndSource = VIMonitorPlus.HwndSource_MainWindow
  hwndSource.WinFormsAdapter.VideoContainer.pnlBackground_6950726765843833856_0_10908231581710604857.lblDisplayCtrl_6950726765843833856_990648698_10908231581710604857.MouseWheel(1)
  hwndSource.MainWindow.tabWorkspaces.btnSnapshot.ClickButton()
  cameraSnapshot = VIMonitorPlus.HwndSource_CameraSnapshot.CameraSnapshot
  aqObject.CheckProperty(cameraSnapshot, "WPFControlText", cmpEqual, "Camera Snapshot")
  cameraSnapshot.radioBtnFile.ClickButton()
  button = cameraSnapshot.btnBrowse
  aqObject.CheckProperty(button, "WPFControlText", cmpEqual, "...")
  button.ClickButton()
  dlgSaveAs = VIMonitorPlus.dlgSaveAs
  HWNDView = dlgSaveAs.DUIViewWndClassName.Explorer_Pane
  edit = HWNDView.FloatNotifySink.ComboBox.Edit
  edit.Click(268, 17)
  edit.Keys("![ReleaseLast]")
  progress = dlgSaveAs.WorkerW.ReBarWindow32.AddressBandRoot.progress
  progress.BreadcrumbParent.toolbarAddressDesktop.Click(190, 22)
  comboBox = progress.comboBox
  comboBox.SetText("C:\\Users\\LENOVO\\Pictures\\Sample")
  comboBox.ComboBox.Edit.Keys("[Enter]")
  comboBox = HWNDView.FloatNotifySink2.ComboBox
  comboBox.Edit.Click(63, 9)
  comboBox.SetText("First")
  dlgSaveAs.btnSave.ClickButton()
  cameraSnapshot.buttonOK.ClickButton()

def Test50():
  explorer = Aliases.explorer
  explorer.wndShell_TrayWnd.DesktopWindowXamlSource.Click(955, 30)
  wndCabinetWClass = explorer.wndDesktop
  progress = wndCabinetWClass.WorkerW.ReBarWindow32.AddressBandRoot.progress
  comboBox = progress.comboBox
  progress.BreadcrumbParent.toolbarAddressQuickAccess.Click(325, 13)
  comboBox.SetText("C:\\Users\\LENOVO\\Pictures\\Sample")
  comboBox.ComboBox.Edit.Keys("[Enter]")
  aqObject.CheckProperty(wndCabinetWClass.Desktop.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.Second, "Value", cmpEqual, "Second")  
  wndCabinetWClass.Close()
