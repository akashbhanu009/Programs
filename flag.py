# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 19:05:27 2018

@author: lenovo
"""

s=input("Enter main string:")   
subs=input("Enter sub string:")   
flag=False   
pos=-1   
n=len(s) 
while True:   
    pos=s.find(subs,pos+1,n)    
    if pos!=-1:
        print("Found at index :",pos)
        flag=True
    else:
        break

if(flag==True):
    if pos!=-1:
        print("Found")   
else:
    if pos==-1:
        print("String Not Found")