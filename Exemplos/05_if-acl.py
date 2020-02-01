# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 18:32:11 2020

@author: CEC
"""

aclNum = int(input("what is the Ipv4 ACL munber? "))
if aclNum >= 1 and aclNum<= 99:
    print ("This is the a standar IPv4 ACL.")
elif aclNum >=100 and aclNum <=199:
    print("This is a extended IPv4 ACL: ")
else:
    print("this is not a standar or extended IPv4 ACL")
    
         
