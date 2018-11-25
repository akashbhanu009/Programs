# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 15:27:33 2018

@author: lenovo
"""
'''
from sys import argv

script,filename=argv

print(f'this is your {filename} file')
t=open(filename)
print(t.read())
print("*-*"*30)

file=input(print('can you please give another file name'))

t1=open(file)
print(t1.read())
print('*'*10,"FINISH THANKS",'*'*10)
'''
from sys import argv
script, file =argv
print(f"This is the script {script}")
print(f'This is the {file} file name you enter')
input('?')
text=open(file,'w')

print("now truncate your file:")
print('?')
text.truncate()

print("Please enter three lines to write in file")
line1=input('First line:')
line2=input('Second line:')
line3=input('Third line:')
print('*'*30)
print('Now I am going to write these linnes in file')
text.write(line1)
text.write('\n')
text.write(line2)
text.write('\n')
text.write(line3)
text.write('\n')

#text.open('r')
print('Now close the file')
text.close()
