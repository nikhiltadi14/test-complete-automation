from drag_and_drop_camera_page import * 
import re
  
def Main():
  launch_application()
  verify_signin_page_is_displayed()
  login_into_application(Project.Variables.Username,Project.Variables.Password)
  verify_user_successfully_logged_into_account()
  wait_for_the_cameras_to_load()
  
  
  # CLick on 2 camera Panel and get streaming camera count
  ''''
  hwndSource = Aliases.VIMonitorPlus.HwndSource_MainWindow
  mainWindow = hwndSource.MainWindow
  mainWindow.tabWorkspaces.Camera4.ClickButton()
  treeViewItem = mainWindow.treeServers.TreeviewitemDemoipCom
  treeViewItem.TreeviewitemParkingCameraH265.Drag(121, 8, 558, 65)
  treeViewItem.TreeviewitemTrainCameraH264.Drag(65, 13, 1515, 106)
  treeViewItem.TreeviewitemWvU1142H265.Drag(118, 20, 867, 575)
  #hwndSource.WinFormsAdapter.VideoContainer.pnlBackground_6950726765843833856_0_17500462890428936937.DragM(730, 352, 17, -15)
  treeViewItem.TreeviewitemSncEm641.Drag(132, 11, 1653, 492)
  
  videoContainer = Aliases.VIMonitorPlus.HwndSource_MainWindow.WinFormsAdapter.VideoContainer
  varray  = videoContainer.FindAll("WinFormsControlName","*Display*",2,True)
  Log.Message(len(varray))
  '''
  
  # Find child elements
  mainWindow = Aliases.VIMonitorPlus2.HwndSource_MainWindow.MainWindow.treeServers.TreeviewitemDemoipCom
  varray  = mainWindow.Find("WPFControlText","demoip.com",2,True)
  #Log.Message(len(varray))
  treeCamera = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.expCameras
  click_element = treeCamera.Find("WPFControlName","expCameras",2,True)
  click_element.click()
  close_application()
 