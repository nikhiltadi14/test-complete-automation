﻿def verify_1_camera_panel_is_displayed():
  tabControl = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces
  button = tabControl.StackPanel2.Button
  aqObject.CheckProperty(button.Textblock1Camera, "WPFControlText", cmpEqual, "1 Camera")

def click_on_1_camera_panel_button():
  tabControl = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces
  button = tabControl.StackPanel2.Button
  button.ClickButton() 
  
def select_camera_view_layout():
  comboBox = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.cboLayoutType
  comboBox.DropDown()
  comboBox.ClickItem(6)
  
def get_layout_type_header_text():
  #tabControl = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.TabitemCameraView
  #text = tabControl.WPFControlText
  ComboBox = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.cboLayoutType
  #cb = ComboBox.Window("ComboBox", "", 6)
  ComboBox.DropDown()
  ComboBox.ClickItem(6)
  
  # Obtain the selected item by its index
  ItemIndex = ComboBox.wSelectedItem
  Log.Message(ItemIndex)
  SelItem = ComboBox.wItem[ItemIndex]
  Log.Message(SelItem)
    
  # Obtain the selected item's text via the wText property
  Sys.Clipboard = ComboBox.wText
  Log.Message(Sys.Clipboard)
  
  ''''
  sub_string = text[0:1:1]
  Log.Message(sub_string)
  return sub_string
  '''

def verify_layout_count_matches_with_blank_camera_count(sub_string):
  VideoContainer = Aliases.VIMonitorPlus.HwndSource_MainWindow.WinFormsAdapter.VideoContainer
  camera_count = VideoContainer.ChildCount
  aqObject.CompareProperty(sub_string, cmpEqual, camera_count, True)
  
def select_stack_pane_camera_panel():
  list_camera_view = []
  tabControl = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces
  
  list_camera_view = ['Textblock1Camera','Textblock2Cameras','Button.Textblock4Cameras','Button3.Textblock8Cameras','Button4.Textblock9Cameras','Textblock10Cameras','Textblock13Cameras',
  'Textblock13Cameras2','Textblock16Cameras','Textblock19Cameras','Textblock25Cameras','Textblock18CamerasWide','Textblock24CamerasWide']
  Log.Message(list_camera_view[7])
  
  #Storing List element in new variable
  button = list_camera_view[7]
  b = eval(button)
  camera_panel_click = tabControl.b
  
  text = aqObject.GetPropertyValue(camera_panel_click, "WPFControlText")
  Log.Message(text)
  text = aqObject.GetPropertyValue(tabControl.Textblock13Cameras2, "WPFControlText")
  Log.Message(text)
  
  #Click on camera 
  camera_panel_click.click()
  
  ''''
  CameraViewHeader = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.TabitemCameraView
  text = aqObject.GetPropertyValue(CameraViewHeader, "WPFControlText")
  Log.Message(text)
  sub_string = text[0:1:1]
  Log.Message(sub_string)
  return sub_string
  '''

def select_stack_pane_camera_panel_v2():
  list_camera_view = []
  list_camera_view_header = []
  tabControl = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces
  
  list_camera_view = ['Textblock1Camera','Textblock2Cameras','Button.Textblock4Cameras','Button3.Textblock8Cameras','Button4.Textblock9Cameras','Textblock10Cameras','Textblock13Cameras',
  'Textblock13Cameras2','Textblock16Cameras','Textblock19Cameras','Textblock25Cameras','Textblock18CamerasWide','Textblock24CamerasWide']
  Log.Message(list_camera_view[5])
  
  #Storing List element in new variable
  button = list_camera_view[5]
  camera_panel_click1 = tabControl.button
  camera_panel_click1.click()
   
  ''''
  tabControl = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces
  list_camera_view_header = ['Tabitem1Camera','Tabitem2Cameras','Tabitem4Cameras','Tabitem8Cameras','Tabitem9Cameras','Textblock10Cameras','Textblock13Cameras',
  'tabControl.Tabitem13CameraView','Tabitem16Cameras','Tabitem19Cameras','Tabitem25Cameras','Tabitem18CamerasWide','Tabitem24CamerasWide']
  

   
  text = aqObject.GetPropertyValue(tabControl.Tabitem10CameraView, "WPFControlText")
  Log.Message(text)
  
  Log.Message(text)
  sub_string = text[0:1:1]
  Log.Message(sub_string)
  return sub_string
  
'''

  
  