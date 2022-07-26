# -*- coding: utf-8 -*-
import time,sys
from time import sleep
# a module which has functions related to time.
# It can be installed using cmd command:
# pip install time, in the same way as pyautogui.
import pyautogui
from subprocess import call
from os import environ, path, devnull, getcwd
from win32api import GetSystemMetrics
import codecs,os
from pywinauto import Application,mouse , keyboard
from PySide2.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import QObject, QUrl, Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

import platform
from PyQt5 import QtCore, QtGui, QtWidgets
import glob
import os.path
import clipboard
import ctypes

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False
pyautogui.size()
width, height = pyautogui.size()
pyautogui.position()

def killProgram(name):
    fnull = open(devnull, 'w')
    call(["taskkill","/f","/im",name], stdout=fnull, stderr=fnull)
    
def screenshot(filename, windowTitle):
    try:
        captureProgram = r"screenCapture.bat"
        call([captureProgram, filename,windowTitle])
    except:
        None

def getUpperDir():
    from os import sep
    dirArray = getcwd().split(sep)
    dirArray.pop()
    return sep.join(dirArray)

def cleanup():
    print("cleanup exist programs")
    killProgram("bit.exe")
    killProgram("h2testw.exe")
    killProgram("notepad.exe")
    mouse.click(coords=(GetSystemMetrics(0),GetSystemMetrics(1)))

def getTable(mainWindow):
    table = {}
    success = True
    listView =  mainWindow["#327701"].ListView
    colummTitle = listView.Columns()
    for index, item in enumerate(colummTitle):
        print(item["text"])
        item_count = listView.ItemCount()
        for tableIndex in range(0,item_count):
            print(listView.GetItem(tableIndex,index).text())
            if tableIndex not in table:
                table[tableIndex] = {}
            tableText = listView.GetItem(tableIndex,index).text()
            table[tableIndex][item["text"]] = tableText
            if index==4 and tableText != "No errors":
                print("error!!")
                success = False
        print("===>")
    return {"success":success,"table": table}

def cleanFile(filename):
    if path.exists(filename):
        from os import remove
        from shutil import rmtree
        if path.isfile(filename):
            remove(filename)
        else:
            rmtree(filename)

def get_clipboard_text():
    user32.OpenClipboard(0)
    try:
        if user32.IsClipboardFormatAvailable(CF_TEXT):
            data = user32.GetClipboardData(CF_TEXT)
            data_locked = kernel32.GlobalLock(data)
            text = ctypes.c_char_p(data_locked)
            value = text.value
            kernel32.GlobalUnlock(data_locked)
            return value
    finally:
        user32.CloseClipboard()

run_time = os.getenv('Test_Timing')
print('getenv run_time')
print(run_time)

logFile = path.join("C:\Jenkins-Report",'test.txt')
statusFile = path.join("C:\Jenkins-Report",'status.txt')

if(os.path.isfile("C:\Jenkins-Report\BurnInTest_result.log")):
    os.remove("C:\Jenkins-Report\BurnInTest_result.log")
    print("File Deleted successfully")
else:
    print("File does not exist")

if(os.path.isfile("C:\Jenkins-Report\BurnInTest_status.txt")):
    os.remove("C:\Jenkins-Report\BurnInTest_status.txt")
    print("File Deleted successfully")
else:
    print("File does not exist")

clear = lambda:os.system('cls')
clear()
cleanup()
TEST_PASS=False
cleanFile(logFile)
os.system('"echo Y|del D:\*"')
SET_Key1 = sys.argv[1] #Select Target
SET_Key2 = sys.argv[2] #Select Target
SET_Key3 = sys.argv[3] #Select Target
SET_Key4 = sys.argv[4] #Select Target
SET_Key5 = sys.argv[5] #Select Target
#----------------------------

fileList = glob.glob('C:\Jenkins\DownloadMicroCode\*_DLMC_log.txt')
for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath)
cleanFile(statusFile)
print("excute H2testw program")

app = Application(backend="win32").start(r"C:\\Jenkins\\H2TestDEFG\\h2testw.exe")
app.H2testw.MoveWindow(0, 0)

time.sleep(2)
pyautogui.click(93, 43) #select English
pyautogui.click(340, 85) #Select target

os.system('"C:\\Jenkins\\_Public\\nircmd cmdwait 1000 win setsize ititle "Browse For Folder" 0 0 120 250"')
time.sleep(1)

