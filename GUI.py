# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:14:45 2020

@author: Ömer
"""
def Naber():
    print("naber")

from tkinter import *
root = Tk()
Label(root, text="Username").grid(row=0, sticky=W)
Label(root, text="Password").grid(row=1, sticky=W)
Entry(root).grid(row=0, column=1, sticky=E)
Entry(root).grid(row=1, column=1, sticky=E)
Button(root, text="Login" ,command=Naber).grid(row=2, column=1, sticky=E)
root.mainloop()