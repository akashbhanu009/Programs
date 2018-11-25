# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 06:18:19 2018

@author: lenovo
"""
'''
eno=int(input("Enter Employee number"))
ename=input("Enter Employee Name")
esal=float(input("Enter employee salary"))
eaddr=input("Employee address")
married=bool(input("Emp[loyee are married?[True|False]"))
print()
print("please confirm information")
print(f"Employee number==>{eno}")
print(f"Employee Name==>{ename}")
print(f"Employee Salary==>{esal}")
print(f"Employee address==>{eaddr}")
print(f"Employee are Married==>{married}")
'''
'''
I=eval(input("Enter a list"))
print("type==>",type(I))
print(I)
'''
'''
from sys import argv
print("Print the number of argument",len(argv))
print("The list of command line argument",argv)
print("command line argument one by one")

for x in argv:
    print(x)
'''
from sys import argv
sum=0
args=argv[1:]
for x in args:
    n=int(x)
    sum=sum+n
print(sum)
