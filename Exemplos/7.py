# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 19:14:24 2020

@author: CEC
"""
def isYearLeap(yr):
    if yr % 4!=0:
        return False
    elif yr % 100!=0:
        return True
    elif yr % 400!=0:
        return False 
    else:
        return True
    
def daysInMonth(yr, mo):
    if yr<1582 or mo<1 or mo>12:
        return None 
    days =[31,28,31,30,31,30,31,31,30,31,30,31] 
    res =days[mo-1]
    if mo==2 and isYearLeap(yr):
        res=29
    return res   

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

        
