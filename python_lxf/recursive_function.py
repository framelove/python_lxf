# 递归函数的使用

# 汉诺塔的移动

def move(n, a, b, c):
    if n == 1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1, a, b, c)
        move(n-1,b,c,a)
move(3,'a','b','c')