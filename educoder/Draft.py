
# 完全数
x = eval(input())
for n in range(2, x):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i
    if sum == n and i < n:
        print(sum)


# 求阶乘
x = eval(input())
a = 1
for i in range(1, x + 1):
    print("%d!=" % i, end="")
    s = 1
    for a in range(1, i + 1):
        print("%d" % a, end="")
        s *= a
        if a == i:
            print("=%d" % s)
            break
        print("*", end="")
        a += 1


# 输出一个三位数，每一位都小于input的数
x = eval(input())
i = 1
for a in range(1, x + 1):
    print(a, end="")
    for b in range(0, x + 1):
        if b == a:
            continue
        print(b, end="")
        for c in range(0, x + 1):
            if c == a or c == b:
                continue
            print(c, end=" ")
            if i % 10 == 0 and i >= 10:
                print()
            i += 1

# 鸡兔同笼
t = eval(input())
j = eval(input())
for a in range(int(j/4) + 1):
    if 4*a + 2*(t - a) == j:
        print("鸡{}只兔子{}只".format(t - a, a))
        break
if a == int(j/4):
    print("无解")