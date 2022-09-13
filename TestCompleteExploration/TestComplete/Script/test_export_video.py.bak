from drag_and_drop_camera_page import *
from export_video_page import *
from utility_method import *
import random
import smtplib
from datetime import datetime, timedelta

def TestExportMultiplex():
  launch_application()
  verify_signin_page_is_displayed()
  login_into_application(Project.Variables.Username,Project.Variables.Password)
  verify_user_successfully_logged_into_account()
  wait_for_the_cameras_to_load()
  verify_2_camera_panel_is_displayed()
  click_on_2_camera_panel()
  verify_2_camera_panel_is_blank()
  drag_and_drop_camera()
  verify_videos_are_streaming_live()
  clickOnExportRecordedVideoButton()  
  now = datetime.now() - timedelta(days=0, hours=0, minutes=20)
  startDate = now.strftime("%m/%d/%Y %H:%M:%S %p")
  now = datetime.now() - timedelta(days=0, hours=0, minutes=19)
  endDate = now.strftime("%m/%d/%Y %H:%M:%S %p")
  enterStartAndEndDateDetailsInExportVideoClipPopup(startDate,endDate)  
  selectCombineIntoSingleFileCameraOption()
  Path = Project.Path
  Path = Path + "ExportedVideos"
  fileName = "V"+str(random.randint(0,5000))+".avi"
  enterFileOptionsDetailsInExportVideoClipPopup(Path,fileName)  
  selectAllExportOptionsInExportVideoClipPopup()
  clickOnExportButton()
  waitUntilVideoFileIsDownloaded()
  closeTheExportDownloadWindow()
  logout_from_application()
  close_application()
  fPath = Path+"\\"+fileName
  utility_method.verifyVideoDuration(fPath,50)