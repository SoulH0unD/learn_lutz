sep = '-' * 45 + '\n'

#Исключение генерируется и перехватывается
print(sep + 'EXCEPTION RAISED AND CAUGHT')
try:
    x = 'spam'[99]
except IndexError:
    print('except run')
finally:
    print('finnaly run')
print('after run')


#Исключение не генерируется
print(sep + 'NO EXCEPTION RAISED')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
finally:
    print('finnaly run')
print('after run')


#Исключение не генерируется, c конструкцией else
print(sep + 'NO EXCEPTION RAISED, WITH ELSE')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finnaly run')
print('after run')


#Исключение генерируется, но не перехватывается
print(sep + 'EXCEPTION RAISED BAD NOT CAUGHT')
try:
    x = 1 / 0
except IndexError:
    print('except run')
finally:
    print('finnaly run')
print('after run')