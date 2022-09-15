import random
import smtplib
from datetime import datetime, timedelta
import json

def verifyVideoDuration(filePath,Seconds):
  from os import sys
  sys.path.insert(0, "C:\\Program Files (x86)\\SmartBear\\TestComplete 15\\x64\\Bin\\Extensions\\Python\\Python38\\Lib\\site-packages")
  from moviepy.editor import VideoFileClip 
  clip = VideoFileClip(filePath)
  sTime = clip.duration
  clip.close()
  sTime = str(sTime)   
  if aqObject.CompareProperty(sTime, cmpGreater, Seconds, True):
    Log.CheckpoiUtility_Methodsnt(sTime+"is greater than expected time"+str(Seconds))
  else:
    Log.Error(sTime+"is not greater than expected time"+str(Seconds))
    
def ReadDataFromExcel():
  Excel = Sys.OleObject["Excel.Application"]
  Excel.Workbooks.Open("C:\\MyFile.xlsx")

  RowCount = Excel.ActiveSheet.UsedRange.Rows.Count
  ColumnCount = Excel.ActiveSheet.UsedRange.Columns.Count

  for i in range(1, RowCount + 1):
    s = "";
    for j in range(1, ColumnCount + 1):
      s = s + VarToString(Excel.Cells.Item[i, j]) + '\r\n'
    Log.Message("Row: " + VarToString(i), s);

  Excel.Quit();
  
def ReadDataFromJson(parameter1,parameter2):
   f = open('C:\\Users\\LENOVO\\Desktop\\Ipro\\Test Data.json')
   data = json.loads(f.read())
   result = data[parameter1][parameter2]
   return result  
   
def ReadDataFromINIFIle(section,option):
    ini = Storages.INI("C:\\Users\\LENOVO\\Desktop\\Ipro\\TestData.ini")
  
    # Reads the Type value from the Settings section 
    value = ini.GetSubSection(section).GetOption(option,"")
    Log.Message(value)
    return value

def AddDataIntoINIFile(new_subsection_name,new_option_name,option_value):
     w = Storages.INI("D:\MyFile.ini")
     Section = w.GetSubSection(new_subsection_name)
     Section.SetOption(new_option_name, option_value)
     w.Save()

def read_data_from_excel(row_value_count):
  excelFile = Excel.Open("C:\\Users\\LENOVO\\Desktop\\Ipro\\Test Data.xlsx")
  excelSheet = excelFile.SheetByTitle["Sheet1"]
  
  valueB = excelSheet.Cell[1, 3].Value
  row_number = 2
  #row_value_count = 9
  list = []
  for i in range(1,row_value_count):
     if(excelSheet.Cell[i, row_number].Value == None):
        break
     else:
        Log.Message(excelSheet.Cell[i, row_number].Value)
        element = excelSheet.Cell[i, row_number].Value
        list.append(element)
  Log.Message(len(list))
  return list

def excel_filled_row_value_count():
    excelFile = Excel.Open("C:\\Users\\LENOVO\\Desktop\\Ipro\\Test Data.xlsx")
    excelSheet = excelFile.SheetByTitle["Sheet1"]
    row_number = 2
    row_value_count = 0
    list = []
    i = 1
    j = 1
    while(excelSheet.Cell[j, row_number].Value != None):
          j = j + 1
          row_value_count = row_value_count  + 1
    Log.Message(len(list))
    Log.Message(row_value_count)
    return row_value_count

def DataDriven():
  DDT.ExcelDriver("C:\\Users\\LENOVO\\Desktop\\Ipro\\Test Data.xlsx", "Sheet1") 
  while not DDT.CurrentDriver.EOL():
    Log.Message(DDT.CurrentDriver.Value[1]) 
    DDT.CurrentDriver.Next()
  DDT.CloseDriver(DDT.CurrentDriver.Name)
  
def wait_until_object_is_visible(parent_name,child_name,duration,error_message):
  try:
    if (parent_name.WaitAliasChild(child_name, duration).Visible,error_message): 
       Log.Message("The Wpf element is visible on screen")
  except Exception as e:
       Log.Message(error_message)
   