# -*- coding: utf-8 -*-
"""
Created on Fri May  8 13:53:29 2020

@author: Ömer
"""

from tkinter import *

def listToString(l):
    str=""
    for each in l:
        str+=each
    return str

def decimalToBinary(n):
    n= bin(n).replace("0b","")
    length=len(str(n))
    if(length<8):
        while(length<8):
            n="0"+n
            length+=1
        return n
    else:
        return n
    
def division(b,length):
    x=0
    y=6
    divided=[]
    while(True):
        if(y-length==6):
            break
        if(y>length):
            divided.append(b[x:length])
            break
        divided.append(b[x:y])
        x+=6
        y+=6
    return divided

def binaryToDecimal(b):
    asci=[int(a,2) for a in b]
    return asci

def asciToString(a):
    a=[asc+33 for asc in a]
    a=[chr(each) for each in a]
    a=listToString(a)
    return a

def decimalToBinaryEncrypted(n):
    n= bin(n).replace("0b","")
    length=len(str(n))
    if(length<6):
        while(length<6):
            n="0"+n
            length+=1
        return n
    else:
        return n
    
def divisionEncrypted(b):
    x=0
    y=6
    length=len(binaryString)
    divided=[]
    while(True):
        if(y-length==6):
            break
        if(y>length):
            divided.append(b[x:length])
            break
        divided.append(b[x:y])
        x+=6
        y+=6
    return divided

def stringToAscii(s):
    s=(ord(s)-33)
    return s

def eDivision(s,length):
    x=0
    y=8
    divided=[]
    while(True):
        if(y-length==8):
            break
        if(y>length):
            divided.append(s[x:length])
            break
        divided.append(s[x:y])
        x+=8
        y+=8
    return divided

def solveAscii(a):
    a=[chr(each) for each in a]
    a=listToString(a)
    return a


def functionEncrypt():
    message=txtMessage.get("1.0","end-1c")
    stringList=[s for s in message]
    asciiList=[ord(each) for each in stringList]
    binaryList=[decimalToBinary(each) for each in asciiList]
    binaryString=listToString(binaryList)
    dividedList=division(binaryString , len(binaryString))
    encryptedList=binaryToDecimal(dividedList)
    encrypted=asciToString(encryptedList)
    
    txtEMessage.delete("1.0","end-1c")
    txtEMessage.insert("1.0",encrypted)
    
def functionSolve():
    eMeesage=txtEMessage.get("1.0","end-1c")
    eList=[s for s in eMeesage]
    eAscii=[stringToAscii(each) for each in eList]
    eLast=eAscii[-1]
    eAscii.pop()
    eBinaryList=[decimalToBinaryEncrypted(each) for each in eAscii]
    eLastBinary=bin(eLast).replace("0b","")
    eBinaryList.append(eLastBinary)
    l=0
    for each in eBinaryList:
        l+=len(each)
    l=l%8
    if(l!=0):
        while(l<8):
            eBinaryList[-1]="0"+eBinaryList[-1]
            l+=1
    eBinaryString=listToString(eBinaryList)
    eDividedList=eDivision(eBinaryString,len(eBinaryString))
    solvedList=binaryToDecimal(eDividedList)
    solved=solveAscii(solvedList)
    
    txtMessage.delete("1.0","end-1c")
    txtMessage.insert("1.0",solved)
    

frame=Tk()
frame.title("Encryption")
frame.geometry("500x500+100+100")
#Encrypt
lblMessage=Label(frame,pady=10,text="Encrypt")
lblMessage.pack()

txtMessage=Text(frame,height=10, width = 40)
txtMessage.pack()

btnEncrypt=Button(frame,text="Encrypt" , command=functionEncrypt)
btnEncrypt.pack()

#Solve
lblEMessage=Label(frame,pady=10,text="Solve")
lblEMessage.pack()

txtEMessage=Text(frame,height=10, width = 40)
txtEMessage.pack()

btnSolve=Button(frame,text="Solve" , command=functionSolve)
btnSolve.pack()

frame.mainloop()