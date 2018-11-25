'''
a = 10
print("Address of 'a'==>",id(a))
a = 20
print("Address of 'a'==>",id(a))

import keyword
a=keyword.kwlist()
print(a)
'''
'''
s=input("enter some words=")
i=0
for x in s:
    print("""The character present in positive
index {} and negative indx {} is {}""".format(i,i-len(s),x))
i=i+1
'''
n=eval(input('enter the number of rows='))
for i in range(1,n+1):
    print(' '*(n-i),end='')
    print('* '*i)
print()
