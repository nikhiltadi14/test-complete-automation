def verify_servers_section_are_displayed():
  MainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  TreeViewItem = MainWindow.treeServers.TreeviewitemDemoipCom
  aqObject.CheckProperty(TreeViewItem, "ClrClassName", cmpEqual, "TreeViewItem")
  aqObject.CheckProperty(TreeViewItem.TextblockDemoipCom, "WPFControlText", cmpEqual, "demoip.com")
  
def click_on_camera_section():
    mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
    expander = mainWindow.expCameras
    expander.Expand()

def verify_camera_section_is_displayed():
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  expander = mainWindow.expCameras
  aqObject.CheckProperty(expander.treeCameras, "IsVisible", cmpEqual, True)

def click_on_view_section():
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  expander = mainWindow.expLayouts
  expander.Expand()
  expander.treeLayouts.ClickItem("|[0]")

def verify_view_section_is_displayed():
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  tabControl = mainWindow.tabWorkspaces
  aqObject.CheckProperty(tabControl.TabitemPocView1, "WPFControlText", cmpEqual, "POC_View1")

def click_on_map_section():
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  expander = mainWindow.expMaps
  expander.Expand()
  expander.treeMaps.ClickItem("|[0]")

def verify_map_section_is_displayed():
  mainWindow = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow
  tabControl = mainWindow.tabWorkspaces
  aqObject.CheckProperty(tabControl.imgMap, "IsVisible", cmpEqual, True)
