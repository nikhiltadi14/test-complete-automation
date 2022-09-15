import time
import random
from datetime import datetime, timedelta
from os import sys



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
  mainWindow.tabWorkspaces.Button.ClickButton()
  
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.Tabitem4CameraView, "Enabled", cmpEqual, True)
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.Tabitem4CameraView, "Header", cmpEqual, "4 Camera View")
  
  videoContainerObj = hwndSource.WinFormsAdapter.VideoContainer
  aqObject.CheckProperty(videoContainerObj,"ChildCount", cmpEqual, 4, True)
  
  for i in range ( 0 , videoContainerObj.ChildCount):
      vChild = videoContainerObj.Child(i)
      Log.Message(vChild.Name, "", 0)
      aqObject.CheckProperty(vChild,"Name", cmpContains, "pnlBackground", True)  
  
  treeViewItem.TreeviewitemParkingCameraH265.Drag(94, 14, 466, 56)
  treeViewItem.TreeviewitemTrainCameraH264.Drag(102, 14, 1275, 32)
  treeViewItem2 = treeViewItem.TreeviewitemSncEm641
  treeViewItem2.Drag(67, 17, 487, 385)
  treeViewItem.TreeviewitemWvS4150H265.ClickR()
  popupRoot.Decorator.NonLogicalAdornerDecorator.ContextMenu.MenuitemAddToCurrentWorkspace.Click()
  time.sleep(10)
  
  videoContainerObj = hwndSource.WinFormsAdapter.VideoContainer
  varray = videoContainerObj.FindAll("WinFormsControlName","*DisplayCtrl*",2,True)
  if aqObject.CompareProperty(len(varray),cmpEqual, 4, True):
    Log.Checkpoint("All 4 live videos are displayed correctly")
  else:
    Log.Warning("Some live videos are not loading, please check")
  Log.Message(len(varray), "", 0)
      
  mainWindow.tabWorkspaces.playbackModeButton.ClickButton()
  
  aqObject.CheckProperty(popupRoot.Decorator.NonLogicalAdornerDecorator.txtDisplayTime, "WPFControlText", cmpContains, datetime.now().strftime("%A, %B %d %H:%M:%S"))
  videoContainerObj = hwndSource.WinFormsAdapter.VideoContainer
  aqObject.CheckProperty(videoContainerObj,"ChildCount", cmpEqual, 4, True)
  
  
  mainWindow.tabWorkspaces.btnExportVideoClip.ClickButton()
  
  
  now = datetime.now() - timedelta(days=0, hours=0, minutes=20)
  startDate = now.strftime("%d-%m-%Y %H:%M:%S")
  now = datetime.now() - timedelta(days=0, hours=0, minutes=19)
  endDate = now.strftime("%d-%m-%Y %H:%M:%S")
  exportWindow = VIMonitorPlus.HwndSource_ExportMultiplexVideo.ExportMultiplexVideo
  exportWindow.wtmTxtStartDateTime.set_Text(startDate)
  aqObject.CheckProperty(exportWindow.wtmTxtStartDateTime, "Text", cmpEqual, startDate)
  exportWindow.wtmTxtEndDateTime.set_Text(endDate)
  aqObject.CheckProperty(exportWindow.wtmTxtEndDateTime, "Text", cmpEqual, endDate)
  exportWindow.combineRadioButton.Click()
  aqObject.CheckProperty(exportWindow.combineRadioButton, "wChecked", cmpEqual, True)
  exportWindow.ComboboxExportTo.ClickItem(0)
  exportWindow.Button.ClickButton()  
  dlgBrowseForFolder = VIMonitorPlus.dlgBrowseForFolder
  Path = Project.Path
  Path = Path + "ExportedVideos"
  fileName = "V"+str(random.randint(0,5000))+".avi"
  
  progress = VIMonitorPlus.dlgBrowseForFolder.WorkerW.ReBarWindow32.AddressBandRoot.progress
  progress.BreadcrumbParent.toolbar.Click(311, 18)
  progress.comboBox.SetText(Path)
  progress.comboBox.Keys("[Enter]")
  #progress.toolbarAddressBandToolbar.ClickItem(100, False) 
  
  comboBox = dlgBrowseForFolder.DUIViewWndClassName.Explorer_Pane.FloatNotifySink.ComboBox
  comboBox.SetText(fileName)
  dlgBrowseForFolder.btnSave.ClickButton()
  exportWindow.CheckboxIncludeAudioIfAvailable.ClickButton(cbChecked)
  
  aqObject.CheckProperty(exportWindow.ComboboxExportTo, "SelectedValue", cmpEqual, "AVI")
  aqObject.CheckProperty(exportWindow.txtClipFilename, "wText", cmpEqual, Path+"\\"+fileName)
  aqObject.CheckProperty(exportWindow.CheckboxIncludeAudioIfAvailable, "IsChecked", cmpEqual, True)
  
  
  exportWindow.chkShowTimestamp.ClickButton(cbChecked)
  exportWindow.chkIncludeWatermark.ClickButton(cbChecked)
  exportWindow.chkForceJPEG.ClickButton(cbChecked)
  aqObject.CheckProperty(exportWindow.chkShowTimestamp, "IsChecked", cmpEqual, True)
  aqObject.CheckProperty(exportWindow.chkIncludeWatermark, "IsChecked", cmpEqual, True)
  aqObject.CheckProperty(exportWindow.chkForceJPEG, "IsChecked", cmpEqual, True)
  exportWindow.btnExport.ClickButton()
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_PopupRoot.PopupRoot.Decorator.NonLogicalAdornerDecorator.ListView.ListViewItem, "Enabled", cmpEqual, True)
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_PopupRoot.PopupRoot.Decorator.NonLogicalAdornerDecorator.ListView.ListViewItem, "Exists", cmpEqual, True) 
  
  for x in range(5):
    text = OCR.Recognize(Aliases.VIMonitorPlus.HwndSource_PopupRoot.PopupRoot.Decorator.NonLogicalAdornerDecorator.ListView.ListViewItem).FullText    
    if aqString.Find(text, "Download Complete", 0 , False) > -1: break
    else:
      time.sleep(60)
      
  OCR.Recognize(Aliases.VIMonitorPlus.HwndSource_PopupRoot.PopupRoot.Decorator.NonLogicalAdornerDecorator.ListView.ListViewItem).CheckText("*Download Complete*")
  
  closeButtonImg = Aliases.VIMonitorPlus.HwndSource_PopupRoot.PopupRoot.Decorator.NonLogicalAdornerDecorator.Image
  closeButtonImg.Click()
  
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  button = mainWindow.WindowCommands.UserPB
  button.ClickButton()
  button.PopupMenu.Click("Log Out")
  
  hwndSource = VIMonitorPlus.HwndSource_LoginWindow
  loginWindow = hwndSource.LoginWindow   
  loginWindow.CloseButton.Click()
  
  #time.sleep(300) 
  sys.path.insert(0, "C:\\Program Files (x86)\\SmartBear\\TestComplete 15\\x64\\Bin\\Extensions\\Python\\Python38\\Lib\\site-packages")
  from moviepy.editor import VideoFileClip 
  clip = VideoFileClip(Path+"\\"+fileName)
  sTime = clip.duration
  clip.close()
  aqObject.CompareProperty(sTime, cmpGreater, 50, True)
  sTime = str(sTime)   
  print( sTime )
  Log.Message("duration:"+sTime)
  
  clip.close()
  
  
  
  
  
  
  
  

  
