# -*- coding: utf-8 -*-
# 高阶函数map/reduce
def normalize(name):
    a1 = name[0]
    a2 = name[1:]
    a1 = a1.upper()
    a2 = a2.lower()
    return a1+a2

print('例子1')
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


from functools import reduce
def prod(x):
    return reduce(lambda x,y:x*y,x)


print('例子2')
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def str2float(x):
    i = get_index(x)
    return reduce(lambda x,y:x*10+y,map(char2num,re.sub(r'\.','',x)))/10**i



import re
def char2num(s):
   digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
   return digits[s]
def get_index(a):
    lens = len(a)
    for i,j in enumerate(a):
        if j == '.':
            return lens-i-1

print('例子3')
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
