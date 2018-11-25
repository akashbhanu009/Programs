def fact(x):
    f=1
    while x>=1:
        f=f*x
        x=x-1
        return f
for i in range(1,5):
    print(i,'factorial==> ',fact(i))
