import imp
import string
from tracemalloc import start
from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con
import math



#click code
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

print("system is online")

#inputs
start_value=int(input("Start Value:"))
end_value=int(input("End Value:"))
collection_name=input("Collection Name:")
price=float(input("Price(It is only ETH right now new coins are coming soon):"))


while start_value<end_value :
    print(collection_name + "_" + str(start_value) + " is creating...")
    #open OpenSea and go to your profile
    time.sleep(2)
       #create
    click(1752,95)
    time.sleep(3)
        #upload image
    click(848,400)
    time.sleep(1)
        #search the image
    click(276,762)
    time.sleep(0.1)
        #type the name
    pyautogui.write(str(start_value))
    time.sleep(0.5)
        #item select
    click(1370,790)
    time.sleep(0.3)
        #item name write  
    click(726,568)
    time.sleep(0.3)
    pyautogui.write(collection_name+ "_" +str(start_value))
    time.sleep(0.3)
#collection
    click(783,965)
    time.sleep(0.5)
    pyautogui.keyDown('pagedown')
    pyautogui.keyUp('pagedown')
    time.sleep(0.6)
    click(817,235)
    time.sleep(0.1)
    #blockchain
    click(835,723)
    time.sleep(0.5)
    click(828,771)
    #create
    time.sleep(0.5)
    click(751,967)
    #robot test
    time.sleep(5)
    click(857,309)
    time.sleep(7)
    #robot test solver crhome
    click(978,520)
    time.sleep(10)
    #sell
    click(1151,191)
    time.sleep(0.2)
    click(1372,154)
    time.sleep(3)
    #price set
    click(390,391)
    time.sleep(0.2)
    keyboard.write(str(price))
    time.sleep(0.5)
    #duration
    click(315,495)
    time.sleep(0.5)
    click(301,595)
    time.sleep(0.5)
    click(274,846)
    time.sleep(0.5)
    click(98,624)
    time.sleep(0.5)
    #complete listing
    click(243,722)
    #metamask
    time.sleep(10)
    click(1701,471)
    time.sleep(0.1)
    pyautogui.keyDown('pagedown')
    pyautogui.keyUp('pagedown')
    time.sleep(0.1)
    pyautogui.keyDown('pagedown')
    pyautogui.keyUp('pagedown')
    time.sleep(0.1)
    pyautogui.keyDown('pagedown')
    pyautogui.keyUp('pagedown') 
    time.sleep(0.2)
    click(1808,556)       
    time.sleep(5)
    click(1209,189)
    print(collection_name + "_" + str(start_value) + " is created.")
    time.sleep(5)
    start_value += 1          

print = str(end_value - start_value) + " NFT are created."
time.sleep(2)
print="OpenSea Upload Bot made by YagizWasTaken"