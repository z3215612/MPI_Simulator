#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
ReadFileTest = open("SBtestfile.txt", "r")
ReadFileCheck = open("SwapBridgeCheckFile.txt", "r")
#Status = input("please input initial status")
Status = ReadFileCheck.readline().replace("\n","")

while(True): 
    ReadLineTest = ReadFileTest.readline()
    try:
        ReadStatus = ReadLineTest.split(" ")[1]
        ReadStatus = ReadStatus.strip().replace("\n","")
    except:
        continue
    print (ReadStatus)
    os.system("pause")
    if ReadStatus == "left":        
        if ReadStatus in Status:
            continue
        else:
            Status = "leftup"
            CheckStatus = ReadFileCheck.readline().replace("\n","")
            if Status == CheckStatus:
                print("OK")
            else :
                print("ERROR")
    if ReadStatus == "right":        
        if ReadStatus in Status:
            continue
        elif (Status == "leftdown"):
            continue
        else:
            Status = "rightup"
            CheckStatus = ReadFileCheck.readline().replace("\n","")
            if Status == CheckStatus:
                print("OK")
            else :
                print("ERROR")
    if ReadStatus == "left,up":        
        if ReadStatus.split(",")[0] in Status:
            if ReadStatus.split(",")[1] in Status:
                continue
            else:
                Status = "leftup" 
                CheckStatus = ReadFileCheck.readline().replace("\n","")
                if Status == CheckStatus:
                    print("OK")
                else :
                    print("ERROR")
        else:
            Status = "leftup"
            CheckStatus = ReadFileCheck.readline().replace("\n","")
            if Status == CheckStatus:
                print("OK")
            else :
                print("ERROR")
    if ReadStatus == "left,down":        
        if ReadStatus.split(",")[0] in Status:
            if ReadStatus.split(",")[1] in Status:
                continue
            else:
                Status = "leftdown" 
                CheckStatus = ReadFileCheck.readline().replace("\n","")
                if Status == CheckStatus:
                    print("OK")
                else :
                    print("ERROR")
        else:
            Status = "leftdown"
            CheckStatus = ReadFileCheck.readline().replace("\n","")
            if Status == CheckStatus:
                print("OK")
            else :
                print("ERROR")
    if ReadStatus == "right,up":        
        if ReadStatus.split(",")[0] in Status:
            if ReadStatus.split(",")[1] in Status:
                continue
            else:
                Status = "rightup" 
                CheckStatus = ReadFileCheck.readline().replace("\n","")
                if Status == CheckStatus:
                    print("OK")
                else :
                    print("ERROR")
        else:
            Status = "rightup"
            CheckStatus = ReadFileCheck.readline().replace("\n","")
            if Status == CheckStatus:
                print("OK")
            else :
                print("ERROR")
    if ReadStatus == "right,down":        
        if ReadStatus.split(",")[0] in Status:
            if ReadStatus.split(",")[1] in Status:
                continue
            else:
                Status = "rightup" 
                CheckStatus = ReadFileCheck.readline().replace("\n","")
                if Status == CheckStatus:
                    print("OK")
                else :
                    print("ERROR")
        else:
            Status = "rightup"
            CheckStatus = ReadFileCheck.readline().replace("\n","")
            if Status == CheckStatus:
                print("OK")
            else :
                print("ERROR")
    if ReadStatus == "current,up":       
        if ReadStatus.split(",")[1] in Status:
            continue
        else:
            if Status == "leftdown":
                Status = "leftup" 
                CheckStatus = ReadFileCheck.readline().replace("\n","")
                if Status == CheckStatus:
                    print("OK")
                else :
                    print("ERROR")
            
    if ReadStatus == "current,down":       
        if ReadStatus.split(",")[1] in Status:
            continue
        else:
            if Status == "leftup":
                Status = "leftdown" 
                CheckStatus = ReadFileCheck.readline().replace("\n","")
                if Status == CheckStatus:
                    print("OK")
                else :
                    print("ERROR")
            if Status == "rightup":
                CheckStatus = ReadFileCheck.readline().replace("\n","")
                if Status == CheckStatus:
                    print("OK")
                else :
                    print("ERROR")
if ReadStatus == "f1,press":       
        if "leftup" in Status:
            continue
        else:
            if Status == "leftdown":
                Status = "leftup" 
                CheckStatus = ReadFileCheck.readline().replace("\n","")
                if Status == CheckStatus:
                    print("OK")
                else :
                    print("ERROR")
            if Status == "rightup":
                Status = "leftup" 
                CheckStatus = ReadFileCheck.readline().replace("\n","")
                if Status == CheckStatus:
                    print("OK")
                else :
                    print("ERROR")
if ReadStatus == "f2,press":       
        if "rightup" in Status:
            continue
        else:
            if Status == "leftup":
                Status = "rightup" 
                CheckStatus = ReadFileCheck.readline().replace("\n","")
                if Status == CheckStatus:
                    print("OK")
                else :
                    print("ERROR")
            if Status == "leftdown":
                Status = "rightup"
                CheckStatus = ReadFileCheck.readline().replace("\n","")
                if Status == CheckStatus:
                    print("OK")
                else :
                    print("ERROR")