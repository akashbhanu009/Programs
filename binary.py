# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:53:57 2018

@author: lenovo
"""

a=10
b=0b10
c=0o10
d=0xffce
print(f"This ia a DECIMAL representation of {a} ==>",a)
print(f"This is BINARY representationn of {b} ==>",b)
print(f"This is OCTAL representation of {c} ==>",c)
print(f"This is HEXA representation of {d} ==>",d)
print("Type of 'A'==>",type(a),"and its ID==>",id(a))
print("Type of 'B'==>", type(b),"and its ID==>",id(b))
print("Type of 'C'==>",type(c),"and its ID==>",id(c))
print("type of 'D'==>",type(d),"and its ID==>",id(d))
print('*_*'*30)
a=3+2.5j # complex number
print(type(a)) 
print(a.real) # real number
print(a.imag) #imaginary number