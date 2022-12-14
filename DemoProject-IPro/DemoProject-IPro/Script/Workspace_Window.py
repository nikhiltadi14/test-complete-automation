def clickOn4CamerasViewButton():
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  mainWindow.tabWorkspaces.Button.ClickButton()
  
def verifyThat4CamerasViewWithBlankPannelsIsDisplayed():
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.Tabitem4CameraView, "Enabled", cmpEqual, True)
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.Tabitem4CameraView, "Header", cmpEqual, "4 Camera View")
  hwndSource = Aliases.VIMonitorPlus.HwndSource_MainWindow
  videoContainerObj = hwndSource.WinFormsAdapter.VideoContainer
  aqObject.CheckProperty(videoContainerObj,"ChildCount", cmpEqual, 4, True)
  
  for i in range ( 0 , videoContainerObj.ChildCount):
      vChild = videoContainerObj.Child(i)
      Log.Message(vChild.Name, "", 0)
      aqObject.CheckProperty(vChild,"Name", cmpContains, "pnlBackground", True)
      
def dragCamerasFromTreeviewToWorkSpace():
  treeViewItem = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.treeServers.TreeviewitemDemoipCom
  popupRoot = Aliases.VIMonitorPlus.HwndSource_PopupRoot.PopupRoot
  treeViewItem.TreeviewitemParkingCameraH265.Drag(94, 14, 466, 56)
  treeViewItem.TreeviewitemTrainCameraH264.Drag(102, 14, 1275, 32)
  treeViewItem2 = treeViewItem.TreeviewitemSncEm641
  treeViewItem2.Drag(67, 17, 487, 385)
  treeViewItem.TreeviewitemWvS4150H265.ClickR()
  popupRoot.Decorator.NonLogicalAdornerDecorator.ContextMenu.MenuitemAddToCurrentWorkspace.Click()
  import time
  time.sleep(10)
  
def verifyThat4LiveVideosAreStreaming():
  hwndSource = Aliases.VIMonitorPlus.HwndSource_MainWindow
  videoContainerObj = hwndSource.WinFormsAdapter.VideoContainer
  varray = videoContainerObj.FindAll("WinFormsControlName","*DisplayCtrl*",2,True)
  if aqObject.CompareProperty(len(varray),cmpEqual, 4, True):
    Log.Checkpoint("All 4 live videos are displayed correctly")
  else:
    Log.Warning("Some live videos are not loading, please check")
  Log.Message(len(varray), "", 0)
  
def clickOnSwitchToRecordedVideoButton():
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  mainWindow.tabWorkspaces.playbackModeButton.ClickButton()
  
def verifyThat4PannelsAreDisplayedInRecordedVideoMode():
  from datetime import datetime
  popupRoot = Aliases.VIMonitorPlus.HwndSource_PopupRoot.PopupRoot
  hwndSource = Aliases.VIMonitorPlus.HwndSource_MainWindow
  videoContainerObj = hwndSource.WinFormsAdapter.VideoContainer
  #aqObject.CheckProperty(popupRoot.Decorator.NonLogicalAdornerDecorator.txtDisplayTime, "WPFControlText", cmpContains, datetime.now().strftime("%A, %B %d %H:%M:%S"))
  videoContainerObj = hwndSource.WinFormsAdapter.VideoContainer
  aqObject.CheckProperty(videoContainerObj,"ChildCount", cmpEqual, 4, True)
  
def clickOnExportRecordedVideoButton():
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  mainWindow.tabWorkspaces.btnExportVideoClip.ClickButton()