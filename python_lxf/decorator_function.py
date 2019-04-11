# -*- coding: utf-8 -*-
# decorator 装饰器，可以动态的增加函数的功能，本质上，decorator是一个返回函数的高阶函数，
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        t1 =time.time()
        r = fn(*args,**kwargs)
        t2 = time.time()


        print('%s executed in %s ms' % (fn.__name__, t2-t1))
        return r
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(1)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(1)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')