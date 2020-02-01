# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 09:26:19 2020

@author: CEC
"""
file = open("devices.txt","a")
while (True):
    Newitem=input("Enter a new User: ")
    if Newitem == "exit":
        print("All done¡")
        break 
    file.write(Newitem + "\n")
file.close()

devices=[]
file = open("devices.txt","r")
for item in file:
    devices.append(item)
file.close()
print(devices)
def fun(x):
    if x%==0:
        return 1
    else:
        return print(fun(fun(2)))