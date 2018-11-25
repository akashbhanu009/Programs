'''
a = "{} {} {}"
print(a.format("akash", "bhanu", "tiwari"))
print(a.format(1, 2, 3))
print()
print(a.format(1, 2, 3, 4))
print()
print(a.format(1, 2))
'''


def hey(*args):
    arg1, arg2 = args
    print(f"First Arguments==>{arg1} \nSecond Arguments==>{arg2}")


def hello(arg1, arg2):
    print(f"Hello_First_Argument==>{arg1}\nHello_Second_Argument==>{arg2}")


print('*_*' * 30)
hey("print_First", "Print_Second")
print('*_*' * 30)
hello("First", "Second")
