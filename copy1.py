# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 21:48:05 2018

@author: lenovo
"""

from sys import argv
from os.path import exists

script, from_file, to_file=argv

print(f"Doe's input file exists {exists(from_file)}")
print(f"Coping from input file {from_file} to ouput file {to_file}")

in_file=open(from_file)
indata=in_file.read()

print(f"Is output file exists? {exists(to_file)}")
input()
out_file=open(to_file,'w')
out_file.write(indata)

from_file.close()
to_file.close()
