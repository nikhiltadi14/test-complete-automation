def get_display_time():
  display_time = Aliases.VIMonitorPlus.HwndSource_PopupRoot2.PopupRoot.txtDisplayTime
  display_text = aqObject.GetPropertyValue(display_time, "WPFControlText")
  sliced_text = display_text[16:27]
  Log.Message(sliced_text)
  return sliced_text
  
def play_button_click():
  play_button = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.play_button
  play_button.click()
  
def backward_button_click():
  backward_button = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.btnStepBack
  backward_button.click()

def fast_backward_button_click():
  fast_backward_button = Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.playbackButtonsGrid.Button
  for i in range(3):
    fast_backward_button.click()
  aqUtils.Delay(7000)

def pause_button_click():
   pause_button=  Aliases.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.playbackButtonsGrid.btnPause
   pause_button.click()

def compare_time(current_time,rewind_time):
  aqObject.CompareProperty(current_time,cmpGreater,rewind_time)