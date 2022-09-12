def click_on_filter_option():
  VIMonitorPlus = Aliases.VIMonitorPlus
  expander = VIMonitorPlus.HwndSource_MainWindow.MainWindow.expSearch
  expander.Click(216, 24)
  expander.Click(216, 24)

def verify_filter_option_is_displayed():
  VIMonitorPlus = Aliases.VIMonitorPlus
  aqObject.CheckProperty(VIMonitorPlus.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator, "IsVisible", cmpEqual, True)

def search_for_server(server_name):
  expander = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.expSearch
  expander.Expand()
  aqObject.CheckProperty(expander, "WPFControlText", cmpEqual, "Search")
  expander.Keys(server_name)
  
def verify_search_server_name_is_displayed(server_name):
  expander = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.expSearch
  treeView = expander.treeSearch
  aqObject.CheckProperty(treeView.TreeviewitemPocView1.TextblockPocView1, "WPFControlText", cmpEqual, server_name)
  treeView.ClickItem("|[0]")