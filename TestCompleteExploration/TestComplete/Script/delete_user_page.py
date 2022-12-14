def switch_to_security_setup_group_section():
  VIMonitorPlus = Aliases.VIMonitorPlus
  menu = VIMonitorPlus.HwndSource_MainWindow.MainWindow.mnuMain
  aqObject.CheckProperty(menu.mnuAdministration, "WPFControlText", cmpEqual, "Administration")
  menu.WPFMenu.Click("Administration|Users & Groups|Setup and Configuration")
  securitySetup = VIMonitorPlus.HwndSource_SecuritySetup.SecuritySetup
  #aqObject.CheckProperty(securitySetup.expUsers, "Visible", cmpEqual, True)

def verify_security_setup_is_displayed():
  setup = Aliases.VIMonitorPlus.HwndSource_SecuritySetup.SecuritySetup
  #System.Windows.Controls.TabControl
  setup.WaitWPFObject("System.Windows.Controls.TabControl", "", 6000)
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_SecuritySetup.SecuritySetup, "WPFControlText", cmpEqual, "Security Setup")
  
def get_user():
  securitySetup = Aliases.VIMonitorPlus.HwndSource_SecuritySetup.SecuritySetup
  treeView = securitySetup.treeUsers
  username = []
  num_list = []
  count = treeView.ChildCount
  Log.Message(treeView.Child(10).WPFControlText)
  element = treeView.Child(26).WPFControlText
  Log.Message(element)
 
def delete_a_user(username):
  VIMonitorPlus = Aliases.VIMonitorPlus
  hwndSource = VIMonitorPlus.HwndSource_SecuritySetup
  expander = hwndSource.SecuritySetup.expSearch
  expander.Expand()
  expander.Keys(username)
  treeView = expander.treeSearch
  treeViewItem = treeView.UserNameDelete
  stackPanel = treeViewItem.StackPanel
  treeViewItem.ClickR(163, 24)
  Aliases.VIMonitorPlus.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuitemDeleteUser.click()
  VIMonitorPlus.MessageBoxVI.VIMessageBox_Fill_Panel.UltraPanelClientAreaUnsafe.pnlTop.TableLayoutPanel1.btnYes.ClickButton()
  
def verify_user_removed_successfully(username):
  VIMonitorPlus = Aliases.VIMonitorPlus
  hwndSource = VIMonitorPlus.HwndSource_SecuritySetup
  expander = hwndSource.SecuritySetup.expSearch
  expander.Expand()
  expander.Keys(username)
  treesearch = expander.treeSearch
  aqObject(treesearch.UserNameDelete,'Visisble','False')
 # if not treesearch.UserNameDelete.Exists:
 #   Log.Message('User Deleted')
 # else:
 #   Log.Message("User not deleted")
  
  