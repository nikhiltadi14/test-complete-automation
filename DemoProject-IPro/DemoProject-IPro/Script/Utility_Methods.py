def verifyVideoDuration(filePath,Seconds):
  from os import sys
  sys.path.insert(0, "C:\\Program Files (x86)\\SmartBear\\TestComplete 15\\x64\\Bin\\Extensions\\Python\\Python38\\Lib\\site-packages")
  from moviepy.editor import VideoFileClip 
  clip = VideoFileClip(filePath)
  sTime = clip.duration
  clip.close()
  sTime = str(sTime)   
  if aqObject.CompareProperty(sTime, cmpGreater, Seconds, True):
    Log.Checkpoint(sTime+"is greater than expected time"+str(Seconds))
  else:
    Log.Error(sTime+"is not greater than expected time"+str(Seconds))
   