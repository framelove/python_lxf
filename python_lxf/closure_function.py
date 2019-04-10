# -*- coding: utf-8 -*-
# 闭包，函数的返回仍是一个函数
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量，不然会产生事与愿违的结果
# 要求：利用闭包返回一个计数器函数，每次调用它返回递增整数

def createCounter():
    i = [0]
    def counter():
        i[0] += 1
        return i[0]
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
