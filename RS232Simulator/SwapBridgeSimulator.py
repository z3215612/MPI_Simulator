#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import IRs232HardWareInterface
import tkinter as tk
from PIL import Image, ImageTk
import threading


class SwapBridgeSimulator(IRs232HardWareInterface.IRs232HardWareInterface):
    DoArray = [0,0,0,0,0,0,0]
    Ack = [36, 48, 50, 77,13]
    CorrectMessage = [33, 48, 50,13]
    InCorrectMessage = [63, 48, 50,13]
    global root 
    global frame ,canvas 
    root = tk.Tk()
    root.title('Simulator')
    root.geometry('800x400')
    frame = tk.Frame(root, width=800, height=400)
    frame.pack()
    canvas = tk.Canvas(frame, width=800, height=400, bg='#fff')
    
    canvas.pack()
    def SimulatorGUI():   
        global root
        root.mainloop()
    def SBDoArray(): 
        global DoArray
        ReadFile = open("SwapBridgeFile.txt", "r")
        ReadStatus = ReadFile.read()
        match ReadStatus:
            case "leftdownup":
                DoArray = [0,1,1,0,0,1,0]
            case "rightupdown":
                DoArray = [1,0,0,1,1,0,0]
            case "leftupup":
                DoArray = [1,0,1,0,0,1,0]
            case "rightupup":
                DoArray = [1,0,1,0,1,0,0]
            case "leftright":
                DoArray = [1,1,1,0,0,0,1]
            case "leftrightdowndown":
                DoArray = [1,1,0,0,0,0,1]
            case "upup":
                DoArray = [0,0,1,0,0,0,1]
            case "downdown":
                DoArray = [0,0,0,0,0,0,1]
        ReadFile.close()
        print(DoArray)  
        
    ###
    def SBGetStatus():
        global SendMessage
        SBfile = open("SwapBridgeFile.txt", "r")
        SBStatus = SBfile.read() 
        SBfile.close()
        match SBStatus:
            case "leftdownup":
                SendMessage = [33,51,50,48,53,48,48,13]
                print("send status back leftdownup")
            case "rightupdown":
                SendMessage = [33,51,56,48,65,48,48,13]
                print("send status back rightupdown")
            case "leftupup":
                SendMessage = [33,65,52,48,68,48,48,13]
                print("send status back leftupup")
            case "rightupup":
                SendMessage = [33,65,56,48,69,48,48,13]
                print("send status back rightupup")
            case "leftright":
                SendMessage = [33,52,54,48,70,48,48,13]
                print("error DI0 DI1 on and all device up ")
            case "upup":
                SendMessage = [33,52,54,48,67,48,48,13]
                print("error DI0 DI1 off and all device up ")
            case "leftrightdowndown":
                SendMessage = [33,52,54,48,51,48,48,13]
                print("error DI0 DI1 on and all device up ")
            case "downdown":
                SendMessage = [33,52,54,48,48,48,48,13]
                print("error DI0 DI1 off and all device up ")
        return SendMessage
        
    def WriteFile(data):
        Demo = open("SwapBridgeFile.txt", "w")
        Demo.write(data)
        Demo.close
    def WriteCheckFile(data):
        Demo = open("SwapBridgeCheckFile.txt", "a")
        Demo.write(data+"\n")
        Demo.close
    def SBSetStatus(data): 
        global DoArray
        print (data)
        if (data[3] == '1'):           
            match data[4]:
                case '0':
                    DoArray[0] = int(data[6])
    
                case '1':
                    DoArray[1] = int(data[6])
    
                case '2':
                    DoArray[2] = int(data[6])
    
                case '3':
                    DoArray[3] = int(data[6])
    
                case '4':
                    DoArray[4] = int(data[6])
    
                case '5':
                    DoArray[5] = int(data[6])
    
                case '6':
                    DoArray[6] = int(data[6])
                    if(data[6]==1):
                        print("Lock")
                    else:
                        print("Unlock")
                        
        print(DoArray)
        
        ##
        if(DoArray == [0,1,1,0,0,1,0]):   
            SwapBridgeSimulator.WriteFile("leftdownup")
            SwapBridgeSimulator.WriteCheckFile("leftdownup")
            SwapBridgeSimulator.GUIImage("leftdownup")
            
        if(DoArray == [1,0,0,1,1,0,0]):       
            SwapBridgeSimulator.WriteFile("rightupdown")
            SwapBridgeSimulator.WriteCheckFile("rightupdown")
            SwapBridgeSimulator.GUIImage("rightupdown")
            
        if(DoArray == [1,0,1,0,0,1,0]):
            SwapBridgeSimulator.WriteFile("leftupup")
            SwapBridgeSimulator.WriteCheckFile("leftupup")
            SwapBridgeSimulator.GUIImage("leftupup")
            
        if(DoArray == [1,0,1,0,1,0,0]):
            SwapBridgeSimulator.WriteFile("rightupup")
            SwapBridgeSimulator.WriteCheckFile("rightupup")
            SwapBridgeSimulator.GUIImage("rightupup")
            
        if(DoArray == [0,1,1,0,0,1,1]):   
            SwapBridgeSimulator.WriteFile("leftdownup")
            SwapBridgeSimulator.GUIImage("leftdownup")
            
        if(DoArray == [1,0,0,1,1,0,1]):       
            SwapBridgeSimulator.WriteFile("rightupdown")
            SwapBridgeSimulator.GUIImage("rightupdown")
            
        if(DoArray == [1,0,1,0,0,1,1]):
            SwapBridgeSimulator.WriteFile("leftupup")
            SwapBridgeSimulator.GUIImage("leftupup")
            
        if(DoArray == [1,0,1,0,1,0,1]):
            SwapBridgeSimulator.WriteFile("rightupup")
            SwapBridgeSimulator.GUIImage("rightupup")
        
    def GUIImage(status):
        #SwapBridgeSimulator.canvas.delete('all')
        global root,frame,canvas 
        img = Image.open( status +'.jpg')        # 開啟圖片
        tk_img = ImageTk.PhotoImage(img)    # 轉換為 tk 圖片物件
        canvas.create_image(0, 0, anchor='nw', image=tk_img)   # 建立圖片        
        canvas.tk_img = tk_img               # 修改屬性更新畫面
        
        print(status)
    def InitialHardware():
        global root
        Demo = open("SwapBridgeFile.txt", "w")
        Status = input("Please input SB status EX:leftup or rightdown etc.\r\n")
        if Status=="":#default
            Demo.write("leftupup")
            SwapBridgeSimulator.GUIImage('leftupup')
        else:
            Demo.write(Status)
            SwapBridgeSimulator.GUIImage(Status)
        Demo.close()
        SwapBridgeSimulator.SBDoArray()
        #SwapBridgeSimulator.SimulatorGUI()
    def GetHardwareReturn(data):
        if (data== "$02M\r"):
            return SwapBridgeSimulator.Ack              
        elif (data== "$026\r"):
            return SwapBridgeSimulator.SBGetStatus()
        elif (data != "" and data[0] == '#'): 
            if (len(data)>6):
                SwapBridgeSimulator.SBSetStatus(data)
            return SwapBridgeSimulator.CorrectMessage#Send !02\r
        else:
            if(data!=""):
                return SwapBridgeSimulator.InCorrectMessage#Send ?02\r
                print("no match codes  "+data)
        return ""