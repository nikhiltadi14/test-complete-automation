import time
import random
import Login_Window, Home_Window, Workspace_Window, ExportVideoClip_Window, Utility_Methods
from datetime import datetime, timedelta
from os import sys

def ExportMultiplexClipping():
  Login_Window.launchVIMonitorPlusApplication()
  Login_Window.loginInToApplication(Project.Variables.AdminUsername,Project.Variables.Password.DecryptedValue,Project.Variables.ConnectionType,Project.Variables.ServerName,Project.Variables.ServerPort)
  Home_Window.verifyThatSpecifiedUserIsLoggedInCorrectly("Administrator")
  Home_Window.waitForCamerasToLoadInLeftTreeView()
  Workspace_Window.clickOn4CamerasViewButton()
  ''''
  Workspace_Window.verifyThat4CamerasViewWithBlankPannelsIsDisplayed()
  Workspace_Window.dragCamerasFromTreeviewToWorkSpace()  
  Workspace_Window.verifyThat4LiveVideosAreStreaming()  
  Workspace_Window.clickOnSwitchToRecordedVideoButton()  
  Workspace_Window.verifyThat4PannelsAreDisplayedInRecordedVideoMode()
  Workspace_Window.clickOnExportRecordedVideoButton()  
  now = datetime.now() - timedelta(days=0, hours=0, minutes=20)
  startDate = now.strftime("%d-%m-%Y %H:%M:%S")
  now = datetime.now() - timedelta(days=0, hours=0, minutes=19)
  endDate = now.strftime("%d-%m-%Y %H:%M:%S")
  ExportVideoClip_Window.enterStartAndEndDateDetailsInExportVideoClipPopup(startDate,endDate)  
  ExportVideoClip_Window.selectCombineIntoSingleFileCameraOption()
  Path = Project.Path
  Path = Path + "ExportedVideos"
  fileName = "V"+str(random.randint(0,5000))+".avi"
  ExportVideoClip_Window.enterFileOptionsDetailsInExportVideoClipPopup(Path,fileName)  
  ExportVideoClip_Window.selectAllExportOptionsInExportVideoClipPopup()
  ExportVideoClip_Window.clickOnExportButton()
  ExportVideoClip_Window.waitUntilVideoFileIsDownloaded()
  ExportVideoClip_Window.closeTheExportDownloadWindow()
  Home_Window.logOutOfTheApplication()
  Login_Window.closeTheApplication()
  fPath = Path+"\\"+fileName
  Utility_Methods.verifyVideoDuration(fPath,50)
  '''
