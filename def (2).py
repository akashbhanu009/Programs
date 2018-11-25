# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 23:28:37 2018

@author: lenovo
"""
def print_two(*arg):
    arg1, arg2=arg
    print(f'First Argument:{arg1}\nSecond Argument:{arg2}')
    print('*'*30)

def print_two_again(arg1, arg2):
    print(f'Argument First:{arg1}\nArgument Second:{arg2}')
    print('*'*30)

def print_one(arg1):
    print(f'Onle Single Argument: {arg1}')
    print('*'*30)

def none():
    print('No Arguments THANKS')

print_two('Hello','Hey')
print_two_again(10,88)
print_one('AKASH BHANU TIWARI')
none()
