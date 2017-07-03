x = "pi"
y = "pie"
x, y = y, x
# print(x, y)


def f(x):
    while x > 3:
        print(x)
        f(x+1)
# f(4)


def f1(x):
    x = x + 1
    print(f1, x)


def f2(x):
    print('f2', x)
    return x

x = 2
# f1(x)
# f2(x)

# i=0
# j=-1
# while i >= 0:
#     while j >= 0:
#         print(i, j)


def f3():
    print(2)
    return 3
a = f3()

list = [2, 1]
tup = (list, 3)
print(tup)
list.append(4)
print(tup)
