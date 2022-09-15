﻿def launchVIMonitorPlusApplication():
  TestedApps.VIMonitorPlus.Run(1, True)
  Sys.WaitProcess("VIMonitorPlus",60000)  
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_LoginWindow.LoginWindow.Image, "FullName", cmpEqual, 'Sys.Process(\"VIMonitorPlus\").WPFObject(\"HwndSource: LoginWindow\", \"VI MonitorPlus\").WPFObject(\"LoginWindow\", \"VI MonitorPlus\", 1).WPFObject(\"LoginCanvas\").WPFObject(\"LoginPanel\").WPFObject(\"StackPanel\", \"\", 1).WPFObject(\"Image\", \"\", 1)')
  
  
def loginInToApplication(username, password, serverType, serverName, PortNumber):
  VIMonitorPlus = Aliases.VIMonitorPlus
  hwndSource = VIMonitorPlus.HwndSource_LoginWindow
  loginWindow = hwndSource.LoginWindow   
  textBox = loginWindow.txtUserName
  textBox.SetText(username)
  passwordBox = loginWindow.txtPassword
  passwordBox.SetText(password)
  loginWindow.cboLoginMode.ClickItem(serverType)
  dataGrid = loginWindow.gridConnections
  
  popupRoot = VIMonitorPlus.HwndSource_PopupRoot.PopupRoot
  if dataGrid.TextblockDemoipCom.Exists: 
    aqObject.CheckProperty(dataGrid.TextblockDemoipCom, "WPFControlText", cmpEqual, serverName)
    dataGrid.ClickCellXY(0, "Server Name", 133, 16)  
  else:
    loginWindow.btnServerAdd.ClickButton()
    popupRoot.txtNewConnectionIPAddress.Click(47, 25)
    hwndSource.Keys(serverName)
    hwndSource.Keys(PortNumber)
    popupRoot.btnTestConnectionServer.ClickButton()
    aqObject.CheckProperty(popupRoot.txtNewServerName, "wText", cmpEqual, serverName)
    popupRoot.btnUpdateConnectionServer.ClickButton()  
  
  loginWindow.btnLogIn.ClickButton()
  hwndSource = VIMonitorPlus.HwndSource_MainWindow
  mainWindow = hwndSource.MainWindow
  mainWindow.WindowButtonCommands.Click()
  
def closeTheApplication():
  VIMonitorPlus = Aliases.VIMonitorPlus
  hwndSource = VIMonitorPlus.HwndSource_LoginWindow
  loginWindow = hwndSource.LoginWindow   
  loginWindow.CloseButton.Click()