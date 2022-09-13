def enterStartAndEndDateDetailsInExportVideoClipPopup(startDate, endDate):  
  VIMonitorPlus = Aliases.VIMonitorPlus2
  VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.btnExportVideoClip.ClickButton()
  exportMultiplexVideo = VIMonitorPlus.HwndSource_ExportMultiplexVideo.ExportMultiplexVideo
  exportMultiplexVideo.wtmTxtStartDateTime.set_Text(startDate)
  aqObject.CheckProperty(exportMultiplexVideo.wtmTxtStartDateTime, "Text", cmpEqual, startDate)
  exportMultiplexVideo.wtmTxtEndDateTime.set_Text(endDate)
  aqObject.CheckProperty(exportMultiplexVideo.wtmTxtEndDateTime, "Text", cmpEqual, endDate)  

def selectCombineIntoSingleFileCameraOption():
  exportWindow = Aliases.VIMonitorPlus.HwndSource_ExportMultiplexVideo.ExportMultiplexVideo
  exportWindow.combineRadioButton.Click()
  aqObject.CheckProperty(exportWindow.combineRadioButton, "wChecked", cmpEqual, True) 
  
def enterFileOptionsDetailsInExportVideoClipPopup(fPath, fileName):  
  exportWindow = Aliases.VIMonitorPlus.HwndSource_ExportMultiplexVideo.ExportMultiplexVideo  
  exportWindow.ComboboxExportTo.ClickItem(0)
  exportWindow.Button.ClickButton()  
  dlgBrowseForFolder = Aliases.VIMonitorPlus.dlgBrowseForFolder  
  progress = Aliases.VIMonitorPlus.dlgBrowseForFolder.WorkerW.ReBarWindow32.AddressBandRoot.progress
  progress.BreadcrumbParent.toolbar.Click(311, 18)
  progress.comboBox.SetText(fPath)
  progress.comboBox.Keys("[Enter]")
  #progress.toolbarAddressBandToolbar.ClickItem(100, False)  
  comboBox = dlgBrowseForFolder.DUIViewWndClassName.Explorer_Pane.FloatNotifySink.ComboBox
  comboBox.SetText(fileName)
  dlgBrowseForFolder.btnSave.ClickButton()
  exportWindow.CheckboxIncludeAudioIfAvailable.ClickButton(cbChecked)  
  aqObject.CheckProperty(exportWindow.ComboboxExportTo, "SelectedValue", cmpEqual, "AVI")
  aqObject.CheckProperty(exportWindow.txtClipFilename, "wText", cmpEqual, fPath+"\\"+fileName)
  aqObject.CheckProperty(exportWindow.CheckboxIncludeAudioIfAvailable, "IsChecked", cmpEqual, True)  
  
def selectAllExportOptionsInExportVideoClipPopup():  
  exportWindow = Aliases.VIMonitorPlus.HwndSource_ExportMultiplexVideo.ExportMultiplexVideo  
  exportWindow.chkShowTimestamp.ClickButton(cbChecked)
  exportWindow.chkIncludeWatermark.ClickButton(cbChecked)
  exportWindow.chkForceJPEG.ClickButton(cbChecked)
  aqObject.CheckProperty(exportWindow.chkShowTimestamp, "IsChecked", cmpEqual, True)
  aqObject.CheckProperty(exportWindow.chkIncludeWatermark, "IsChecked", cmpEqual, True)
  aqObject.CheckProperty(exportWindow.chkForceJPEG, "IsChecked", cmpEqual, True)
  
def clickOnExportButton():
  exportWindow = Aliases.VIMonitorPlus.HwndSource_ExportMultiplexVideo.ExportMultiplexVideo
  exportWindow.ExportButton.ClickButton()
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_PopupRoot.PopupRoot.Decorator.NonLogicalAdornerDecorator.ListView.ListViewItem, "Enabled", cmpEqual, True)
  aqObject.CheckProperty(Aliases.VIMonitorPlus.HwndSource_PopupRoot.PopupRoot.Decorator.NonLogicalAdornerDecorator.ListView.ListViewItem, "Exists", cmpEqual, True) 

def waitUntilVideoFileIsDownloaded():
  import time
  for x in range(10):
    text = OCR.Recognize(Aliases.VIMonitorPlus.HwndSource_PopupRoot.PopupRoot.Decorator.NonLogicalAdornerDecorator.ListView.ListViewItem).FullText    
    if aqString.Find(text, "Download Complete", 0 , False) > -1: break
    else:
      time.sleep(30)
      
  OCR.Recognize(Aliases.VIMonitorPlus.HwndSource_PopupRoot.PopupRoot.Decorator.NonLogicalAdornerDecorator.ListView.ListViewItem).CheckText("*Download Complete*")
  
def closeTheExportDownloadWindow():
  closeButtonImg = Aliases.VIMonitorPlus.HwndSource_PopupRoot.PopupRoot.Decorator.NonLogicalAdornerDecorator.Image
  closeButtonImg.Click()

def click_on_export_recorded_video_button():
  mainWindow = NameMapping.Sys.VIMonitorPlus.HwndSource_MainWindow.MainWindow.tabWorkspaces.playbackModeButton
  mainWindow.ClickButton()