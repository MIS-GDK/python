# _*_ coding: utf-8 _*_
import os
from functools import reduce
from collections import Iterable
# print(os.path.abspath('.'))
# print(os.environ.get('PATH'))
# os.mkdir('./testdir')

print([
    x for x in os.listdir('.')
    if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'
])


def add(x, y):
    return x + y


mm = reduce(add, [1, -10, -100, -90, -35])
print(mm)

nn = filter(lambda n: n % 2 == 1, [1, 2, 4, 5, 6, 9, 10, 15])
print(list(nn))

print(sorted([-1, 1000, -100, 20, 19, 44, 23], key=abs))

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(d[key])
print('    ')
g = (x * x for x in range(1, 11))
for n in g:
    print(n)
print(isinstance([], Iterable))

print('1122')
