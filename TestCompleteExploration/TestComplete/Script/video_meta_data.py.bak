
def main():
  explorer = Aliases.explorer
  explorer.wndShell_TrayWnd.DesktopWindowXamlSource.Click(960, 59)
  HWNDView = explorer.wndDesktop.Desktop.DUIViewWndClassName.Explorer_Pane
  UIItemsView = HWNDView.CtrlNotifySink.ShellView.Items_View
  UIItemsView.VI_MonitorPLus.DblClick(29, 34)
    
  from os import sys
  sys.path.insert(0, "C:\\Program Files (x86)\\SmartBear\\TestComplete 15\\x64\\Bin\\Extensions\\Python\\Python38\\Lib\\site-packages")
  from moviepy.editor import VideoFileClip 
  clip = VideoFileClip("C:\\Users\\LENOVO\\Desktop\\VI MonitorPLus\\File217.avi")
  sTime = clip.duration
  clip.close()
  sTime = str(sTime)   
  if aqObject.CompareProperty(sTime, cmpGreater, 1, True):
    Log.CheckpoiUtility_Methodsnt(sTime+"is greater than expected time"+1)
  else:
    Log.Error(sTime+"is not greater than expected time"+str(Seconds))