# -*- coding: utf-8 -*-
# filter 滤波器
# filter()把传入的函数依次作用于每个元素，然后根据返回值的True还是False决定
# 保留还是丢弃该元素
def is_palindrome(n):
    n1 = int(str(n)[::-1])
    return n == n1

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')


# sorted()高阶排序函数
#
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_name)
print(L2)
L3 = sorted(L, key=by_score,reverse=True)
print(L3)

