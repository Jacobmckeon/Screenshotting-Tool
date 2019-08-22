import pyautogui
import os
import tkinter as tk
from tkinter import *
from pynput.keyboard import Key,Listener
screenshotprefix = ""
directoryname = ""
counter = 0
countertype = ""
def returner():
    a = "abcdefghijklmnopqrstuvwxyz"
    b = list(a.upper())
    c = []
    for z in b:
        c.append(z)
    for i in b:
        for x in b:
            c.append(i + x)
    return c


def on_press(key):
    pass
def on_release(key):
    global counter
    if key == Key.tab:
        x = returner()
        if countertype == "Letters":
            print(key)
            pyautogui.screenshot("%s//%s_%s.png"%(directoryname,screenshotprefix,x[counter]))
            counter +=1
        else:
            counter += 1
            print(key)
            pyautogui.screenshot("%s//%s_%i.png"%(directoryname,screenshotprefix,counter))
class Text(Frame):
    def __init__(self,master):
        
        Frame.__init__(self,master)
        self.master = master
        self.init_window()
        
    def init_window(self):
        self.master.title("directory select")
        self.pack(fill = BOTH, expand = 1)
        L = Label(self,text = " Please select directory name")
        T = Entry(self, width = '20')
        L2 = Label(self,text = "Please select screenshot prefix")
        T2 = Entry(self,width = '20')
        L3 = Label(self,text = " Please select count type")
        args =["Numbers","Letters"]
        var = StringVar(self)
        var.set("Numbers")
        popupmenu = OptionMenu(self, var, *args)
        B = Button(self,text = "Confirm",command = lambda: self.close(root,T,T2,var))
        L.pack()
        T.pack()
        L2.pack()
        T2.pack()
        L3.pack()
        popupmenu.pack()
        B.pack()
        
    def close(self,root,T,T2,var):
        global directoryname
        directoryname = T.get()
        global screenshotprefix
        screenshotprefix = T2.get()
        print(screenshotprefix)
        os.mkdir(directoryname)
        print(directoryname)
        global countertype
        countertype = var.get()
        print(countertype)
        root.destroy()
root = Tk()
root.geometry("400x300")    
app = Text(root)
root.mainloop()
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

