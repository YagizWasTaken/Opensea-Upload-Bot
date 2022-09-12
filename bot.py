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
import tkinter as tk
from tkinter import*    

root=tk.Tk()
root.geometry("400x350+50+100")
root.title("OpenSea Upload BOT")

#click code
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

print("system is online")



def buttonclick12():
    start_value_int = start_value.get()
    end_value_int=end_value.get()
    price_int = price.get()
    colllection_name_int = collection_name.get()

    loop_number=int(end_value_int) + 1
    loop_total= int(start_value_int)
    while loop_number > loop_total :

        print(colllection_name_int + "_" + str(start_value_int) + " is creating...")
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
        pyautogui.write(str(start_value_int))
        time.sleep(0.5)
        #item select
        click(1370,790)
        time.sleep(1)
        #item name write  
        click(800,565)
        time.sleep(0.5)
        pyautogui.write(colllection_name_int+ "_" +str(start_value_int))
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
        click(797,828)
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
        keyboard.write(str(price_int))
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
        time.sleep(5)   
        loop_number += 1 


label = Label(root, text="Start Value:")
label.pack()
start_value=Entry(root,width=10)
start_value.pack()

label1 = Label(root, text="End Value:")
label1.pack()
end_value=Entry(root,width=10)
end_value.pack()

label2 = Label(root, text="Collection Name:")
label2.pack()
collection_name=Entry(root,width=10)
collection_name.pack()

label3 = Label(root, text="Price:")
label3.pack()
price=Entry(root,width=10)
price.pack()


button=Button(root,text="Start",command=buttonclick12)
button.pack()



        

#inputs


root.mainloop()
# print = str(end_value - start_value) + " NFT are created."
# time.sleep(2)
# print="OpenSea Upload Bot made by YagizWasTaken"
