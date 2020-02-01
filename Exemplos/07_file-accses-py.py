# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 08:45:49 2020

@author: CEC
"""
devices=[]
file = open("devices.txt","r")
for item in file:
    item=item.strip()
    devices.append(item)
file.close()
print(devices)