pyautogui.doubleClick(180, 220) #set Target
pyautogui.typewrite(SET_Key1)
pyautogui.doubleClick(180, 20) #select space point
time.sleep(1)
pyautogui.click(180, 255) #push OK button
pyautogui.click(33, 185) #Select DataVolume only
pyautogui.click(83, 185) #MB
pyautogui.typewrite(SET_Key5)

pyautogui.click(296, 234) #endless verify

pyautogui.click(80, 234) #Write+verify
pyautogui.click(350, 195) #Push OK
os.system('"C:\\Jenkins\\_Public\\nircmd cmdwait 1000 win setsize ititle "H2testw | Progress" 0 258 390 320"')
time.sleep(2)

##----------------------------------------------
app2 = Application(backend="win32").start(r"C:\\Jenkins\\H2TestDEFG\\h2testw.exe")
app2.H2testw.MoveWindow(100, 0)
time.sleep(2)
pyautogui.click(193, 43) #select English
pyautogui.click(440, 85) #Select target

os.system('"C:\\Jenkins\\_Public\\nircmd cmdwait 1000 win setsize ititle "Browse For Folder" 100 0 120 250"')
time.sleep(1)

pyautogui.doubleClick(280, 220) #set Target
pyautogui.typewrite(SET_Key2)
pyautogui.doubleClick(280, 20) #select space point
time.sleep(1)
pyautogui.click(280, 255) #push OK button
pyautogui.click(133, 185) #Select DataVolume only
pyautogui.click(183, 185) #MB
pyautogui.typewrite(SET_Key5)

pyautogui.click(396, 234) #endless verify

pyautogui.click(180, 234) #Write+verify
pyautogui.click(450, 195) #Push OK
os.system('"C:\\Jenkins\\_Public\\nircmd cmdwait 1000 win setsize ititle "H2testw | Progress" 100 258 390 320"')
time.sleep(2)

##----------------------------------------------
app3 = Application(backend="win32").start(r"C:\\Jenkins\\H2TestDEFG\\h2testw.exe")
app3.H2testw.MoveWindow(200, 0)

time.sleep(2)
pyautogui.click(293, 43) #select English
pyautogui.click(540, 85) #Select target

os.system('"C:\\Jenkins\\_Public\\nircmd cmdwait 1000 win setsize ititle "Browse For Folder" 200 0 120 250"')
time.sleep(1)

pyautogui.doubleClick(380, 220) #set Target
pyautogui.typewrite(SET_Key3)
pyautogui.doubleClick(380, 20) #select space point
time.sleep(1)
pyautogui.click(380, 255) #push OK button
pyautogui.click(233, 185) #Select DataVolume only
pyautogui.click(283, 185) #MB
pyautogui.typewrite(SET_Key5)

pyautogui.click(496, 234) #endless verify

pyautogui.click(280, 234) #Write+verify
pyautogui.click(550, 195) #Push OK
os.system('"C:\\Jenkins\\_Public\\nircmd cmdwait 1000 win setsize ititle "H2testw | Progress" 200 258 390 320"')
time.sleep(2)

##----------------------------------------------
app4 = Application(backend="win32").start(r"C:\\Jenkins\\H2TestDEFG\\h2testw.exe")
app4.H2testw.MoveWindow(300, 0)

time.sleep(2)
pyautogui.click(393, 43) #select English
pyautogui.click(640, 85) #Select target

os.system('"C:\\Jenkins\\_Public\\nircmd cmdwait 1000 win setsize ititle "Browse For Folder" 300 0 120 250"')
time.sleep(1)

pyautogui.doubleClick(480, 220) #set Target
pyautogui.typewrite(SET_Key4)
pyautogui.doubleClick(480, 20) #select space point
time.sleep(1)
pyautogui.click(480, 255) #push OK button
pyautogui.click(333, 185) #Select DataVolume only
pyautogui.click(383, 185) #MB
pyautogui.typewrite(SET_Key5)

pyautogui.click(596, 234) #endless verify

pyautogui.click(380, 234) #Write+verify
pyautogui.click(650, 195) #Push OK
os.system('"C:\\Jenkins\\_Public\\nircmd cmdwait 1000 win setsize ititle "H2testw | Progress" 300 258 390 320"')
time.sleep(2)
exit(0)




