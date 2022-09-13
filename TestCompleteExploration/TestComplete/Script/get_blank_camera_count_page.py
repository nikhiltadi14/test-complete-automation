﻿def verify_25_camera_panel_is_displayed():
  button = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.StackPanel2.Button2
  aqObject.CheckProperty(button, "IsVisible", cmpEqual, True)

def click_on_25_camera_panel():
  button = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.StackPanel2.Button2
  button.ClickButton()

def get_total_blank_camera_count():
  VideoContainer = Aliases.VIMonitorPlus.HwndSource_MainWindow.WinFormsAdapter.VideoContainer
  Log.Message(VideoContainer.ChildCount)
  