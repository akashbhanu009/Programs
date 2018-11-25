hello = "{} {} {} {}"

print(hello.format(1, 2, 3, 4))

print(hello.format(True, False, False, True))

print(hello.format({}, {}, {}, {}))

print(hello.format(hello, hello, hello, hello))

print(hello.format('Try your', 'own text here',
                   'May be poem', 'or a song without fear understand'))


cat = 10
x = f'I have total {cat} numbers of cat'

dog = 8
y = f'I have {dog} numbes of dog beware about your cat'

print(x, y)
print('.' * 20)

print('So, you both are {} lovers!'.format('PET'))
print(f'Mr. john have total cats:{cat}')
