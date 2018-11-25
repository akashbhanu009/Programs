'''
n=int(input('enter rows='))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print()
'''
'''
n=eval(input('enter rows'))
for i in range(1,n+1):
    print('*'*i,end='')
    print()
'''
n=eval(input('enter the number of rows='))
for i in range(1,n+1):
    #for j in range(1,i+1):
    print(' '*(n-i),end='')
    print('* '*i)
print()
